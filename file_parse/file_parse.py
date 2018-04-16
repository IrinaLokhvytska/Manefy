import pandas as pd
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class FileParse:
    @staticmethod
    def read_from_file(path):
        return pd.read_csv(path)

    def get_balance(self, data):
        df = pd.DataFrame(data)
        amount = self.__replace_space(df['amount'])
        result = self.__convert_amount_2_float(amount).sum()
        return result

    @staticmethod
    def __replace_space(amount):
        return amount.apply(lambda x: x.replace('\xa0', ''))

    @staticmethod
    def __convert_amount_2_float(amount):
        return pd.to_numeric(amount)


if __name__ == '__main__':
    file_parser = FileParse()
    path = '{0}/{1}/{2}'.format(root_dir, 'downloads', 'Monefy.Data.05.04.18.csv')
    data = file_parser.read_from_file(path)
    print(file_parser.get_balance(data))
