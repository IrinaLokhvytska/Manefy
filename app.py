from sanic import Sanic
from sanic.response import text, json
from transport.data_provider import DropboxTransport
from file_parse.file_parser import FileParse

app = Sanic()


@app.route('/')
async def test(request):
    return json({'hello': 'world'})


@app.route('/webhook')
async def webhook(request):
    dropbox_class = DropboxTransport()
    file_class = FileParse()
    path = dropbox_class.save_monefy_file()
    data = file_class.read_from_file(path)
    balance = str(file_class.get_balance(data))
    return text(balance)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
