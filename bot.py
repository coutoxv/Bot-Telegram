import telebot

TOKEN = "8630888437: AAENoVw2pbYxJkb3XZ5KFhPituAfd
JVluy4"

bot = telebot.TeleBot(TOKEN)

# ===== CONFIGURE SEUS PRODUTOS =====

produto1 = "Pack básico"
preco1 = "R$15"
desc1 = "Pack com apenas 5 fotos"

produto2 = "Pack mediano"
preco2 = "R$25"
desc2 = "Pack com 8 fotos + 2 videos"

produto3 = "Pack Premium"
preco3 = "R$45,90"
desc3 = "Pack com 10 fotos + 5 vídeos"

produto4 = "Pack Extreme"
preco4 = "R$59,90"
desc4 = "Pack com 20 fotos + 10 vídeos"

# ===================================

@bot.message_handler(commands=['start'])
def menu(message):

    bot.send_message(
        message.chat.id,
        "👋 Bem-vindo!\n\n"
        "Escolha um produto:\n"
        "1 - Produto 1\n"
        "2 - Produto 2\n"
        "3 - Produto 3\n"
        "4 - Produto 4\n"
        "\nDigite o número do produto."
    )

@bot.message_handler(func=lambda message: True)
def responder(message):

    texto = message.text

    if texto == "1":
        bot.send_message(message.chat.id,
            f"🛒 {produto1}\n💰 {preco1}\n📄 {desc1}\n\nDigite comprar para continuar.")

    elif texto == "2":
        bot.send_message(message.chat.id,
            f"🛒 {produto2}\n💰 {preco2}\n📄 {desc2}\n\nDigite comprar para continuar.")

    elif texto == "3":
        bot.send_message(message.chat.id,
            f"🛒 {produto3}\n💰 {preco3}\n📄 {desc3}\n\nDigite comprar para continuar.")

    elif texto == "4":
        bot.send_message(message.chat.id,
            f"🛒 {produto4}\n💰 {preco4}\n📄 {desc4}\n\nDigite comprar para continuar.")

    elif "comprar" in texto.lower():
        bot.send_message(message.chat.id,
            "✅ Fale com o vendedor para finalizar a compra.")

    else:
        bot.send_message(message.chat.id,
            "Digite um número de 1 a 4.")

bot.polling()
