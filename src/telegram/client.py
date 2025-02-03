from telethon import TelegramClient

from src.config.config import settings

bot = TelegramClient(
    session=settings.SESSION_NAME,
    api_id=settings.API_ID,
    api_hash=settings.API_HASH
)

async def startClient():
    await bot.start(bot_token=settings.BOT_TOKEN)

async def stopClient():
    await bot.disconnect()

async def getClient():
    return bot