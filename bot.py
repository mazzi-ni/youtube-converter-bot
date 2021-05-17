import telebot
import converter

global url
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "hello boyzzz ")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    title = converter.converter(message.text);
    # sendAudio
    chat_id = message.chat.id
    audio = open('./'+ title +'.mp3', 'rb');
    bot.send_audio(chat_id, audio);
    bot.send_audio(chat_id, "FILEID");

bot.polling()
