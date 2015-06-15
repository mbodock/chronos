from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chronos.config import config
from .entities import Entity


engine = create_engine(config.database, isolation_level='SERIALIZABLE')

if config.create_schema:
    Entity.metadata.create_all(engine)

Session = sessionmaker(autocommit=True)
Session.configure(bind=engine)

database = Session()
