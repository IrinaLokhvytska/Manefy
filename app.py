from sanic import Sanic
from sanic.response import json
from transport import data_provider

app = Sanic()


@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/webhook')
async def webhook(request):
    dropbox_class = data_provider.DropboxTransport()
    dropbox_class.save_monefy_file()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
