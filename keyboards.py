import telebot

start = telebot.types.InlineKeyboardMarkup()
url_button = telebot.types.InlineKeyboardButton(text="Проект на GitHub 🚀", url="https://github.com/MaynixX/PlainPhpFramework")
start.add(url_button)