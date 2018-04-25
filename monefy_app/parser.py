import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.transaction import Transaction, Category
from sqlalchemy.dialects.postgresql import insert

engine = create_engine('postgresql://postgres:111@localhost:5432/monefy')
connection = engine.connect()
Session = sessionmaker()
Session.configure(bind=engine)


def add_transaction_2_bd(monefy_data):
    df = pd.DataFrame(monefy_data)
    for i in range(len(df)):
        category = df['category'][i].strip().lower()
        category_id = insert_category_2_bd(category)
        insert_transaction = insert(Transaction).values(
            date=df['date'][i],
            account=df['account'][i],
            category=category_id,
            amount=abs(convert_ammount(df['amount'][i])),
            currency=df['currency'][i],
            converted_amount=convert_ammount(df['converted amount'][i]),
            converted_currency=df['currency.1'][i],
            description=str(df['description'][i]),
            is_debet=convert_ammount(df['amount'][i]) > 0
        )
        on_update_transaction = insert_transaction.on_conflict_do_update(
            constraint='tr_constraint',
            set_=dict(
                category=category_id,
                currency=df['currency'][i],
                converted_amount=convert_ammount(df['converted amount'][i]),
                converted_currency=df['currency.1'][i],
                is_debet=convert_ammount(df['amount'][i]) > 0
            )
        )
        connection.execute(on_update_transaction)


def insert_category_2_bd(category):
    insert_category = insert(Category).values(
        title=category
    )
    do_nothing_category = insert_category.on_conflict_do_nothing(
        index_elements=['title']
    )
    res = connection.execute(do_nothing_category)
    if res.inserted_primary_key:
        return res.inserted_primary_key[0]
    else:
        return get_category_id(category)


def get_category_id(category):
    session = Session()
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
    delete_tables()
