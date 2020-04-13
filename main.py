# from telegram.ext import Updater, InlineQueryHandler, CommandHandler
# import requests
# import re

# contents = requests.get('https://random.dog/woof.json').json()


# def get_url():
#     contents = requests.get('https://random.dog/woof.json').json()    
#     url = contents['url']
#     return url


# def bop(bot, update):
#     # get image url
#     url = get_url()
#     # get recipient's id
#     chat_id = update.message.chat_id
#     # send photo to recipient
#     bot.send_photo(chat_id=chat_id, photo=url)

# def main():
#     updater = Updater('1137170938:AAGbOrkFpLg_y2YSyONY0DLUye-e5p0TPzc', use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler('bop',bop))
#     updater.start_polling()
#     updater.idle()
    
# if __name__ == '__main__':
#     main()

# from telegram.ext import Updater, InlineQueryHandler, CommandHandler
# from telegram.ext.dispatcher import run_async
# import requests
# import re

# def get_url():
#     contents = requests.get('https://random.dog/woof.json').json()    
#     url = contents['url']
#     return url

# def bop(bot, update):
#     url = get_url()
#     chat_id = update.message.chat_id
#     bot.send_photo(chat_id=chat_id, photo=url)

# def main():
#     updater = Updater('1137170938:AAGbOrkFpLg_y2YSyONY0DLUye-e5p0TPzc', use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler('bop',bop))
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()

# from telegram.ext import Updater, InlineQueryHandler, CommandHandler
# import requests
# import re

# def get_url():
#     contents = requests.get('https://random.dog/woof.json').json()    
#     url = contents['url']
#     return url

# def get_image_url():
#     allowed_extension = ['jpg','jpeg','png']
#     file_extension = ''
#     while file_extension not in allowed_extension:
#         url = get_url()
#         file_extension = re.search("([^.]*)$",url).group(1).lower()
#     return url

# def bop(bot, update):
#     url = get_image_url()
#     chat_id = update.message.chat_id
#     bot.send_photo(chat_id=chat_id, photo=url)

# def main():
#     updater = Updater('1137170938:AAGbOrkFpLg_y2YSyONY0DLUye-e5p0TPzc', use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler('bop',bop))
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re
import logging
import os
import sys
import random

# Enabling logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Getting mode, so we could define run function for local and Heroku setup
mode = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")
if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
else:
    logger.error("No MODE specified!")
    sys.exit(1)

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@run_async
def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('1010556494:AAG0-5rvy9scE_llIawpGe3wYHyJEzTzAps', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
