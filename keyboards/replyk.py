from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from text import TEXTS

def get_join_nso_keyboard(lang: str):
    """
    Создает Reply-клавиатуру с кнопкой "Вступить в НСО" на выбранном языке.
    """
    builder = ReplyKeyboardBuilder()
    # Получаем текст кнопки из словаря TEXTS по выбранному языку: язык передается в аргумент lang, по нему ищется соответствущий словарь keyboard_reply_buttons, 
    # в нем ищется соответствущий ключ join_nso_button
    join_button_text = TEXTS[lang]['keyboard_reply_buttons']['join_nso_button']
    builder.add(KeyboardButton(text=join_button_text))
    builder.adjust(1) # Кнопка будет на новой строке
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True) # 1. делаем кнопку небольшой; 2. Избавляемся от клавиатуры после нажатия кнопки