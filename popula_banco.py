from Models.Produto import *
from Models.Cliente import *
from Models.Venda import *
from Models.VendasItens import *
from csv import reader
import glob
import peewee

if __name__ == '__main__':
    try:
        Produto.create_table()
        print("Tabela 'Produto' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Produto' ja existe!")


    try:
        Cliente.create_table()
        print("Tabela 'Cliente' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Cliente' ja existe!")


    try:
        Venda.create_table()
        print("Tabela 'Venda' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Venda' ja existe!")


    try:
        VendasItens.create_table()
        print("Tabela 'VendasItens' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'VendasItens' ja existe!")


    caminho = ".\data\*.csv"
    for arquivo in glob.glob(caminho):
        tuplas = []
        with open(arquivo, 'r') as obj:
            csv = reader(obj)
            tuplas = list(map(tuple, csv))


        del tuplas[0]
        tabela = arquivo.split("\\")[2].split(".")[0]

        registros = []
        if tabela == 'cliente':
            Cliente.insert_many(tuplas, fields=[Cliente.id, Cliente.nome]).execute()
        elif tabela == 'produto':
            Produto.insert_many(tuplas, fields=[Produto.id, Produto.nome]).execute()
        elif tabela == 'venda':
            Venda.insert_many(tuplas, fields=[Venda.id, Venda.cliente_id, Venda.data]).execute()
        elif tabela == 'venda_itens':
            VendasItens.insert_many(tuplas, fields=[VendasItens.id, VendasItens.venda_id, VendasItens.produto_id, VendasItens.valor, VendasItens.quantidade]).execute()