from text import TEXTS
from config import settings
from datetime import datetime
from DataBase.users import get_reg_count
from aiogram import Router, types, Bot, F
from aiogram.fsm.context import FSMContext
from DataBase.users import increment_reg_count
from Fsm.registration import RegistrationState
from keyboards.replyk import get_final_keyboard
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.inlinek import get_course_level_keyboard, get_course_number_keyboard


router_reg = Router() #роутер для регистрации

@router_reg.message(F.text.in_([
    TEXTS['ru']['keyboard_reply_buttons']['join_nso_button'],
    TEXTS['en']['keyboard_reply_buttons']['join_nso_button'],
    TEXTS['fr']['keyboard_reply_buttons']['join_nso_button'],
])) # 1. Начинаем
async def start_survey(message: types.Message, state: FSMContext):
    # проверка на кол-во регистраций
    data = await state.get_data()
    lang = data.get('language', 'ru')
    user_id = message.from_user.id
    count = get_reg_count(user_id)
    if count >= 2:
        await message.answer(TEXTS[lang]['too_many_registrations'])
        return

    # Если всё ок, начинаем опрос
    await message.answer(TEXTS[lang]['registration_prompt_fio'])
    await state.set_state(RegistrationState.fio)

# 2. Ловим ФИО -> Спрашиваем Факультет
@router_reg.message(RegistrationState.fio)
async def process_fio(message: types.Message, state: FSMContext):
    await state.update_data(fio=message.text) # Сохраняем ФИО
    data = await state.get_data()
    lang = data.get('language', 'ru')
    await message.answer(TEXTS[lang]['registration_prompt_faculty'])
    await state.set_state(RegistrationState.faculty)

# 3. Ловим Факультет -> Спрашиваем Уровень образования (Инлайн кнопки)
@router_reg.message(RegistrationState.faculty)
async def process_faculty(message: types.Message, state: FSMContext):
    await state.update_data(faculty=message.text) # Сохраняем Факультет
    data = await state.get_data()
    lang = data.get('language', 'ru')
    await message.answer(
        TEXTS[lang]['registration_prompt_course_level'],
        reply_markup=get_course_level_keyboard(lang).as_markup()
    )
    await state.set_state(RegistrationState.course_level)

# 4. Ловим выбор уровня (бакалавриат и т.д.) -> Спрашиваем номер курса
@router_reg.callback_query(RegistrationState.course_level, F.data.startswith("level_"))
async def process_course_level(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    level_key = callback.data.split("_")[1] # Извлекаем 'bachelor', 'master' или 'phd'
    await state.update_data(course_level=TEXTS[lang]['keyboard_levels'][level_key]) # Сохраняем уровень образования (текстом)
    await callback.message.delete() # не засоряем чат - удаляем сообщение
    await callback.message.answer(
        TEXTS[lang]['registration_prompt_course_number'],
        reply_markup=get_course_number_keyboard(lang).as_markup()
    )
    await state.set_state(RegistrationState.course_number)
    await callback.answer()

# 5. Ловим выбор номера курса -> Спрашиваем про опыт
@router_reg.callback_query(RegistrationState.course_number, F.data.startswith("course_"))
async def process_course_number(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language', 'ru')
    course_num = callback.data.split("_")[1] # Извлекаем '1', '2', '3' и т.д.
    await state.update_data(course_number=TEXTS[lang]['keyboard_courses'][course_num]) # Сохраняем номер курса (текстом)
    await callback.message.delete()
    await callback.message.answer(TEXTS[lang]['registration_prompt_experience'])
    await state.set_state(RegistrationState.experience)
    await callback.answer()

# 6. Ловим опыт -> Спрашиваем про интересы
@router_reg.message(RegistrationState.experience)
async def process_experience(message: types.Message, state: FSMContext):
    await state.update_data(experience=message.text) # Сохраняем опыт
    data = await state.get_data()
    lang = data.get('language', 'ru')
    await message.answer(TEXTS[lang]['registration_prompt_interests'])
    await state.set_state(RegistrationState.interests)

# 6. Ловим интересы -> Спрашиваем КОНТАКТЫ 
@router_reg.message(RegistrationState.interests)
async def process_interests(message: types.Message, state: FSMContext):
    await state.update_data(interests=message.text)
    data = await state.get_data()
    lang = data.get('language', 'ru')
    # Теперь спрашиваем контакты
    await message.answer(TEXTS[lang]['registration_prompt_contacts'])
    await state.set_state(RegistrationState.contacts)

# 7. ФИНАЛЬНЫЙ ШАГ: ловим контакты, собираем всё и отправляем админу
@router_reg.message(RegistrationState.contacts)
async def process_contacts_and_finish(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(contacts=message.text)
    full_user_data = await state.get_data()
    lang = full_user_data.get('language', 'ru')
    user_id = message.from_user.id
    now = datetime.now().strftime("%d.%m.%Y %H:%M")

    # 3. анкета админа
    admin_message = (
        f"✅ **НОВАЯ АНКЕТА ПОЛЬЗОВАТЕЛЯ**\n\n"
        f"🆔 **ID:** `{user_id}`\n"
        f"📅 **Дата:** {now}\n"
        f"🌐 **Язык:** {lang.upper()}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 **ФИО:** {full_user_data.get('fio', 'N/A')}\n"
        f"🎓 **Факультет:** {full_user_data.get('faculty', 'N/A')}\n"
        f"📚 **Уровень:** {full_user_data.get('course_level', 'N/A')}\n"
        f"🔢 **Курс:** {full_user_data.get('course_number', 'N/A')}\n"
        f"💡 **Опыт:** {full_user_data.get('experience', 'N/A')}\n"
        f"🚀 **Интересы:** {full_user_data.get('interests', 'N/A')}\n"
        f"📞 **КОНТАКТЫ:** {full_user_data.get('contacts', 'N/A')}\n"
    )
    
    # --- ОТПРАВКА АДМИНУ ---
    # Достаем ID из настроек
    admin_chat_id = settings.admin_id 
    
    try:
        # Отправляем именно админу в чат
        await bot.send_message(
            chat_id=admin_chat_id, 
            text=admin_message, 
            parse_mode="HTML"
        )
    except Exception as e:
        print(f"Ошибка отправки админу: {e}")

    # --- ОТВЕТ ПОЛЬЗОВАТЕЛЮ ---
    from keyboards.replyk import get_final_keyboard
    user_final_message = TEXTS[lang]['application_created'] 
    final_keyboard = get_final_keyboard(lang)
    await message.answer(
        text=user_final_message,
        reply_markup=final_keyboard
    )
    # УВЕЛИЧИВАЕМ СЧЕТЧИК В БАЗЕ
    increment_reg_count(message.from_user.id)
    # --- Завершаем анкету ---
    # Ставим метку, что пользователь прошел регистрацию
    # await state.update_data(is_registered=True) 
    # await message.answer(
    #     text=TEXTS[lang]['application_created'],
    #     reply_markup=get_final_keyboard(lang)
    # )
    await state.set_state(None) # НЕ используем .clear(), чтобы флаг выжил!