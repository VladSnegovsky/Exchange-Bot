# =================== Files
from aiogram import Bot, Dispatcher, executor, types
import telegram
import logging
import asyncio
import time


# =================== My Files
import Config
import Keyboards as keyboard
import Messages as msg
import Languages.English as english
import Languages.Russian as russian
import Timer as timer
import Functions as function
import Requests as request
import Graph as graph
import DataBase as database


# =================== Initialize Bot
logging.basicConfig(level=logging.INFO)
bot = Bot(token=Config.TG_BOT_API_TOKEN)
dp = Dispatcher(bot)


# =================== Constants
language = english


# =================== Handlers
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Please, select language 🇬🇧\n"
                         "Пожалуйста, выбери язык 🇷🇺\n",
                         reply_markup = keyboard.languages())
    if not database.user_exists(message.from_user.id):
        database.add_user(message.from_user.id)
    await msg.delete_message(bot, message)

@dp.message_handler(commands=['historyCAD'])
async def process_start_command(message: types.Message):
    request.get_history("CAD")
    newMessage = await msg.send_image_message(bot, message, language.dictionary["Here is the history for the last 7 days.\n(will expire in 10 min)"] + "[CAD]")
    messageTimer = timer.Timer(bot, newMessage, 10)
    function.start_timer(messageTimer)
    await msg.delete_message(bot, message)

@dp.message_handler(commands=['historyCZK'])
async def process_start_command(message: types.Message):
    request.get_history("CZK")
    newMessage = await msg.send_image_message(bot, message, language.dictionary["Here is the history for the last 7 days.\n(will expire in 10 min)"] + "[CZK]")
    messageTimer = timer.Timer(bot, newMessage, 10)
    function.start_timer(messageTimer)
    await msg.delete_message(bot, message)\

@dp.message_handler(commands=['historyGBP'])
async def process_start_command(message: types.Message):
    request.get_history("GBP")
    newMessage = await msg.send_image_message(bot, message, language.dictionary["Here is the history for the last 7 days.\n(will expire in 10 min)"] + "[GBP]")
    messageTimer = timer.Timer(bot, newMessage, 10)
    function.start_timer(messageTimer)
    await msg.delete_message(bot, message)

@dp.message_handler(commands=['exchangecad'])
async def process_start_command(message: types.Message):
    answer = request.convert_to("CAD")
    newMessage = await msg.send_text_message(bot, message, language.dictionary["Exchange"] + answer)
    messageTimer = timer.Timer(bot, newMessage, 10)
    function.start_timer(messageTimer)
    await msg.delete_message(bot, message)

@dp.message_handler(commands=['exchangegbp'])
async def process_start_command(message: types.Message):
    answer = request.convert_to("GBP")
    newMessage = await msg.send_text_message(bot, message, language.dictionary["Exchange"] + answer)
    messageTimer = timer.Timer(bot, newMessage, 10)
    function.start_timer(messageTimer)
    await msg.delete_message(bot, message)

@dp.message_handler(commands=['exchangeczk'])
async def process_start_command(message: types.Message):
    answer = request.convert_to("CZK")
    newMessage = await msg.send_text_message(bot, message, language.dictionary["Exchange"] + answer)
    messageTimer = timer.Timer(bot, newMessage, 10)
    function.start_timer(messageTimer)
    await msg.delete_message(bot, message)

@dp.message_handler(commands=['list'])
async def process_start_command(message: types.Message):
    lastTime = database.get_time(message.from_user.id)
    now = time.time()
    if (function.compare_time(lastTime, now)):
        info = request.get_all_rates()
        newMessage = await msg.send_text_message(bot, message, language.dictionary["Here is all rates for now: "] + "\n" + info + "\n(will expire in 10 min)")
        messageTimer = timer.Timer(bot, newMessage, 10)
        function.start_timer(messageTimer)
        database.update_info(message.from_user.id, int(now), info)
    else:
        newMessage = await msg.send_text_message(bot, message, language.dictionary["Here is all rates for now: "] + "\n" + str(database.get_info(message.from_user.id)[0][0]) + "\n(will expire in 10 min)")
        messageTimer = timer.Timer(bot, newMessage, 10)
        function.start_timer(messageTimer)
    await msg.delete_message(bot, message)

@dp.callback_query_handler(lambda message: True)
async def ans(message):
    global language

    # ========================================== Change Language ==============
    if message.data == "change to english":
        language = english
        await msg.main_menu(bot, message, language, message.from_user.first_name)
    elif message.data == "change to russian":
        language = russian
        await msg.main_menu(bot, message, language, message.from_user.first_name)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

