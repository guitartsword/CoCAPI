"""Clash of Clans."""
from flask import Flask
from flask_restful import Api
from api.player import Player

APP = Flask(__name__)
API = Api(APP)

@APP.route('/')
def root():
    """Returns hola perro."""
    return 'Hola Perro'

API.add_resource(
    Player,
    '/player',
)

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80)
