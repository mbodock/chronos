from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, String, ForeignKey


Entity = declarative_base()


class User(Entity):

    __tablename__ = 'users'

    ADMIN = 'admin'
    EMPLOYEE = 'employee'

    id = Column(BigInteger, primary_key=True)
    email = Column(String(256), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    type = Column(String(10), nullable=False)


class Session(Entity):

    __tablename__ = 'sessions'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    token = Column(String(36), nullable=False, unique=True)
