""" Module represents a Transaction. """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, String, Integer, Date,  ForeignKey, Boolean, Float, DateTime
)
from datetime import datetime

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, autoincrement=True, primary_key=True)
    timestamp = Column('timestamp', DateTime, default=datetime.utcnow())
    title = Column(String(255), nullable=False)
    limit = Column(Float, nullable=True)
    start_date = Column(Date, nullable=True)
    period = Column(Integer, nullable=True)
    is_repeated = Column(Boolean, nullable=True)
    transaction = relationship("Transaction")



class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, autoincrement=True, primary_key=True)
    timestamp = Column('timestamp', DateTime, default=datetime.utcnow())
    date = Column(Date, nullable=False)
    account = Column(String(255), nullable=False)
    category = Column(ForeignKey('category.id'))
    amount = Column(Float, nullable=False)
    currency = Column(String(30), nullable=False)
    converted_amount = Column(Float, nullable=False)
    converted_currency = Column(String(30), nullable=False)
    description = Column(String(30), nullable=True)
    is_debet = Column(Boolean)

    # Methods
    def __repr__(self):
        """ Show transaction object info. """
        return '<Transaction: {}>'.format(self.id)
