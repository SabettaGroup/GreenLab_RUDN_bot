from text import TEXTS
from config import settings
from datetime import datetime
from DataBase.users import add_user
from Fsm.language import LanguageState
from aiogram.filters import CommandStart
from aiogram import Router, types, Bot, F
from aiogram.fsm.context import FSMContext
from Fsm.becoming_member import MemberState
from keyboards.replyk import get_join_nso_keyboard 
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder 
from keyboards.inlinek import get_language_keyboard, get_departments_keyboard, get_organizer_keyboard, get_dept_action_keyboard

# Создаем роутер для общих хендлеров
router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext, bot: Bot):
    """
    Обрабатывает команду /start.
    Предлагает пользователю выбрать язык. Схраняет ID пользователя в базу данных.
    """
    add_user(message.from_user.id) # СОХРАНЯЕМ ЮЗЕРА
    
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

    if callback.message:
        await callback.message.delete()
    # 4. Редактируем старое сообщение или отправляем новое
    if callback.message:
        await callback.message.answer(
        text=welcome_text,
        reply_markup=reply_markup
    )
    await state.set_state(None) 
    # Убираем часики на кнопке
    await callback.answer()

@router.callback_query(MemberState.choosing_department, F.data.startswith("dept_"))
async def show_dept_info(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    dept_key = callback.data.split("_")[1]
    
    # Показываем описание отдела и кнопки "Выбрать" / "Назад"
    await callback.message.edit_text(
        text=TEXTS[lang][f'department_description_{dept_key}'],
        reply_markup=get_dept_action_keyboard(lang, dept_key)
    )

@router.callback_query(MemberState.choosing_department, F.data == "back_to_depts")
async def back_to_depts(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    await callback.message.edit_text(TEXTS[lang]['choose_dept_message'], reply_markup=get_departments_keyboard(lang))

# Кнопка "Выбрать отдел" (ФИНАЛ)
@router.callback_query(MemberState.choosing_department, F.data.startswith("confirm_dept_"))
async def confirm_dept(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    # ПРОВЕРКА
    if data.get('already_sent_final_request'):
        await callback.answer(TEXTS[lang]['already_applied'], show_alert=True) # Показываем уведомление
        return
    
    dept_key = callback.data.split("_")[2]
    dept_name = TEXTS[lang]['keyboard_departments'][dept_key]
    # 1. Меняем текст пользователю
    await callback.message.edit_text(TEXTS[lang]['thanks_dept'])
    # 2. Уведомляем админа
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    user_data = await state.get_data() 
    user_contacts = data.get('contacts', 'Не указаны')
    admin_msg = (
        f"🔔 **НОВАЯ ЗАЯВКА: ОРГАНИЗАТОР**\n"
        f"🆔 ID: `{callback.from_user.id}`\n"
        f"📅 Дата: {now}\n"
        f"🏢 Отдел: {dept_name}\n"
        f"Контакты: {user_contacts}"
    )
    await bot.send_message(settings.admin_id, admin_msg, parse_mode="HTML")
    await state.update_data(already_sent_final_request=True)
    await callback.message.edit_text(TEXTS[lang]['thanks_dept'])
    await state.set_state(None)

# Новый хендлер для кнопки "Стать организатором"
@router.message(F.text.in_([
    TEXTS['ru']['keyboard_reply_buttons']['become_an_org'],
    TEXTS['en']['keyboard_reply_buttons']['become_an_org'],
    TEXTS['fr']['keyboard_reply_buttons']['become_an_org']
]))
async def process_become_org(message: types.Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    
    # Проверка на повторную заявку (оставляем)
    if data.get('already_sent_final_request'):
        await message.answer(TEXTS[lang]['already_applied'])
        return

    # СРАЗУ отправляем выбор отделов (как раньше было у участников)
    await message.answer(
        TEXTS[lang]['choose_dept_message'], 
        reply_markup=get_departments_keyboard(lang)
    )
    # Используем состояние 
    await state.set_state(MemberState.choosing_department)

# Кнопка "Стать организатором"
@router.callback_query(F.data == "confirm_org")
async def confirm_org(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    # проверка
    if data.get('already_sent_final_request'):
        await callback.answer(TEXTS[lang]['already_applied'], show_alert=True)
        return
    
    await callback.message.edit_text(TEXTS[lang]['thanks_org'])
    user_data = await state.get_data() 
    user_contacts = data.get('contacts', 'Не указаны')
    # Уведомляем админа
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    admin_msg = (
        f"🔥 **НОВАЯ ЗАЯВКА: ОРГАНИЗАТОР**\n"
        f"🆔 ID: `{callback.from_user.id}`\n"
        f"📅 Дата: {now}\n"
        f"Контакты: {user_contacts}"
    )
    await bot.send_message(settings.admin_id, admin_msg, parse_mode="HTML")
    await state.update_data(already_sent_final_request=True)
    await callback.message.edit_text(TEXTS[lang]['thanks_org'])
    await state.set_state(None)

# Кнопка "Назад" для организатора (к сообщению благодарности)
@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    # Просто удаляем инлайн-сообщение, так как реплай-клава и так на месте
    await callback.message.delete()
























