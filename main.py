import asyncio
import logging
from config import settings
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
#from handlers import common

logging.basicConfig(level=logging.INFO)

async def main():
    # Используем .get_secret_value() для извлечения токена из SecretStr
    bot = Bot(token=settings.bot_token.get_secret_value())
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    # TODO: Зарегистрировать роутеры хендлеров
    logging.info("Starting bot...")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\n------------------\nБот приостановлен\n------------------\n')