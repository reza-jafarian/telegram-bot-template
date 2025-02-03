from telethon import events

from src.database.database import get_user, update_step
from src.utils.keyboards import start_key

async def init(bot):
    @bot.on(events.NewMessage(pattern=r'^([\/\#\!\.]start)$', func=lambda e: e.is_private))
    async def start(event):
        user = await event.get_sender()
        user_data = get_user(user_id=user.id)
        
        update_step(user_id=user.id, step='none')
        await event.reply('<b>👋 Hello</b>', buttons = start_key())