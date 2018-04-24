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
        category = df['category'][i].strip().lower()
        model = Transaction()
        model.date = df['date'][i]
        model.account = df['account'][i]
        if check_category_exist(category, sess):
            model.category = sess.add(Category(title=category))
        else:
            model.category = get_category_id(category, sess)
        model.amount = convert_ammount(df['amount'][i])
        model.currency = df['currency'][i]
        model.converted_amount = convert_ammount(df['converted amount'][i])
        model.converted_currency = df['currency.1'][i]
        model.description = df['description'][i]
        model.is_debet = model.amount >= 0
        sess.add(model)
    sess.commit()
    sess.close()


def check_category_exist(category, session):
    res = session.query(Category).filter(Category.title == category).all()
    if not res:
        return True


def get_category_id(category, session):
    res = session.query(Category).filter(Category.title == category).first()
    return res.id


def convert_ammount(amount: str) -> float:
    result = amount.replace('\xa0', '')
    return float(pd.to_numeric(result))


def select_transaction():
    session = Session()
    res = session.query(Transaction).all()
    for e in res:
        print(e. date, e.account, e.amount, e.category, e.currency, e.is_debet)
    cat = session.query(Category).all()
    for c in cat:
        print(c.title, c.limit, c.start_date, c.period)
    session.close()


def delete_tables():
    Transaction.__table__.drop(engine)
    Category.__table__.drop(engine)
    connection.execute('DROP TABLE alembic_version')


if __name__ == '__main__':
    delete_tables()
