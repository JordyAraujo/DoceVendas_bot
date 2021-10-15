from Controllers.bot_controller import *
import logging
import os
import sys

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

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


def main() -> None:
    """Inicia o bot."""
    # Cria o "Updater" com o token do Bot.
    updater = Updater(TOKEN)

    # Seta o "dispatcher" para registrar os manipuladores
    dispatcher = updater.dispatcher

    # Seta o comando /start para chamar sua respectiva função
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("total", total))
    dispatcher.add_handler(CommandHandler("cliente",cliente))

    # Inicia o Bot de fato
    updater.start_polling()

    # Mantém o Bot rodando até que receba um comando para encerrar a execução
    updater.idle()


if __name__ == '__main__':
    main()
