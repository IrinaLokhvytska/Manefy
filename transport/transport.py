import dropbox
import os
import re

from datetime import datetime
import keys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class DropboxTransport:
    '''
    This class is designed to obtain data from the dropbox account
    for Monefy app.
    '''

    def __init__(self):
        self.access_token = keys.access_token
        self.download_path = '{0}/{1}'.format(root_dir, 'downloads')
        self.dbx = dropbox.Dropbox(self.access_token)
        self.dir = ''

    '''
    :param access_token: dropbox API token.
    :param download_path: path to folder where file should be saved.
    :param dbx: initialize Dropbox app for access_token.
    :param dir: root directory in the dropbpx application.
    '''

    def test_dropbox(self) -> object:
        return self.dbx.users_get_current_account()

    def __get_list_of_files(self) -> list:
        files = []
        try:
            files = self.dbx.files_list_folder(self.dir).entries
        except Exception as e:
            print(e)
        return files

    def save_monefy_file(self) -> None:
        file = self.__get_new_file(self.__get_list_of_files())
        if file:
            path_to_file = '{0}/{1}'.format(self.dir, file)
            path = '{0}/{1}'.format(self.download_path, file)
            self.dbx.files_download_to_file(path, path_to_file)

    def __get_new_file(self, files: list) -> str:
        date = datetime(1, 1, 1)
        file = ''
        monefy_files = self.__get_monefy_files(files)
        for i in range(len(monefy_files)):
            file_date = self.__parse_date_of_file(monefy_files[i].name)
            if file_date and file_date > date:
                date = file_date
                file = monefy_files[i].name
        return file

    @staticmethod
    def __parse_date_of_file(file: str) -> datetime:
        pattern = r'(\d{1,2}(\-|\.)\d{1,2}(\-|\.)\d{2})'
        match = re.search(pattern, file)
        helper = [('.', '%d.%m.%y'), ('-', '%m-%d-%y')]
        file_date = match[0] if match else 'Not found'
        for v in helper:
            if file_date.find(v[0]) > 1:
                return datetime.strptime(file_date, v[1])

    @staticmethod
    def __get_monefy_files(files: list) -> list:
        monefy_files = list(filter(lambda x: x.name.startswith('Monefy.Data'), files))
        return monefy_files


if __name__ == '__main__':
    dropbox_class = DropboxTransport()
    print(dropbox_class.test_dropbox())
