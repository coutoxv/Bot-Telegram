import telebot

TOKEN = "8630888437: AAENoVw2pbYxJkb3XZ5KFhPituAfd
JVluy4"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Olá! Digite 1 para ver produto.")

@bot.message_handler(func=lambda message: True)
def responder(message):

    if message.text == "1":
        bot.reply_to(message, "RX580 8GB para conserto - R$350")

    elif "comprar" in message.text.lower():
        bot.reply_to(message, "Acesse o anúncio para comprar.")

bot.polling()
