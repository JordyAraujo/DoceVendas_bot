import BaseModel

class VendasItens(BaseModel):
    id = peewee.IntegerField(primary_key=True)
    venda_id = peewee.ForeignKeyField(Venda)
    produto_id = peewee.ForeignKeyField(Produto)
    valor = peewee.FloatField()
    quantidade = peewee.IntegerField()