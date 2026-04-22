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

@router.callback_query(LanguageState.waiting_for_language)
async def select_language(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    # 1. Получаем код языка из callback_data (например, 'ru' или 'en')
    selected_lang = callback.data 
    # Проверяем, что такой язык вообще есть в нашем словаре (на всякий случай)
    if selected_lang not in TEXTS:
        selected_lang = 'ru' # Дефолт, если что-то пошло не так
    # 2. Сохраняем выбор в FSM. Это позволит другим хендлерам узнать язык пользователя.
    await state.update_data(language=selected_lang)
    # 3. Теперь достаем тексты.selected_lang тут уже определена и не будет красной.
    welcome_text = TEXTS[selected_lang]['welcome_message']
    # Передаем язык в функцию создания клавиатуры (она должна его принимать)
    reply_markup = get_join_nso_keyboard(selected_lang) # Убираем инлайн-кнопки выбора языка

    # 4. Редактируем старое сообщение или отправляем новое
    if callback.message:
        await callback.message.answer(
        text=welcome_text,
        reply_markup=reply_markup
    )
    # Убираем часики на кнопке
    await callback.answer()
    























