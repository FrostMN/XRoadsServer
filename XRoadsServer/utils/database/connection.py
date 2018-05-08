from XRoadsServer.utils.database.schema import schema
# from XRoadsServer.Main import app
from config import DevelopmentConfig as config
import MySQLdb

sql_host = config.MYSQL_HOST
sql_port = int(config.MYSQL_PORT)
sql_pwd = config.MYSQL_PASSWORD
sql_usr = config.MYSQL_USER
sql_db = config.MYSQL_DB

db = MySQLdb.connect(host=sql_host, port=sql_port, user=sql_usr, passwd=sql_pwd, db=sql_db)


def execute_query(qry, params=None, custom_functions=None):
    if params:
        if custom_functions is not None:
            for f in custom_functions:
                db.create_function(f[0], f[1], f[2])
        with db.cursor() as cur:
            try:
                cur.execute(qry, params)
                db.commit()
            except MySQLdb.Error as e:
                db.rollback()
                print("MySql Transaction error:\n" + str(e))
                return e
    else:
        with db.cursor() as cur:
            try:
                cur.execute(qry)
                db.commit()
            except MySQLdb.Error as e:
                db.rollback()
                print("MySql Transaction error:\n" + str(e))
                return e


def get_rs(qry, params=None, custom_functions=None):
    if params:
        if custom_functions is not None:
            for f in custom_functions:
                db.create_function(f[0], f[1], f[2])
        with db.cursor() as cur:
            try:
                cur.execute(qry, params)
                rs = cur.fetchall()
                if len(rs) == 1:
                    rs = rs[0]
                db.commit()
                return rs
            except MySQLdb.Error as e:
                db.rollback()
                print("MySql Transaction error:\n" + str(e))
                return e
    else:
        with db.cursor() as cur:
            try:
                cur.execute(qry)
                rs = cur.fetchall()
                db.commit()
                return rs
            except MySQLdb.Error as e:
                db.rollback()
                print("MySql Transaction error:\n" + str(e))
                return e


def init_db():
    for qry in schema:
        execute_query(qry)


if __name__ == '__main__':
    init_db()
