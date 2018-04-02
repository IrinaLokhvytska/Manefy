from sanic import Sanic
from sanic.response import json
from dropbox_app import auth
# import sqlalchemy
# import alembic
# import telepot
# import flake8
# import oauth2client
# import os

app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})


@app.route('/upload')
async def test(request):
    dropbox_class = auth.AuthDropbox()
    dropbox_class.upload_file_to_dropbox()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
