import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.transaction import Transaction, Category

engine = create_engine('postgresql://postgres:111@localhost:5432/monefy')
connection = engine.connect()
Session = sessionmaker()
Session.configure(bind=engine)


def add_transaction_2_bd(monefy_data):
    df = pd.DataFrame(monefy_data)
    sess = Session()
    for i in range(len(df)):
        category = add_category_2_bd(df['category'][i])
        date = df['date'][i]
        model = Transaction()
        model.date = date
        model.account = df['account'][i]
        model.category = category
        model.amount = convert_ammount(df['amount'][i])
        model.currency = df['currency'][i]
        model.converted_amount = convert_ammount(df['converted amount'][i])
        model.converted_currency = df['currency.1'][i]
        model.description = df['description'][i]
        model.is_debet = model.amount >= 0
        sess.add(model)
    sess.commit()


def add_category_2_bd(category):
    sess = Session()
    model = Category()
    if check_category_exist(category, sess):
        model.title = category
        model.amount = '1000'
        sess.add(model)
        sess.commit()
        sess.flush()
        return model.id
    else:
        return get_category_id(category, sess)


def check_category_exist(category, session):
    res = session.query(Category).filter(Category.title == category).all()
    if not res:
        return True


def get_category_id(category, session):
    res = session.query(Category).filter(Category.title == category).first()
    return res.id


def convert_ammount(amount: str) -> float:
    result = lambda x: x.replace('\xa0', '')
    return float(pd.to_numeric(result(amount)))


def delete_table():
    connection.execute('DROP TABLE transaction')
    connection.execute('DROP TABLE category')
    connection.execute('DROP TABLE alembic_version')

def select_transaction():
    session = Session()
    res = session.query(Transaction).all()
    for e in res:
        print(e. date, e.account, e.amount, e.category, e.currency, e.is_debet)
