from Models.VendasItens import VendasItens
from Models.Cliente import Cliente
from Models.Venda import Venda
from telegram import Update, ForceReply, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import locale
import prettytable

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
    """Retorna mensagem da função total formatada e estilizada"""
    total_formatado = locale.currency(total, grouping=True)
    return "Total de vendas: " + total_formatado


def cliente(update: Update, context: CallbackContext) -> None:
    cliente_id = context.args[0]
    venda = Venda.select().order_by(Venda.data.desc()).limit(
        1).where(Venda.cliente_id == cliente_id).get()
    vendas_itens = VendasItens.select(VendasItens).where(
        VendasItens.venda_id == venda.id)

    context.bot.send_message(chat_id=update.effective_chat.id, text=cliente_mensagem(vendas_itens), parse_mode=ParseMode.HTML)


def cliente_mensagem(vendas_itens):
    """Retorna mensagem da função cliente formatada e estilizada"""
    tabela = prettytable.PrettyTable(['Item', 'Quantidade', 'Valor'])
    tabela.align['Item'] = 'l'
    tabela.align['Quantidade'] = 'r'
    tabela.align['Valor'] = 'r'
    venda_id = str(vendas_itens[0].venda_id)
    total = 0
    detalhamento = []
    for venda_item in vendas_itens:
        total += venda_item.valor * venda_item.quantidade
        detalhamento.append((venda_item.produto_id.nome, venda_item.quantidade, venda_item.valor))
    total_formatado = locale.currency(total, grouping=True)
    for item, quantidade, valor in detalhamento:
        tabela.add_row([item, f'{quantidade:.2f}', f'{valor:.3f}'])

    return 'Pedido ' + venda_id + '\nValor: ' + total_formatado + f'<pre>{tabela}</pre>'
