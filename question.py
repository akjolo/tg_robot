# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, PicklePersistence, MessageHandler, Filters, ConversationHandler
# from android import TOKEN

# users = {}
# ENTER_NAME, ENTER_PHONE, UPLOAD_RESUME = range(3)

# def start(update, context):
#     chat_id = update.effective_chat.id
#     context.bot.send_message(chat_id=chat_id, text="Привет! Пожалуйста, введите ваше имя:")
#     users[chat_id] = {}
#     return ENTER_NAME

# def receive_name(update, context):
#     chat_id = update.effective_chat.id
#     name = update.message.text
#     users[chat_id]['name'] = name
#     context.bot.send_message(chat_id=chat_id, text="Отлично! Теперь введите ваш номер телефона:")
#     return ENTER_PHONE

# def receive_phone(update, context):
#     chat_id = update.effective_chat.id
#     phone = update.message.text
#     users[chat_id]['phone'] = phone
#     context.bot.send_message(chat_id=chat_id, text="Спасибо! Пожалуйста, отправьте ваше резюме в расширении.docx:")
#     return UPLOAD_RESUME

# def receive_document(update, context):
#     chat_id = update.effective_chat.id
#     document = update.message.document
#     file_id = document.file_id
#     new_file = context.bot.get_file(file_id)
#     new_file.download('file.docx')
#     context.bot.send_message(chat_id=chat_id, text="Файл успешно получен!")
#     send_data_to_me(context, chat_id)
#     return ConversationHandler.END

# def send_data_to_me(context, chat_id):
#     user_data = users.get(chat_id, None)
#     if user_data:
#         name = user_data['name']
#         phone = user_data['phone']
#         score = context.chat_data.get('score', 0)
#         if score >= 15:  # минимальный проходной балл
#             context.bot.send_message(chat_id=-945828460, text=f"Имя:{name}\nТелефон: {phone}\nБаллы: {score}")

# def test(update, context):
#     update.message.reply_text(f'Здравcтвуйте')
#     keyboard1 = [
#         [InlineKeyboardButton('(1) x == x + 1', callback_data='1_1'), InlineKeyboardButton('(2) x = x + 1', callback_data='1_2')],
#         [InlineKeyboardButton('(3) x == 1 + x', callback_data='1_3'), InlineKeyboardButton('(4) x = 1', callback_data='1_4')]
#     ]
#     reply_markup1 = InlineKeyboardMarkup(keyboard1)
#     update.message.reply_text('Укажите выражение , корректно соответствующее понятию "инкремент"', reply_markup=reply_markup1)
    
