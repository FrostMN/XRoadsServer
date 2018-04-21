from flask import session, redirect, url_for
import XRoadsServer.utils.secrets.users as secrets
from XRoadsServer.models.users import User
import XRoadsServer.utils.database.connection as db
import time
import datetime


def valid_password(user_name: str, password: str) -> bool:
    """ tests if the given password given matches the hash in the db for the given user """
    login_qry = "SELECT hash FROM users WHERE user_name = %s"
    password_rs = db.get_rs(login_qry, (user_name,))
    if password_rs:
        hashed = db.get_rs(login_qry, (user_name,))[0]
        if secrets.check_password_hash(password, hashed):
            return True
        else:
            return False
    else:
        return False


def update_password(email: str, password: str) -> None:
    """ updates the password hash in the db for a given username """
    hashed = secrets.hash_password(password)
    update_qry = "UPDATE users SET hash = %s WHERE email = %s"
    print(hashed)
    db.execute_query(update_qry, (hashed, email))


def is_email_unique(email: str) -> bool:
    """ tests if the new email exists in the db """
    unique_query = "SELECT COUNT(*) FROM users WHERE email = %s"
    rs = db.get_rs(unique_query, (email,))
    print("in uniq email")
    print(rs)
    print("after rs")
    if not rs[0]:
        return True
    else:
        return False


def is_user_unique(user_name: str) -> bool:
    """ tests if the new email exists in the db """
    unique_query = "SELECT COUNT(*) FROM users WHERE user_name = %s"
    print("before unique query")
    rs = db.get_rs(unique_query, (user_name,))
    print("rs:")
    print(rs)
    if not rs[0]:
        return True
    else:
        return False


def user_exists(user_name: str):
    """ tests if the user exists in the db """
    return not is_user_unique(user_name)


def get_user(user_name: str) -> User:
    """ gets user from db and loads into an object """
    user_qry = "SELECT user_name, email, email_confirmed, admin, first_name, last_name, user_id FROM users WHERE user_name = %s"
    rs = db.get_rs(user_qry, (user_name,))
    db_user = User(db_user=rs)
    return db_user


def login(user_name, password):
    """ does the login for the givens user and password and returns a success/fail message """
    message = "Invalid username or password"
    if valid_password(user_name, password):
        if user_exists(user_name):
            db_user = get_user(user_name)
            start_session(db_user)
            message = "user successfully logged in"
            return {"error": False, "message": message}
        else:
            return {"error": True, "message": message}
    else:
        return {"error": True, "message": message}


def start_session(user):
    """ loads data from the user into the session vars """
    session["logged_in"] = True
    session["first_name"] = user.first_name
    session["last_name"] = user.last_name
    session["user_name"] = user.user_name
    session["email"] = user.email
    session["user_id"] = user.user_id
    session["admin"] = user.is_admin()
    session["confirmed"] = user.is_confirmed()


def create(form_user):
    email = form_user["email"]
    user_name = form_user["user_name"]
    if is_email_unique(email):
        if is_user_unique(user_name):

            first = form_user["first"]
            last = form_user["last"]
            user_name = form_user["user_name"]

            hashed = secrets.hash_password(form_user["password"])
            nonce = secrets.generate_nonce()
            nonce_time = time.time()

            create_qry = "INSERT INTO users (user_name, email, first_name, last_name, hash, nonce, nonce_timestamp) " \
                         "VALUES ( %s, %s, %s, %s, %s, %s, %s )"

            time_stamp = datetime.datetime.fromtimestamp(nonce_time)

            db.execute_query(create_qry, (user_name, email, first, last, hashed, nonce, time_stamp))
            print("before get_user() in db.create()")
            user = get_user(user_name)
            start_session(user)
            return {"error": False, "message": "Account created."}
        else:
            return {"error": True, "message": "Username is taken."}
    else:
        return {"error": True, "message": "Email is taken."}


def end_session():
    """ clears session data and returns a success message """
    session.clear()
    return {"error": False, "message": "User logged out."}
