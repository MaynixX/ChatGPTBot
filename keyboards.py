import telebot

start = telebot.types.InlineKeyboardMarkup()
url_button = telebot.types.InlineKeyboardButton(text="Проект на GitHub 🚀", url="https://github.com/MaynixX/ChatGPTBot")
start.add(url_button)