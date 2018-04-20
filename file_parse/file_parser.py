import pandas as pd
import os
from monefy_app.parser import add_transaction_2_bd, select_transaction

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class FileParse:
    @staticmethod
    def read_from_file(path: str) -> object:
        return pd.read_csv(path)

    def get_balance(self, data: object) -> object:
        df = pd.DataFrame(data)
        amount = self.__replace_space(df['amount'])
        result = self.__convert_amount_2_float(amount).sum()
        return result

    @staticmethod
    def __replace_space(amount: str) -> str:
        return amount.apply(lambda x: x.replace('\xa0', ''))

    @staticmethod
    def __convert_amount_2_float(amount: str) -> object:
        return pd.to_numeric(amount)


if __name__ == '__main__':
    file_parser = FileParse()
    data = file_parser.read_from_file('{}/{}/2762457936Monefy.Data.05.04.18.csv'.format(root_dir, 'downloads'))
    # delete_table()
    add_transaction_2_bd(data)
    select_transaction()
