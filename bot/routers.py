from datetime import datetime

from yadisk.exceptions import PathExistsError
from aiogram import Router, F
from aiogram.types import Message
from config import bot, ydisk, admin

router = Router()


@router.message(F.photo)
async def collect_photo(message: Message):
    if message.from_user.id == admin:  # Проверка пользователя
        await bot.download(message.photo[-1], destination=fr"photos\{message.photo[-1].file_id}.jpg")  # Скачиваем файл
        try:
            ydisk.upload(fr"photos\{message.photo[-1].file_id}.jpg",
                         f"{message.photo[-1].file_id}.jpg")  # Загружаем на диск
        except PathExistsError:
            ydisk.upload(fr"photos\{message.photo[-1].file_id}.jpg",
                         # Если файл загружается повторно, то загружаем с пометкой в имени - датой и временем
                         f"{message.photo[-1].file_id}({datetime.now()}).jpg")
    else:
        await message.answer("Вы не имеете доступа")


@router.message(F.video)
async def collect_video(message: Message):
    if message.from_user.id == admin:
        await bot.download(message.video, destination=fr"videos\{message.video.file_id}.mp4")
        try:
            ydisk.upload(fr"videos\{message.video.file_id}.mp4",
                         f"{message.video.file_id}.mp4")
        except PathExistsError:
            ydisk.upload(fr"videos\{message.video.file_id}.mp4",
                         f"{message.video.file_id}({datetime.now()}).mp4")
    else:
        await message.answer("Вы не имеете доступа")
