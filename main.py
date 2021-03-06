"""Clash of Clans."""
from flask import Flask
from flask_restful import Api
from api.player import Player
from api.clan import Clan

APP = Flask(__name__)
API = Api(APP)

@APP.route('/')
def root():
    """Returns hola perro."""
    return 'Welcome'

API.add_resource(
    Player,
    '/player/<player_id>',
)

API.add_resource(
    Clan,
    '/clan/<clan_id>',
)

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080)
