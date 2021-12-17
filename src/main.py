import logging
import os

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, MessageHandler
from dotenv import load_dotenv

from handlers import start, help_handler, game_handler, game_button_handler, echo


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

load_dotenv('../.env')

TOKEN = os.environ.get('TOKEN', '')
DEBUG = os.environ.get('DEBUG', False)
PORT = int(os.environ.get('PORT', '8443'))
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', '')


def main():
    print(TOKEN)
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_handler))
    dp.add_handler(CommandHandler("game", game_handler))
    dp.add_handler(CallbackQueryHandler(game_button_handler, pattern='^button_'))

    dp.add_handler(MessageHandler(Filters.text, echo))

    if DEBUG:
        updater.start_polling()
    else:
        updater.start_webhook(listen="0.0.0.0",
                              port=int(PORT),
                              url_path=TOKEN,
                              webhook_url=WEBHOOK_URL + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
