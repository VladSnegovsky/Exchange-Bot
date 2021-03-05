from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Languages
def languages():
    button_English = InlineKeyboardButton(text="English 🇬🇧", callback_data="change to english")
    button_Russian = InlineKeyboardButton(text="Русский 🇷🇺", callback_data="change to russian")
    languages = InlineKeyboardMarkup()
    return languages.add(button_English).add(button_Russian)