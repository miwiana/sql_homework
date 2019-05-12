"""Mapping and defining schema using SQLAlchemy ORM"""

from sqlalchemy import Integer, String, Float, Column, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Expenses(Base):
    __tablename__ = 'expenses'

    exp_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    value = Column(Float)
    date = Column(Date)

    categories = relationship('Categories', secondary='exp_cat', back_populates='expenses')

    def __repr__(self):
        return f'{self.name} - {self.value} PLN, {self.date} (id {self.exp_id})'


class Categories(Base):
    __tablename__ = 'categories'
    cat_id = Column(Integer, auto_increment=True, primary_key=True)
    name = Column(String)

    expenses = relationship('Expenses', secondary='exp_cat', back_populates='categories')

    def __repr__(self):
        return f'{self.name} (id {self.cat_id})'


class ExpCat(Base):
    __tablename__ = 'exp_cat'

    cat_id = Column(Integer, ForeignKey('categories.cat_id'), primary_key=True)
    exp_id = Column(Integer, ForeignKey('expenses.exp_id'), primary_key=True)
