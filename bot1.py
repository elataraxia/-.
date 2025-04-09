import telebot

bot = telebot.TeleBot('8069924388:AAGsaVVm1PEuRH0NkQcLECykX4AH5owWSno')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, 'привет бродяга')

@bot.message_handler(commands=['help', 'about'])
def help_command(message):
    bot.reply_to(message, 'че каво чем помочь')

@bot.message_handler(content_types=['text'])
def text_message_handler(message): 
    response = f"ты написал: {message.text}"
    bot.send_message(message.chat.id, response)

bot.polling()
