from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from text import LANGUAGES

def get_language_keyboard():
    """Создает инлайн-клавиатуру для выбора языка, беря варианты из LANGUAGES"""
    builder = InlineKeyboardBuilder()
    for lang_code, lang_text in LANGUAGES.items():
        builder.add(InlineKeyboardButton(text=lang_text, callback_data=lang_code))

    builder.adjust(1)

    return builder.as_markup()