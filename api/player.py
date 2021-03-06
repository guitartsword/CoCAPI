"""Clash Of Clans Player API."""
import json
import urllib
import requests
from flask_restful import Resource, reqparse
from flask import Response

with open('auth.json') as auth:
    KEY = 'Bearer ' + json.load(auth)['key']

class Player(Resource):
    """Clash Of Clans Player API."""
    def __init__(self):
        """Contructor."""
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('offensive_weight', type=bool)
        self.url = "https://api.clashofclans.com/v1/players/"
        self.headers = {
            "authorization": KEY
        }
    def get(self, player_id):
        """HTTP GET method."""
        player_id = urllib.quote_plus(player_id)
        response = requests.request("GET", self.url + player_id, headers=self.headers)
        return Response(response=response.text,
                        status=200,
                        mimetype="application/json")
