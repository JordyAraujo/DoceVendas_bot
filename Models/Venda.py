from .Cliente import Cliente
from .BaseModel import BaseModel
import peewee

class Venda(BaseModel):
    id = peewee.IntegerField(primary_key=True)
    cliente_id = peewee.ForeignKeyField(Cliente)
    data = peewee.DateField()