import pymysql

class DatabaseManager(object):
    def __init__(self):
        pass
    def get_connection(self):
        db = pymysql.connect(host='shanmugapriyacp.mysql.pythonanywhere-services.com', user='shanmugapriyacp',
                             password='mysql!23', db='shanmugapriyacp$user_contact')
        cur = db.cursor(pymysql.cursors.DictCursor)
        return cur
