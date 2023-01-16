import telebot
bot = telebot.TeleBot('5816188541:AAE5YW-IYn3xqbT3hcevX2AdnM0OpCMBWN4')
a ={"кот": "Рыжий", "небо": "Голубое", "мышь": "серая", "трава": "зеленая", "тополь": "высокий", "Привет": "круто"}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text in dict.keys(a):
        bot.send_message(message.from_user.id, a[message.text])
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)