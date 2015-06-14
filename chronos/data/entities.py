from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, String


Entity = declarative_base()


class User(Entity):

    __tablename__ = 'users'

    ADMIN = 'admin'
    EMPLOYEE = 'employee'

    id = Column(BigInteger, primary_key=True)
    email = Column(String(256), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    type = Column(String(10), nullable=False)
