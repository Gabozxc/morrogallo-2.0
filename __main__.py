import telebot
import config
from loader import register_handlers

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

register_handlers(bot)

if __name__ == '__main__':
    bot.infinity_polling()
