import Keyboards as keyboard


async def main_menu(bot, message, language, name):
    """Changes Main Message to <Main Menu>"""
    await bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                                text=language.mainMessage(name))


async def delete_message(bot, message):
    """Deletes Message"""
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


async def send_text_message(bot, message, text):
    """Sends text Message"""
    return await bot.send_message(chat_id=message.chat.id, text=text)

async def send_image_message(bot, message, text):
    """Sends image Message"""
    return await bot.send_photo(chat_id=message.chat.id, photo=open("temp.png", "rb"), caption=text)