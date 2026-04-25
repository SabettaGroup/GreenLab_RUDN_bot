import asyncio
from text import TEXTS
from config import settings
from aiogram.filters import Command
from DataBase.users import get_all_users
from aiogram import Router, types, F, Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from Fsm.admin_state import AdminNewsletter

# роутер для админских команд
admin_router = Router()

ADMIN_LANG = 'ru'

async def send_newsletter_task(bot: Bot, user_id: int, from_chat_id: int, message_id: int, state_manager: FSMContext, dp: Dispatcher):
    # проверяем состояние пользователя
    state_context = dp.fsm.get_context(bot, user_id, user_id)
    current_state = await state_context.get_state()

    if current_state is not None:
        # Если юзер в FSM (занят), ждем 30 минут (1800 сек)
        print(f'пользователь {user_id} занят, ждем 30 минут')
        await asyncio.sleep(18000)
        # После паузы проверяем еще раз (вдруг он всё еще занят)
    try:
        await bot.copy_message(
            chat_id=user_id,
            from_chat_id=from_chat_id,
            message_id=message_id
    )
        print(f"Сообщение успешно отправлено юзеру {user_id}")
    except Exception as e:
        print(f"Не удалось отправить пользователю {user_id}: {e}")

# команда запуска рассылки
@admin_router.message(Command('send_a_newsletter'), F.from_user.id == settings.admin_id)
async def start_newsletter(message: types.Message, state: FSMContext):
    await message.answer("Напишите сообщение или перешлите пост, который придёт всем пользователям бота.")
    await state.set_state(AdminNewsletter.waiting_for_message)

# Прием сообщения для рассылки
@admin_router.message(AdminNewsletter.waiting_for_message, F.from_user.id == settings.admin_id)
async def process_newsletter(message: types.Message, state: FSMContext, bot: Bot, dp):
    users = get_all_users()
    admin_id = settings.admin_id
    
    count = 0
    for user_id in users:
        if user_id == admin_id:
            continue
            
        # Запускаем фоновую задачу для каждого юзера
        # Мы передаем dp.fsm, чтобы внутри задачи проверить состояние
        asyncio.create_task(
            send_newsletter_task(bot, user_id, message.chat.id, message.message_id, AdminNewsletter.waiting_for_message, dp=dp)
        )
        count += 1

    await message.answer(f"Рассылка запущена для {count} пользователей.\nТе, кто сейчас заполняют анкету, получат её через 30 минут.")
    await state.clear()

# --- Пример админской команды: Получить информацию о пользователе ---
# Это может быть полезно, чтобы по ID пользователя найти его анкету в будущем,
# если ты будем сохранять их в БД. Пока это заглушка.
@admin_router.message(F.text.startswith("/user_info"), F.from_user.id == settings.admin_id)
async def admin_user_info(message: types.Message, bot: Bot):
    # Разбираем команду. Например, админ пишет: /user_info 123456789
    parts = message.text.split()
    if len(parts) == 2 and parts[1].isdigit():
        user_id_to_find = int(parts[1])
        # Здесь в будущем можно будет искать анкету этого user_id в базе данных
        response_text = f"⚙️ Запрос информации по пользователю ID: {user_id_to_find}\n"
        response_text += "Функция поиска в базе данных пока не реализована."
    else:
        response_text = "⚙️ Неверный формат команды. Используйте: /user_info <ID пользователя>"
        
    await message.answer(response_text)


# --- Пример админской команды: Получить статистику бота ---
# Статистика (сколько пользователей, сколько анкет и т.д.)
# Пока это заглушка, но потом здесь можно будет делать запросы к БД
# @admin_router.message(F.text == "/stats", F.from_user.id == settings.admin_id)
# async def admin_show_stats(message: types.Message, bot: Bot):
#     # Здесь можно получать данные из базы:
#     # total_users = await db.get_total_users() # Пример
#     # total_applications = await db.get_total_applications() # Пример
    
#     response_text = f"📊 **Статистика бота:**\n"
#     response_text += f"👥 Общее количество пользователей: [Будет из БД]\n"
#     response_text += f"📝 Количество заполненных анкет: [Будет из БД]\n"
#     response_text += f"🤖 Бот активен: Да (uptime)\n"
    
#     await message.answer(response_text, parse_mode="HTML")

# --- Другие админские команды по необходимости ---
# Например, для перезагрузки бота (в будущем, не сейчас) или для отправки рассылки.

# Админский роутер не должен обрабатывать ничего, кроме своих команд,
# поэтому здесь нет хендлеров без фильтров.
