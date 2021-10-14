from Models import Produto, Cliente, Venda, VendasItens
from csv import reader
import glob

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
        list_of_tuples = []
        # open file in read mode
        with open(arquivo, 'r') as obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(obj)
            # Get all rows of csv from csv_reader object as list of tuples
            list_of_tuples = list(map(tuple, csv_reader))


        del list_of_tuples[0]
        tabela = arquivo.split("\\")[2].split(".")[0]

        registros = []
        if tabela == 'cliente':
            Cliente.insert_many(list_of_tuples, fields=[Cliente.id, Cliente.nome]).execute()
        elif tabela == 'produto':
            Produto.insert_many(list_of_tuples, fields=[Produto.id, Produto.nome]).execute()
        elif tabela == 'venda':
            Venda.insert_many(list_of_tuples, fields=[Venda.id, Venda.cliente_id, Venda.data]).execute()
        elif tabela == 'venda_itens':
            VendasItens.insert_many(list_of_tuples, fields=[VendasItens.id, VendasItens.venda_id, VendasItens.produto_id, VendasItens.valor, VendasItens.quantidade]).execute()