from ChatGpt import ChatGpt
import telebot
import keyboards
import texts
import env

chat = ChatGpt(env.gpt_token)
bot = telebot.TeleBot(env.tgbot_token)


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(
        message.chat.id,
        texts.start,
        reply_markup=keyboards.start
    )

@bot.message_handler()
def answer(message):
    message_id = bot.send_message(
        message.chat.id,
        "Обработка сообщения, ожидайте..."
    ).message_id
    username = message.from_user.username
    ans = chat.ask(message.text, username)
    bot.delete_message(message.chat.id, message_id)
    bot.send_message(
        message.chat.id,
        ans
    )
bot.polling(none_stop=True)