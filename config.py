from os import getenv, mkdir, path

from aiogram import Bot
from dotenv import load_dotenv
from yadisk import Client


# Создание папок для хранения файлов
def makedirs() -> None:
    if not path.isdir('videos'):
        mkdir('videos')

    if not path.isdir('photos'):
        mkdir('photos')


load_dotenv()

admin = int(getenv('ADMIN'))  # Вставить telegram-id(не username, а id) админа, который сможет загружать файлы
bot = Bot(token=getenv('API_TG'))  # Вставить свой api-ключ бота
ydisk = Client(token=getenv('API_YA'))  # Вставить свой api-ключ от yandex.disk
