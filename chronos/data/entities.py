from peewee import CharField, ForeignKeyField, DateTimeField

from chronos.data.database import Entity, database
from chronos.config import config


class User(Entity):

    ADMIN = 'admin'
    EMPLOYEE = 'employee'

    email = CharField(256, unique=True)
    password = CharField(60)
    type = CharField(10)


class Session(Entity):

    user = ForeignKeyField(User, related_name='sessions')
    token = CharField(36, unique=True)


class Clock(Entity):

    user = ForeignKeyField(User, related_name='clocks')
    start = DateTimeField()
    stop = DateTimeField(null=True)


if config.database.get('create_schema'):
    database.create_tables([User, Session, Clock], safe=True)
