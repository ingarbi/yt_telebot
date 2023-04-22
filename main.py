import telebot

bot = telebot.TeleBot("5855917656:AAE89D3EgAGyP29h7c9De8E5tOLG4rfdLZM")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет %s" % message.from_user.first_name)


bot.infinity_polling()
