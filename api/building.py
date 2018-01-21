"""Clash Of Clans Player API."""
from flask_restful import Resource, reqparse
from pymysql import InternalError
from settings import SETTINGS

KEY = 'Bearer ' + SETTINGS['clash_key']

class Building(Resource):
    """Clash Of Clans Player API."""
    def __init__(self, cnx):
        """Contructor."""
        self.cnx = cnx
        self.cursor = cnx.cursor()
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
        try:
            args = self.parser.parse_args()
            cur_args = (args.th_id, args.building_id, args.level)
            self.cursor.callproc('building_add_to_th', cur_args)
            self.cnx.commit()
            return {
                'status': 'ok',
                'message':'building added successfully'
            }
        except InternalError as error:
            print error
            if error[0] == 1644:
                status = 'invalid_sp'
            else:
                status = 'mysql_error'
            return {
                'status': status,
                'message':error[1]
            }
