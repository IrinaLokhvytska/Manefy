import dropbox
from monefy_app import keys


class DropboxTransport:
    def upload_file_to_dropbox(self):
        sess = dropbox.session.DropboxSession(keys.APP_KEY, keys.APP_SECRET, keys.ACCESS_TYPE)
        sess.set_token(keys.access_token)
        client = dropbox.client.DropboxClient(sess)
        f = open('dropbox-upload.py')
        client.put_file('/dropbox-upload.py', f)