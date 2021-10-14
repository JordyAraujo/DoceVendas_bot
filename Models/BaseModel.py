import peewee

db = peewee.SqliteDatabase('docevendas_bot.db')

class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        database = db