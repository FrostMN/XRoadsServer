from XRoadsServer.utils.database.schema import schema
import XRoadsServer.utils.database.test_data as data
from XRoadsServer.utils.secrets.users import hash_password
# from XRoadsServer.Main import app
from config import TestingConfig as config
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
    print("init")
    for qry in schema:
        execute_query(qry)


def load_db():
    print("load")
    user_qry = "INSERT INTO users (" \
               "    user_id, user_name, email, email_confirmed, temp_email, admin, first_name, last_name, hash" \
               ") VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s )"

    char_qry = "INSERT INTO characters ( " \
               "    characters_id, user_id, character_name, character_background, character_class, character_rank, rank_up" \
               ") VALUES ( %s, %s, %s, %s, %s, %s, %s ) "

    for u in data.users:
        hashed = hash_password(u[1])
        user_args = (u[0].user_id, u[0].user_name, u[0].email, 1, None, u[0].admin, u[0].first_name, u[0].last_name, hashed)
        execute_query(user_qry, user_args)

    for c in data.characters:

        background = c.background.name[:3].lower()
        character_class = c.character_class.name[:3].upper()

        print(background)

        char_args = (c.id, c.player_id, c.character_name, background, character_class, c.rank_value, c.ranks_available)
        execute_query(char_qry, char_args)


if __name__ == '__main__':
    init_db()


