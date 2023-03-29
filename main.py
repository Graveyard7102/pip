import telebot
import pyautogui as pg
import keyboard

keyboard.press_and_release('shift+s, space')

bot = telebot.TeleBot('5816188541:AAE5YW-IYn3xqbT3hcevX2AdnM0OpCMBWN4')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/off":
        pg.leftClick(24, 1056, duration=0.3)
        pg.leftClick(19, 1008, duration=0.5)
        pg.doubleClick(26, 926, duration=1)
    elif message.text == "/gamepad":
        keyboard.press_and_release('win+i')
        pg.leftClick(656, 362, duration=0.9)
        pg.leftClick(710, 429, duration=0.5)
        pg.leftClick(674, 495, duration=0.5)
        pg.leftClick(785, 446, duration=0.5)
        pg.doubleClick(478, 133,duration=7)
        pg.leftClick(756, 335, duration=1)
        pg.leftClick(800, 366, duration=7)
        pg.leftClick(1135, 773, duration=7)
        pg.leftClick(1330, 39, duration=0.5)
        pg.leftClick(1894, 14, duration=0.5)
    elif message.text == "/gamepadbrowser":
        pg.leftClick(1626, 107, duration=0.5)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Вот список моих команд:\n/off - Выключить комппьютер\n/gamepad - подключить геймпад\n/gamepadbrowser - закрыть браузер после отключения геймпада")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Вот список моих команд:\n/off - Выключить комппьютер0\n/gamepad - подключить геймпад\n/gamepadbrowser - закрыть браузер после отключения геймпада")
bot.polling(none_stop=True, interval=0)