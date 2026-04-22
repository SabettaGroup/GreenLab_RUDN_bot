import sys
import asyncio
import logging
from config import settings
from handlers.common import router
from aiogram import Bot, Dispatcher
from handlers.registration import router_reg
from aiogram.fsm.storage.memory import MemoryStorage

# Специальный фикс для Windows, чтобы не было ошибки таймаута семафора
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

logging.basicConfig(level=logging.INFO)

async def main():
    # Используем .get_secret_value() для извлечения токена из SecretStr
    bot = Bot(token=settings.bot_token.get_secret_value())
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(router)
    dp.include_router(router_reg)
    logging.info("Starting bot...")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\n------------------\nБот приостановлен\n------------------\n')