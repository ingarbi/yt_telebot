import telebot

bot = telebot.TeleBot("5855917656:AAE89D3EgAGyP29h7c9De8E5tOLG4rfdLZM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()