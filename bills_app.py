from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_homework.model import Base, Expenses, Categories
import datetime

if __name__ == '__main__':
    engine = create_engine('sqlite:///../bills.db', echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    name = input("name of product: ")
    value_input = input("price (in PLN, separate with '.' eg. 3.99): ")
    value = float(value_input)
    date_input = input("date of purchase (yyyy-mm-dd): ")
    date = datetime.datetime.strptime(date_input, '%Y-%m-%d')
    categories = input("categories (separate with ',' eg. cat_1,cat_2): ").lower()
    cat_list = categories.split(',')

    expense = Expenses(name=name, value=value, date=date)

    for category_name in cat_list:
        category = session.query(Categories).filter_by(name=category_name).scalar()

        if category is None:
            category = Categories(name=category_name)
            session.add(category)

        expense.categories.append(category)

    session.add(expense)

    session.commit()
    session.close()

