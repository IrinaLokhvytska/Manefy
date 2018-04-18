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
        '''The method that allows you to get the current information
        about dropbox account using the access token.'''
        return self.dbx.users_get_current_account()

    def __get_list_of_files(self) -> list:
        '''The method that gets a list of files from the dropbox account.'''
        files = []
        try:
            files = self.dbx.files_list_folder(self.dir).entries
        except Exception as e:
            print(e)
        return files

    def save_monefy_file(self) -> str:
        '''The method that saves the last monefy file in the specified directory'''
        file = self.__get_new_file(self.__get_list_of_files())
        id = self.test_dropbox().root_info.root_namespace_id
        path = ''
        if file:
            path_to_file = '{0}/{1}'.format(self.dir, file)
            path = '{0}/{1}{2}'.format(self.download_path, id, file)
            self.dbx.files_download_to_file(path, path_to_file)
        return path

    def __get_new_file(self, files: list) -> str:
        '''The method that gets the last monefy file'''
        date = datetime(1, 1, 1)
        file = ''
        monefy_files = self.__get_monefy_files(files)
        for i in range(len(monefy_files)):
            file_date = self.__parse_date_of_file(monefy_files[i].name)
            if file_date and file_date > date:
                date = file_date
                file = monefy_files[i].name
        return file

    '''
        :param files: a list of files from the dropbox account.
    '''

    @staticmethod
    def __parse_date_of_file(file: str) -> datetime:
        '''The method that pars date from the file name'''
        pattern = r'(\d{1,2}(\-|\.)\d{1,2}(\-|\.)\d{2})'
        match = re.search(pattern, file)
        helper = [('.', '%d.%m.%y'), ('-', '%m-%d-%y')]
        file_date = match[0] if match else 'Not found'
        for v in helper:
            if file_date.find(v[0]) > 1:
                return datetime.strptime(file_date, v[1])

    '''
        :param file: a name of the monefy file.
    '''

    @staticmethod
    def __get_monefy_files(files: list) -> list:
        '''The method that returns the list only of the monefy files'''
        monefy_files = list(filter(lambda x: x.name.startswith('Monefy.Data'), files))
        return monefy_files


if __name__ == '__main__':
    dropbox_class = DropboxTransport()
    print(dropbox_class.test_dropbox())
