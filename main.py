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
