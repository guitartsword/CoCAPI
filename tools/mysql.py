"""MySQL helpers."""
from pymysql.err import InternalError
from pymysql import connect as connect_pymysql
from settings import SETTINGS

def call_procedure(proc_name, proc_args):
    """
    calls a stored procedure, opens and
    closes the connection and cursor.
    """
    cnx = connect_pymysql(**SETTINGS['mysql'])
    try:
        with cnx.cursor() as cur:
            cur.callproc(proc_name, proc_args)
            cnx.commit()
            return {'status': 'ok'}
    except InternalError as error:
        if error[0] == 1644:
            status = 'invalid_sp'
        else:
            status = 'mysql_error'
        return {
            'status': status,
            'message':error[1]
        }
    cnx.close()
