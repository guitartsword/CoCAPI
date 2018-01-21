"""Clash Of Clans Player API."""
import json
import urllib
import requests
from flask_restful import Resource, reqparse
from flask import Response
from settings import SETTINGS
KEY = 'Bearer ' + SETTINGS['clash_key']

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
        response = requests.get(self.url + player_id, headers=self.headers)
        return Response(response=response.text,
                        status=200,
                        mimetype="application/json")

    def post(self, player_id):
        """HTTP POST method."""
        return "Not available for now"
