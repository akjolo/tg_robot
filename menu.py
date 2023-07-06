import telegram
from key_buttons import tele_button

def main_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(tele_button[0])],
        [telegram.KeyboardButton(tele_button[1])],
        [telegram.KeyboardButton(tele_button[2])],
    ])
    

    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False 
    )    