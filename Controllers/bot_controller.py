from Models.VendasItens import VendasItens
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')


def start(update: Update, context: CallbackContext) -> None:
    """Envia uma mensagem quando o Bot é iniciado (comando /start no Telegram)."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Olá {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def echo(update: Update, context: CallbackContext) -> None:
    """Repete a mensagem enviada pelo usuário."""
    update.message.reply_text(update.message.text)


def total(update: Update, context: CallbackContext) -> None:
    """Retorna o valor de todas as vendas"""
    total = 0
    for venda in VendasItens.select():
        valor = venda.valor * venda.quantidade
        total += valor

    update.message.reply_text(total_mensagem(total))

def total_mensagem(total):
    """Retorna mensagem de total formatada e estilizada"""
    total_formatado = locale.currency(total, grouping=True)
    mensagem = "Total de vendas: " + total_formatado
    return mensagem