#     keyboard2 = [
#         [InlineKeyboardButton('(1) Hel', callback_data='2_1'), InlineKeyboardButton('(2) Hell', callback_data='2_2')],
#         [InlineKeyboardButton('(3) Hello', callback_data='2_3'), InlineKeyboardButton('(4) ello!', callback_data='2_4')]
#     ]
#     reply_markup2 = InlineKeyboardMarkup(keyboard2)
#     update.message.reply_text('Укажите корректный результат выполнения кода >>>myString="Hello!" >>>print myString[0:4]', reply_markup=reply_markup2)
#     keyboard3 = [
#         [InlineKeyboardButton('(1) >>>while (x=2)', callback_data='3_1'), InlineKeyboardButton('(2) >>>while (x==2)', callback_data='3_2')],
#         [InlineKeyboardButton('(3) >>>while (x+2)', callback_data='3_3'), InlineKeyboardButton('(4) >>>while (x>2)', callback_data='3_4')]
#     ]
#     reply_markup3 = InlineKeyboardMarkup(keyboard3)
#     update.message.reply_text('Укажите корректный синтаксис использование инструкции while', reply_markup=reply_markup3)
#     keyboard4 = [
#         [InlineKeyboardButton('(1) \n', callback_data='4_1'), InlineKeyboardButton('(2) \eol', callback_data='4_2')],
#         [InlineKeyboardButton('(3) \\l', callback_data='4_3'), InlineKeyboardButton('(4) \/n', callback_data='4_4')]
#     ]
#     reply_markup4 = InlineKeyboardMarkup(keyboard4)
#     update.message.reply_text('Укажите, как корректно отображается спецсимвол "конец строки"', reply_markup=reply_markup4)
#     keyboard5 = [
#         [InlineKeyboardButton('(1) x = 8', callback_data='5_1'), InlineKeyboardButton('(2) x == 8', callback_data='5_2')],
#         [InlineKeyboardButton('(3) x := 8', callback_data='5_3'), InlineKeyboardButton('(4) x is 8', callback_data='5_4')]
#     ]
#     reply_markup5 = InlineKeyboardMarkup(keyboard5)
#     update.message.reply_text('Укажите правильный синтаксис присвоения переменной х значания 8', reply_markup=reply_markup5)
#     keyboard6 = [
#         [InlineKeyboardButton('(1) (0,1,2,3,4)', callback_data='6_1'), InlineKeyboardButton('(2) (7, 2, 3, 4))|', callback_data='6_2')],
#         [InlineKeyboardButton('(3) (7,3,4)', callback_data='6_3'), InlineKeyboardButton('(4) TypeError: object doesn`t support item assignment', callback_data='6_4')]
#     ]
#     reply_markup6 = InlineKeyboardMarkup(keyboard6)
#     update.message.reply_text('Выберите правильный результат работы кода myTuple=(0,1,2,3,4) myTuple = (7,) + myTuple[2:] print myTuple', reply_markup=reply_markup6)
#     keyboard7 = [
#         [InlineKeyboardButton('(1) music, Tracks', callback_data='7_1'), InlineKeyboardButton('(2) TABLE, title', callback_data='7_2')],
#         [InlineKeyboardButton('(3) title, plays|', callback_data='7_3'), InlineKeyboardButton('(4) Tracks, title', callback_data='7_4')]
#     ]
#     reply_markup7 = InlineKeyboardMarkup(keyboard7)
#     update.message.reply_text('Укажите, какие поля составляют структуры базы данных music.db', reply_markup=reply_markup7)
#     keyboard8 = [
#         [InlineKeyboardButton('(1) 0', callback_data='8_1'), InlineKeyboardButton('(2) 10', callback_data='8_2')],
#         [InlineKeyboardButton('(3) 2', callback_data='8_3'), InlineKeyboardButton('(4) 5', callback_data='8_4')]
#     ]
#     reply_markup8 = InlineKeyboardMarkup(keyboard8)
#     update.message.reply_text('Какое значение НЕ может быть получено в результате выполнения инструкции >>>print random.random()*10', reply_markup=reply_markup8)
#     keyboard9 = [
#         [InlineKeyboardButton('кортеж (tuple)', callback_data='9_1'), InlineKeyboardButton('список (list)', callback_data='9_2')],
#         [InlineKeyboardButton('множество (set)*', callback_data='9_3'), InlineKeyboardButton('словарь (dict)', callback_data='9_4')]
#     ]
#     reply_markup9 = InlineKeyboardMarkup(keyboard9)
#     update.message.reply_text('Необходимо собрать и вывести все уникальные слова из строки рекламного текста. Какой из перечисленных типов данных Python подходит лучше всего?', reply_markup=reply_markup9)
#     keyboard10 = [
#         [InlineKeyboardButton('', callback_data='10_1'), InlineKeyboardButton('', callback_data='10_2')],
#         [InlineKeyboardButton('', callback_data='10_3'), InlineKeyboardButton('', callback_data='10_4')]
#     ]
#     reply_markup10 = InlineKeyboardMarkup(keyboard10)
#     update.message.reply_text('', reply_markup=reply_markup10)
#     keyboard11 = [
#         [InlineKeyboardButton('', callback_data='11_1'), InlineKeyboardButton('', callback_data='11_2')],
#         [InlineKeyboardButton('', callback_data='11_3'), InlineKeyboardButton('', callback_data='11_4')]
#     ]
#     reply_markup11 = InlineKeyboardMarkup(keyboard11)
#     update.message.reply_text('', reply_markup=reply_markup11)
#     keyboard12 = [
#         [InlineKeyboardButton('', callback_data='12_1'), InlineKeyboardButton('', callback_data='12_2')],
#         [InlineKeyboardButton('', callback_data='12_3'), InlineKeyboardButton('', callback_data='12_4')]
#     ]
#     reply_markup12 = InlineKeyboardMarkup(keyboard12)
#     update.message.reply_text('', reply_markup=reply_markup12)
#     keyboard13 = [
#         [InlineKeyboardButton('', callback_data='13_1'), InlineKeyboardButton('', callback_data='13_2')],
#         [InlineKeyboardButton('', callback_data='13_3'), InlineKeyboardButton('', callback_data='13_4')]
#     ]
#     reply_markup13 = InlineKeyboardMarkup(keyboard13)
#     update.message.reply_text('', reply_markup=reply_markup13)
#     keyboard14 = [
#         [InlineKeyboardButton('', callback_data='14_1'), InlineKeyboardButton('', callback_data='14_2')],
#         [InlineKeyboardButton('', callback_data='14_3'), InlineKeyboardButton('', callback_data='14_4')]
#     ]
#     reply_markup14 = InlineKeyboardMarkup(keyboard14)
#     update.message.reply_text('', reply_markup=reply_markup14)
#     keyboard15 = [
#         [InlineKeyboardButton('', callback_data='15_1'), InlineKeyboardButton('', callback_data='15_2')],
#         [InlineKeyboardButton('', callback_data='15_3'), InlineKeyboardButton('', callback_data='15_4')]
#     ]
#     reply_markup15 = InlineKeyboardMarkup(keyboard15)
#     update.message.reply_text('', reply_markup=reply_markup15)
#     keyboard16 = [
#         [InlineKeyboardButton('', callback_data='16_1'), InlineKeyboardButton('', callback_data='16_2')],
#         [InlineKeyboardButton('', callback_data='16_3'), InlineKeyboardButton('', callback_data='16_4')]
#     ]
#     reply_markup16 = InlineKeyboardMarkup(keyboard16)
#     update.message.reply_text('', reply_markup=reply_markup16)
#     keyboard17 = [
#         [InlineKeyboardButton('', callback_data='17_1'), InlineKeyboardButton('', callback_data='17_2')],
#         [InlineKeyboardButton('', callback_data='17_3'), InlineKeyboardButton('', callback_data='17_4')]
#     ]
#     reply_markup17 = InlineKeyboardMarkup(keyboard17)
#     update.message.reply_text('', reply_markup=reply_markup17)
#     keyboard18 = [
#         [InlineKeyboardButton('', callback_data='18_1'), InlineKeyboardButton('', callback_data='18_2')],
#         [InlineKeyboardButton('', callback_data='18_3'), InlineKeyboardButton('', callback_data='18_4')]
#     ]
#     reply_markup18 = InlineKeyboardMarkup(keyboard18)
#     update.message.reply_text('', reply_markup=reply_markup18)
#     keyboard19 = [
#         [InlineKeyboardButton('', callback_data='19_1'), InlineKeyboardButton('', callback_data='19_2')],
#         [InlineKeyboardButton('', callback_data='19_3'), InlineKeyboardButton('', callback_data='19_4')]
#     ]
#     reply_markup19 = InlineKeyboardMarkup(keyboard19)
#     update.message.reply_text('', reply_markup=reply_markup19)
#     keyboard20 = [
#         [InlineKeyboardButton('20', callback_data='_1'), InlineKeyboardButton('', callback_data='20_2')],
#         [InlineKeyboardButton('20', callback_data='_3'), InlineKeyboardButton('', callback_data='20_4')]
#     ]
#     reply_markup20 = InlineKeyboardMarkup(keyboard20)
#     update.message.reply_text('', reply_markup=reply_markup20)
#     keyboard21 = [
#         [InlineKeyboardButton('', callback_data='21_1'), InlineKeyboardButton('', callback_data='21_2')],
#         [InlineKeyboardButton('', callback_data='21_3'), InlineKeyboardButton('', callback_data='21_4')]
#     ]
#     reply_markup21 = InlineKeyboardMarkup(keyboard21)
#     update.message.reply_text('', reply_markup=reply_markup21)
#     keyboard22 = [
#         [InlineKeyboardButton('', callback_data='22_1'), InlineKeyboardButton('', callback_data='22_2')],
#         [InlineKeyboardButton('', callback_data='22_3'), InlineKeyboardButton('', callback_data='22_4')]
#     ]
#     reply_markup22 = InlineKeyboardMarkup(keyboard22)
#     update.message.reply_text('', reply_markup=reply_markup22)
#     keyboard23 = [
#         [InlineKeyboardButton('', callback_data='23_1'), InlineKeyboardButton('', callback_data='23_2')],
#         [InlineKeyboardButton('', callback_data='23_3'), InlineKeyboardButton('', callback_data='23_4')]
#     ]
#     reply_markup23 = InlineKeyboardMarkup(keyboard23)
#     update.message.reply_text('', reply_markup=reply_markup23)
#     keyboard24 = [
#         [InlineKeyboardButton('', callback_data='24_1'), InlineKeyboardButton('', callback_data='24_2')],
#         [InlineKeyboardButton('', callback_data='24_3'), InlineKeyboardButton('', callback_data='24_4')]
#     ]
#     reply_markup24 = InlineKeyboardMarkup(keyboard24)
#     update.message.reply_text('', reply_markup=reply_markup24)
#     keyboard25 = [
#         [InlineKeyboardButton('', callback_data='25_1'), InlineKeyboardButton('', callback_data='25_2')],
#         [InlineKeyboardButton('', callback_data='25_3'), InlineKeyboardButton('', callback_data='25_4')]
#     ]
#     reply_markup25 = InlineKeyboardMarkup(keyboard25)
#     update.message.reply_text('', reply_markup=reply_markup25)
    

# def button(update, context):
#     query = update.callback_query
#     question, user_answer = map(int, query.data.split('_'))
#     if 'score' not in context.chat_data:
#         context.chat_data['score'] = 0
#     if  (question == 1 and user_answer == 2) or (question == 2 and user_answer == 3):
#         context.chat_data['score'] += 1
#         query.answer("Ответ успешно отправлен")
#         send_data_to_me(context, query.message.chat_id)

# updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
# dispatcher = updater.dispatcher

# conv_handler = ConversationHandler(
#     entry_points=[CommandHandler('start', start)],
#     states={
#         ENTER_NAME: [MessageHandler(Filters.text, receive_name)],
#         ENTER_PHONE: [MessageHandler(Filters.text, receive_phone)],
#         UPLOAD_RESUME: [MessageHandler(Filters.document, receive_document)],
#     },
#     fallbacks=[CommandHandler('start', start)],
# )

# dispatcher.add_handler(conv_handler)
# dispatcher.add_handler(CallbackQueryHandler(button))
# dispatcher.add_handler(CommandHandler('test', test))

# updater.start_polling()
# updater.idle()

    
