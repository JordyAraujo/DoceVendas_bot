from .BaseModel import BaseModel
import peewee


class Cliente(BaseModel):
    id = peewee.IntegerField(primary_key=True)
    nome = peewee.CharField(max_length=4000, unique=True)
