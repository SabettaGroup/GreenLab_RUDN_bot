from text import TEXTS
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


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

def get_final_keyboard(lang: str) -> ReplyKeyboardMarkup:
    '''клава по окончании заполнения анкеты'''
    buttons = TEXTS[lang]['keyboard_reply_buttons']
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=buttons['become_an_org'])],
            [KeyboardButton(text=buttons['waste_sorting'])]
        ],
        resize_keyboard=True,
        one_time_keyboard=False # Клавиатура остается после использования
    )
    return keyboard
