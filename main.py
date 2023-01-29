import telebot

bot = telebot.TeleBot("6009458088:AAHK_CBHNc6q5CMyrAmS2GhV20ZCl-k4yVA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, "Bot by Veshagurova Amina")
    if "crash" in message.text:
        g = 5/0
bot.infinity_polling() 