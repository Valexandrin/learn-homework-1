"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import logging
import ephem
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    logger.info(text)
    update.message.reply_text(text)


def ask_planet_name(update, context):
    user_text = update.message.text.split()
    current_date = update.message.date
    logger.info(user_text)
    for word in user_text:        
        word = word.capitalize()        
        planet = getattr(ephem, word)
        if not planet:
            logger.info('Planet %s not found', word)
            return
        planet_info = planet(current_date)
        constellation = ephem.constellation(planet_info)
        update.message.reply_text(constellation)              


def talk_to_me(update, context):
    user_text = update.message.text
    logger.info(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", ask_planet_name))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
