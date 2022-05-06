from datetime import datetime

from sqlalchemy import Column, Integer, String, create_engine, DateTime, ForeignKey, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(VARCHAR(255), unique=True, nullable=False)
    info = Column(VARCHAR(255))
    password = Column(VARCHAR(255), nullable=False)
    history = relationship('History', cascade="all, delete-orphan")

    def to_dict(self):
        return {'id':self.id,
                'login': self.login,
                'info': self.info,
                'password': self.password
                }

    # def __repr__(self):
    #     return f"Логин: {self.login}. Пароль: {self.password}. Info: {self.info}"


class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=datetime.now, comment='Дата входа')
    ip_addr = Column(VARCHAR(255))
    user_id = Column(Integer, ForeignKey('clients.id'))

# class Contacts(Base):
#     __tablename__ = 'contacts'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     owner_id = Column(Integer, ForeignKey('users.id'))
#     client_id = Column(Integer, ForeignKey('users.id'))
