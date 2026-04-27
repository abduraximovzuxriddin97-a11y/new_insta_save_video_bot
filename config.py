import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.filters import Command

from dotenv import load_dotenv

load_dotenv()


BOT_API = os.getenv("API_TOKEN")
bot = Bot(token=BOT_API)
db = Dispatcher()


async def main_commands():
    commands = [
        BotCommand(command="start", description="Botni boshlash")
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
