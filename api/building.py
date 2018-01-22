"""Clash Of Clans Player API."""
from flask_restful import Resource, reqparse
from settings import SETTINGS
from tools.mysql import call_procedure
KEY = 'Bearer ' + SETTINGS['clash_key']

class Building(Resource):
    """Clash Of Clans Player API."""
    def __init__(self):
        """Contructor."""
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('th_id', type=str, required=True)
        self.parser.add_argument('building_id', type=str, required=True)
        self.parser.add_argument('level', type=int, required=True)
        self.url = "https://api.clashofclans.com/v1/players/"
        self.headers = {
            "authorization": KEY
        }

    def post(self):
        """HTTP POST method."""
        args = self.parser.parse_args()
        cur_args = (args.th_id, args.building_id, args.level)
        msg = call_procedure('building_add_to_th', cur_args)
        if msg['status'] == 'ok':
            msg['message'] = 'buidling added successfully'
        return msg
