import asyncio
import aiohttp

async def main():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.telegram.org') as resp:
                print(f"Статус подключения к TG: {resp.status}")
                print("Связь есть!")
    except Exception as e:
        print(f"Ошибка связи: {e}")

asyncio.run(main())
