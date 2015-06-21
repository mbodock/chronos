from peewee import SqliteDatabase, Model
from chronos.config import config


if config.database.get('driver') == 'sqlite':
    database = SqliteDatabase(config.database.get('dbname'))


class Entity(Model):

    class Meta:
        database = database
