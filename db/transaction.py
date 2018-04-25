""" Module represents a Transaction. """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, String, Integer, Date,  ForeignKey, Boolean, Float, DateTime, UniqueConstraint
)
from datetime import datetime

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, autoincrement=True, primary_key=True)
    timestamp = Column('timestamp', DateTime, default=datetime.utcnow())
    title = Column(String(255), nullable=False, unique=True)
    limit = Column(Float, nullable=True)
    start_date = Column(Date, nullable=True)
    period = Column(Integer, nullable=True)
    is_repeated = Column(Boolean, nullable=True)
    transaction = relationship("Transaction")


class Transaction(Base):
    __tablename__ = 'transaction'
    __table_args__ = (
        UniqueConstraint('date', 'account', 'amount', 'description', name='tr_constraint'),
    )

    id = Column(Integer, autoincrement=True, primary_key=True)
    timestamp = Column('timestamp', DateTime, default=datetime.utcnow())
    date = Column('date', Date, nullable=False)
    account = Column('account', String(255), nullable=False)
    category = Column('category', ForeignKey('category.id'))
    amount = Column('amount', Float, nullable=False)
    currency = Column('currency', String(30), nullable=False)
    converted_amount = Column('converted_amount', Float, nullable=False)
    converted_currency = Column('converted_currency', String(30), nullable=False)
    description = Column('description', String(30), nullable=True)
    is_debet = Column('is_debet', Boolean)


    # Methods
    def __repr__(self):
        """ Show transaction object info. """
        return '<Transaction: {}>'.format(self.id)
