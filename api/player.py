"""Clash Of Clans Player API."""
import urllib
import requests
from flask_restful import Resource, reqparse
from flask import Response

from settings import SETTINGS
from tools.mysql import call_procedure
KEY = 'Bearer ' + SETTINGS['clash_key']

class Player(Resource):
    """Clash Of Clans Player API."""
    def __init__(self):
        """Contructor."""
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str)
        self.parser.add_argument('level', type=int)
        self.url = "https://api.clashofclans.com/v1/players/"
        self.headers = {
            "authorization": KEY
        }
    def get(self, player_id):
        """HTTP GET method."""
        player_id = urllib.quote_plus(player_id)
        response = requests.get(self.url + player_id, headers=self.headers)
        return Response(response=response.text,
                        status=200,
                        mimetype="application/json")

    def post(self, player_id):
        """HTTP POST method."""
        args = self.parser.parse_args()
        cur_args = (player_id, args.username, args.level)
        msg = call_procedure('th_add', cur_args)
        if msg['status'] == 'ok':
            msg['message'] = 'townhall information successfully processed'
        return msg
