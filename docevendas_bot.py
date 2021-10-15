from Controllers.bot_controller import *
import logging
import secrets

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Inicia o bot."""
    # Cria o "Updater" com o token do Bot.
    updater = Updater(secrets.token)

    # Seta o "dispatcher" para registrar os manipuladores
    dispatcher = updater.dispatcher

    # Seta o comando /start para chamar sua respectiva função
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("total", total))

    # Quando a mensagem não for um comando, chama a função 'echo'
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Inicia o Bot de fato
    updater.start_polling()

    # Mantém o Bot rodando até que receba um comando para encerrar a execução
    updater.idle()


if __name__ == '__main__':
    main()
