from aiogram import Router, types, F, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder # Импортируем для клавиатур

from keyboards.inlinek import get_language_keyboard # Для кнопок языков импортируем соответ. инлайн-клаву 
from keyboards.replyk import get_join_nso_keyboard # Для кнопки "Вступить в НСО"
from Fsm.language import LanguageState # Наш FSM класс для языка
from text import TEXTS # Наш словарь текстов

# Создаем роутер для общих хендлеров
router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext, bot: Bot):
    """
    Обрабатывает команду /start.
    Предлагает пользователю выбрать язык.
    """
    # Устанавливаем состояние фсм для ожидания выбора языка
    await state.set_state(LanguageState.waiting_for_language)

    # Отправляем сообщение с выбором языка
    await message.answer(
        TEXTS['ru']['welcome_message_lang'], # "Выберите язык / Select a language"
        reply_markup=get_language_keyboard() # Инлайн-клава с языками
    )

@router.callback_query(LanguageState.waiting_for_language, F.data.in_(['ru', 'en', 'fr']))
async def select_language(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    """
    Обрабатывает выбор языка пользователем.
    Сохраняет язык в FSM, отправляет приветствие и Reply-клавиатуру.
    """
    selected_lang = callback.data # Получаем код языка ('ru', 'en', 'fr') из callback_data
    
    # Сохраняем выбранный язык в FSM контекст пользователя
    await state.update_data(language=selected_lang)
    
    # Получаем тексты на выбранном языке
    welcome_message_text = TEXTS[selected_lang]['welcome_message'] # Текст "Здравствуйте! ..."
    join_nso_keyboard_markup = get_join_nso_keyboard(selected_lang) # Reply-клавиатура с кнопкой "Вступить в НСО"

    # Редактируем предыдущее сообщение (с выбором языка)
    # Отправляем НОВОЕ сообщение с приветствием и Reply-клавиатурой
    await callback.message.answer(
        welcome_message_text,
        reply_markup=join_nso_keyboard_markup # Теперь это Reply-клавиатура!
    )
    
    # Завершаем состояние выбора языка
    await state.clear() 

    # Отвечаем на callback_query, чтобы убрать индикатор загрузки на кнопке
    await callback.answer(text=TEXTS[selected_lang]['language_selected_notification'])