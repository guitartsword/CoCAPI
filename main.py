"""Clash of Clans."""
from flask import Flask
from flask_cors import CORS
from flask_restful import Api


from api.player import Player
from api.clan import Clan
from api.building import Building
from settings import ENV, SETTINGS

APP = Flask(__name__)
APP.config.update(SETTINGS['mysql'])
CORS(APP)
API = Api(APP)

@APP.route('/')
def root():
    """ Returns welcome. """
    return 'The %s environment is working' % ENV

API.add_resource(
    Player,
    '/player/<player_id>',
)

API.add_resource(
    Clan,
    '/clan/<clan_id>',
)
API.add_resource(
    Building,
    '/building',
)

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080)
