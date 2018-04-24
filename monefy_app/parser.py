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
        if check_category_exist(category, sess):
            cat = Category(title=category)
            sess.add(cat)
            sess.flush()
            category_id = cat.id
        else:
            category_id = get_category_id(category, sess)
        res = sess.query(Transaction).filter_by(
            date=df['date'][i],
            account=df['account'][i],
            category=category_id,
            amount=abs(convert_ammount(df['amount'][i])),
            currency=df['currency'][i],
            converted_amount=convert_ammount(df['converted amount'][i]),
            converted_currency=df['currency.1'][i],
            description=str(df['description'][i]),
            is_debet=convert_ammount(df['amount'][i]) > 0
        ).first()
        if res:
            print('The transaction exist')
        else:
            model = Transaction()
            model.date = df['date'][i]
            model.account = df['account'][i]
            model.category = category_id
            model.amount = abs(convert_ammount(df['amount'][i]))
            model.currency = df['currency'][i]
            model.converted_amount = convert_ammount(df['converted amount'][i])
            model.converted_currency = df['currency.1'][i]
            model.description = str(df['description'][i])
            model.is_debet = convert_ammount(df['amount'][i]) > 0
            sess.add(model)
    sess.commit()
    sess.close()


def check_that_transaction_exist(transaction, session):
    res = session.query(Transaction).filter_by(
        date=transaction.date,
        account=transaction.account,
        amount=transaction.amount,
        currency=transaction.currency,
        converted_amount=transaction.converted_amount,
        converted_currency=transaction.converted_currency,
        is_debet=transaction.is_debet
    ).first()
    if not res:
        return True


def check_category_exist(category, session):
    res = session.query(Category).filter_by(title=category).first()
    if not res:
        return True


def get_category_id(category, session):
    res = session.query(Category).filter_by(title=category).first()
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


def clean_tables():
    session = Session()
    session.query(Transaction).delete()
    session.query(Category).delete()
    session.commit()
    session.close()


if __name__ == '__main__':
    clean_tables()
