import asyncio, logging

from aiogram import F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from utils import download_instagram_video
from config import main_commands, db, bot


@db.message(Command('start'))
async def start_cmd(message: Message):
    await message.reply("Salom, Ushbu botga instagramdan havola yuborib, uning videosini ajratib oling")

@db.message(F.text.startswith("https://www.instagram.com/"))
async def download_video(message: Message):
    load_msg = await message.answer("⏳")

    try:
        video = download_instagram_video(message.text)

        video_send = FSInputFile(video)
        await load_msg.delete()
        await message.answer_video(video_send, caption="Ushbu video @backend_pythonbot orqali yukland")
        await message.answer_audio(video_send, caption="Ushbu video @backend_pythonbot orqali yukland")

        video.unlink()
    except:
        await message.answer("Video yuklashda xatolik buldi, qayta urining")


async def main():
    await main_commands()
    await db.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
