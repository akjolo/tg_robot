from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, PicklePersistence, MessageHandler, Filters, ConversationHandler
from android import TOKEN
import os

ENTER_NAME, ENTER_PHONE, UPLOAD_RESUME = range(3)

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Привет! Пожалуйста, введите ваше имя:")
    context.user_data[chat_id] = {}
    context.user_data[chat_id]['files'] = []
    return ENTER_NAME

def receive_name(update, context):
    chat_id = update.effective_chat.id
    name = update.message.text
    context.user_data[chat_id]['name'] = name
    context.bot.send_message(chat_id=chat_id, text="Отлично! Теперь введите ваш номер телефона:")
    return ENTER_PHONE

def receive_phone(update, context):
    chat_id = update.effective_chat.id
    phone = update.message.text
    context.user_data[chat_id]['phone'] = phone
    context.bot.send_message(chat_id=chat_id, text="Спасибо! Пожалуйста, отправьте ваше резюме в расширении.docx:")
    return UPLOAD_RESUME

def receive_document(update, context):
    chat_id = update.effective_chat.id
    document = update.message.document
    file_id = document.file_id
    new_file = context.bot.get_file(file_id)
    file_path = f'{chat_id}_file_{len(context.user_data[chat_id]["files"])}.docx'
    new_file.download(file_path)
    context.user_data[chat_id]['files'].append(file_path)

    # Проверяем количество отправленных файлов
    if len(context.user_data[chat_id]['files']) == 1:
        context.bot.send_message(chat_id=chat_id, text="Файл успешно получен! Отправьте еще файл или /submit для завершения.", reply_markup=get_inline_keyboard_markup())

    return UPLOAD_RESUME

def submit(update, context):
    chat_id = update.effective_chat.id
    send_data_to_me(context, chat_id)
    return ConversationHandler.END

def send_data_to_me(context, chat_id):
    user_data = context.user_data.get(chat_id, None)
    if user_data:
        name = user_data['name']
        phone = user_data['phone']
        files = user_data['files']
        score = len(files)  # the score is the number of submitted files

        if score >= 15:  # минимальный проходной балл
            context.bot.send_message(chat_id=-945828460, text=f"Имя:{name}\nТелефон: {phone}\nБаллы: {score}")
            for file in files:
                with open(file, 'rb') as f:
                    context.bot.send_document(chat_id=-945828460, document=f)

def get_inline_keyboard_markup():
    keyboard = [
        [
            InlineKeyboardButton("Завершение", callback_data='submit')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def button(update, context):
    query = update.callback_query
    if query.data == 'submit':
        submit(update, context)

updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
dispatcher = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        ENTER_NAME: [MessageHandler(Filters.text, receive_name)],
        ENTER_PHONE: [MessageHandler(Filters.text, receive_phone)],
        UPLOAD_RESUME: [MessageHandler(Filters.document, receive_document)],
    },
    fallbacks=[CommandHandler('start', start)],
)

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(CommandHandler('submit', submit))
dispatcher.add_handler(CallbackQueryHandler(button))


updater.start_polling()
updater.idle()
