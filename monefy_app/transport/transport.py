import dropbox
from monefy_app import keys


class DropboxTransport:
    @staticmethod
    def test_dropbox():
        dbx = dropbox.Dropbox(keys.access_token)
        return dbx.users_get_current_account()


if __name__ == '__main__':
    dropbox_class = DropboxTransport()
    print(dropbox_class.test_dropbox())
