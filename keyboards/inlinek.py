from text import LANGUAGES, TEXTS
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_language_keyboard() -> InlineKeyboardBuilder:
    """Создает инлайн-клавиатуру для выбора языка, беря варианты из LANGUAGES"""
    builder = InlineKeyboardBuilder()
    for lang_code, lang_text in LANGUAGES.items():
        builder.add(InlineKeyboardButton(text=lang_text, callback_data=lang_code))
    builder.adjust(1)
    return builder.as_markup()

def get_course_level_keyboard(lang: str) -> InlineKeyboardBuilder:
    """
    Создает инлайн-клавиатуру для выбора уровня образования.
    """
    builder = InlineKeyboardBuilder()
    # Получаем данные для уровней из TEXTS
    levels = TEXTS[lang].get('keyboard_levels', {}) 
    
    # Добавляем кнопки уровня образования
    if 'bachelor' in levels:
        builder.add(InlineKeyboardButton(text=levels['bachelor'], callback_data="level_bachelor"))
    if 'master' in levels:
        builder.add(InlineKeyboardButton(text=levels['master'], callback_data="level_master"))
    if 'phd' in levels:
        builder.add(InlineKeyboardButton(text=levels['phd'], callback_data="level_phd"))
        
    builder.adjust(1) # Располагаем кнопки друг под другом
    return builder

def get_course_number_keyboard(lang: str) -> InlineKeyboardBuilder:
    """
    Создает инлайн-клавиатуру для выбора номера курса.
    """
    builder = InlineKeyboardBuilder()
    # Получаем данные для номеров курсов из TEXTS
    courses = TEXTS[lang].get('keyboard_courses', {})
    
    # Добавляем кнопки номеров курсов (1-6)
    for i in range(1, 7): # От 1 до 6
        course_key = str(i) # Ключ в словаре - строка
        if course_key in courses:
            builder.add(InlineKeyboardButton(text=courses[course_key], callback_data=f"course_{course_key}"))
            
    builder.adjust(3) # Располагаем кнопки в 3 столбца (по 2 в каждом ряду)
    return builder
