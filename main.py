import telebot

bot = telebot.TeleBot("5855917656:AAE89D3EgAGyP29h7c9De8E5tOLG4rfdLZM")


items_catalog = [
    {
        "name": "iphone",
        "price": 1000,
        "currency": "USD",
        "description": "this is iphone 15",
        "photo": "https://img.freepik.com/free-psd/smartphone-mock-up-isolated_1310-1576.jpg?w=1380&t=st=1682150565~exp=1682151165~hmac=c44ad261254e6ee0e4a95ad6b662b46f631a45f8f1dabe0054899181d9eaad3c",
    }
]


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет %s! \n\nWelcome to Our MyShop! \n Here u can but anything! \n/catalog - get the update-to-date catalog"
        % message.from_user.first_name,
    )


@bot.message_handler(commands=["catalog"])
def send_catalog(message):
    bot.send_message(message.chat.id, "This is %s" % items_catalog[0]['name'])
    bot.send_photo(message.chat.id, photo=items_catalog[0]["photo"])


bot.infinity_polling()
