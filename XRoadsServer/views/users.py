from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from XRoadsServer.utils import valid
import XRoadsServer.utils.database.users as db_users

mod = Blueprint('users', __name__)


@mod.route('/')
def user():
    return render_template("users/users.html")


@mod.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        if valid.new_user(request.form):
            email = request.form["email"]
            print(email)
            user_name = request.form["user_name"]
            print(user_name)
            if db_users.is_email_unique(email) and \
               db_users.is_user_unique(user_name):
                print("before db_users.create")

                create_message = db_users.create(request.form)
                print(create_message)
                if create_message["error"]:
                    flash(create_message["message"], "error")
                else:
                    flash(create_message["message"], "message")
            return redirect(url_for("home.index"))
        else:
            message = {"error": True, "message": "Missing data in form"}
            flash(message)
            return redirect(url_for("home.index"))
    else:
        message = {"error": True, "message": "Method not allowed"}
        flash(message)
        return redirect(url_for("home.index"))


@mod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        r_data = request.form
        if "user" in r_data.keys() and r_data["user"] != "" and \
           "password" in r_data.keys() and r_data["password"] != "":
            print(r_data["user"])
            print(r_data["password"])
            message = db_users.login(r_data["user"], r_data["password"])
            print(message)
            flash(message)
            return redirect(url_for("home.index"))
        else:
            print("redirecting")
            return redirect(url_for("home.index"))
    else:
        return redirect(url_for("home.index"))


@mod.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == "POST":
        message = db_users.end_session()
        flash(message)
        return redirect(url_for("home.index"))
    else:
        message = db_users.end_session()
        flash(message)
        return redirect(url_for("home.index"))

