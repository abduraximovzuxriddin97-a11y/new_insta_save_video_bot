import asyncio, logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile, BotCommand, BotCommandScopeDefault
from aiogram.filters import Command

from utils import download_instagram_video


async def main_commands():
    commands = [
        BotCommand(command="start", description="Botni boshlash")
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())


dp = Dispatcher()
bot_token = "8505119931:AAEb4XDI-njdhPFMOml4mCX5P35zabyy78o"
bot = Bot(token=bot_token)

@dp.message(Command('start'))
async def start_cmd(message: Message):
    await message.reply("Salom, Ushbu botga instagramdan havola yuborib, uning videosini ajratib oling")

@dp.message(F.text.startswith("https://www.instagram.com/"))
async def download_video(message: Message):
    await message.answer("⏳")

    try:
        video = download_instagram_video(message.text)

        video_send = FSInputFile(video)
        await message.delete()
        await message.answer_video(video_send, caption="Ushbu video @backend_pythonbot orqali yukland")
        await message.answer_audio(video_send, caption="Ushbu video @backend_pythonbot orqali yukland")

        video.unlink()
    except:
        await message.answer("Video yuklashda xatolik buldi, qayta urining")


async def main():
    await main_commands()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
