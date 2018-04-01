from sanic import Sanic
from sanic.response import json
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
