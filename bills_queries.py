from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from sql_homework.model import Expenses, Categories, ExpCat
from datetime import date

if __name__ == '__main__':
    engine = create_engine('sqlite:///../bills.db', echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    # get all expenses
    print('All expenses:')
    for expense in session.query(Expenses):
        print(expense)
    print(' ')

    # get all categories
    print('All categories:')
    for category in session.query(Categories):
        print(category)
    print(' ')

    # get all expenses in specified time range
    print('Get all expenses newer than 2019-01-01')
    for expense in session.query(Expenses).filter(Expenses.date > date(2019, 1, 1)):
        print(expense)
    print(' ')

    print('Get all expenses from 2018 year')
    for expense in session.query(Expenses).filter(and_(Expenses.date > date(2018, 1, 1), Expenses.date < date(2018, 12, 31))):
        print(expense)
    print(' ')

    # get all expenses from one category
    print('Get names and prices of all expenses from category: napoje.')
    for x in session.query(Categories, Expenses).filter(Categories.cat_id == ExpCat.cat_id, Expenses.exp_id == ExpCat.exp_id, Categories.name == 'napoje').all():
        print("Category: {}, Expense: {} - {} PLN".format(x.Categories.name, x.Expenses.name, x.Expenses.value))
    print()



