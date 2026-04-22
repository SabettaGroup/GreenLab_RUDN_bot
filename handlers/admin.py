from text import TEXTS
from config import settings
from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext
from handlers.registration import router_reg 

# роутер для админских команд
admin_router = Router()

ADMIN_LANG = 'ru'

# --- Пример админской команды: Получить информацию о пользователе ---
# Это может быть полезно, чтобы по ID пользователя найти его анкету в будущем,
# если ты будем сохранять их в БД. Пока это заглушка.
@admin_router.message(F.text.startswith("/user_info"), F.from_user.id == int(settings.admin_chat_id.get_secret_value()))
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
@admin_router.message(F.text == "/stats", F.from_user.id == int(settings.admin_chat_id.get_secret_value()))
async def admin_show_stats(message: types.Message, bot: Bot):
    # Здесь можно получать данные из базы:
    # total_users = await db.get_total_users() # Пример
    # total_applications = await db.get_total_applications() # Пример
    
    response_text = f"📊 **Статистика бота:**\n"
    response_text += f"👥 Общее количество пользователей: [Будет из БД]\n"
    response_text += f"📝 Количество заполненных анкет: [Будет из БД]\n"
    response_text += f"🤖 Бот активен: Да (uptime)\n"
    
    await message.answer(response_text, parse_mode="Markdown")

# --- Другие админские команды по необходимости ---
# Например, для перезагрузки бота (в будущем, не сейчас) или для отправки рассылки.

# Админский роутер не должен обрабатывать ничего, кроме своих команд,
# поэтому здесь нет хендлеров без фильтров.
