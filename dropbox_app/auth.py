import dropbox


class AuthDropbox:
    APP_KEY = '34dhhdhghefudx5'
    APP_SECRET = 'edfvmiwc9dnfjjy'
    ACCESS_TYPE = 'Full Dropbox'
    access_token = 'mB-ACISwtPAAAAAAAAAADwhABRbwQ9dEhPaAgr5Vkf2UaPW335aW6kxq9JCg4tPI'

    def upload_file_to_dropbox(self):
        sess = dropbox.session.DropboxSession(self.APP_KEY, self.APP_SECRET, self.ACCESS_TYPE)
        sess.set_token(self.access_token)
        client = dropbox.client.DropboxClient(sess)
        f = open('dropbox-upload.py')
        client.put_file('/dropbox-upload.py', f)
