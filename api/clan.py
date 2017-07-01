"""Clash Of Clans Clan API."""
import json
import urllib
import requests
from flask_restful import Resource, reqparse
from flask import Response

with open('auth.json') as auth:
    KEY = 'Bearer ' + json.load(auth)['key']

class Clan(Resource):
    """Clash Of Clans Clan API."""
    def __init__(self):
        """Contructor."""
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('offensive_weight', type=bool)
        self.url = "https://api.clashofclans.com/v1/clans/"
        self.headers = {
            "authorization": KEY
        }
    def get(self, clan_id):
        """HTTP GET method."""
        clan_id = urllib.quote_plus(clan_id)
        url = self.url + clan_id + "/members"
        response = requests.request("GET", url, headers=self.headers)
        return Response(response=response.text,
                        status=200,
                        mimetype="application/json")
