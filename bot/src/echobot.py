from aiogram import Bot, Dispatcher, types
from bot.src.settings import config
from datetime import datetime
from zoneinfo import ZoneInfo
from bot.src.database.create_table import execute_query

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    timestamp_now = datetime.now(tz=ZoneInfo('UTC')).isoformat(' ')
    inser_query = (
        f"INSERT INTO message (message_text, user_id, message_time, username) "
           f"VALUES ('{message.text}',{message.from_user['id']},'{timestamp_now}', '{message.from_user['first_name']} {message.from_user['last_name']}')"
    )
    execute_query(inser_query)
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    #!!!!!!
    # написати функцію, для запису повідомлення в БД
    timestamp_now = datetime.now(tz=ZoneInfo('UTC')).isoformat(' ')
    inser_query = (
        f"INSERT INTO message (message_text, user_id, message_time, username) "
        f"VALUES ('{message.text}',{message.from_user['id']},'{timestamp_now}', '{message.from_user['first_name']} {message.from_user['last_name']}')"
    )
    execute_query(inser_query)
    await message.answer(message.text)
