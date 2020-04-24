import telebot
import pyowm

bot = telebot.TeleBot('1051699427:AAEoQsFotygwjyhCp7r3R0jpkZBqu6pEAjY', language = "ru")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    msg = bot.reply_to(message, "Введите город")

    bot.register_next_step_handler(msg, process_place_step)

def process_place_step(message):
    place = message.text
    owm = pyowm.OWM('ef10360ae36e154345f37afd1f0ce884', language = "ru")
    observation = owm.weather_at_place(place)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    bot.reply_to(message , "В городе "+ place + " сейчас " + w.get_detailed_status() + ", температура " + str(temp) + " градусов по цельсию")

if __name__ == '__main__':
     bot.polling(none_stop=True)
