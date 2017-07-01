"""Clash Of Clans Player API."""
from flask_restful import Resource, reqparse
import requests
import json

with open('auth.json') as auth:
    KEY = 'Bearer ' + json.load(auth)['key']

class Player(Resource):
    """Clash Of Clans Player API."""
    def __init__(self):
        """Contructor."""
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('player_id', required=True)
        self.url = "https://api.clashofclans.com/v1/players/"
        self.headers = {
            "authorization": KEY
        }
    def get(self):
        """HTTP GET method."""
        args = self.parser.parse_args()
        player_id = '%23' + args.get('player_id')
        print player_id
        response = requests.request("GET", self.url + player_id, headers=self.headers)
        res_obj = json.loads(response.text)
        return res_obj, 200
