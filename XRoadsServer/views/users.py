from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
# from XRoadsServer.utils.secrets import users as user
from XRoadsServer.utils import valid
import XRoadsServer.utils.database.users as db_users
from XRoadsServer.models.Character import Character, db_class
from XRoadsServer.enums.Ranks import Rank

mod = Blueprint('users', __name__)


@mod.route('/')
def user():
    if "logged_in" in session.keys():
        if session["logged_in"]:
            print(session)
            chars = db_users.get_characters(session["user_id"])
            level_up = 0
            for c in chars:
                if c.can_rank_up:
                    level_up += 1
            return render_template("users/users.html", characters=chars, level_up=level_up)
        else:
            return redirect(url_for("home.index"))
    else:
        return redirect(url_for("home.index"))


# @user.logged_in
@mod.route('/add/char', methods=['GET', 'POST'])
def add_char():
    if request.method == "POST":
        user_id = session["user_id"]
        char_name = request.form["name"]
        char_background = request.form["background"]

        new_char_args = (user_id, char_name, char_background)

        db_users.add_character(new_char_args)

        return redirect(url_for("users.user"))
    else:
        message = {"error": True, "message": "Method not allowed"}
        flash(message)
        return redirect(url_for("users.user"))


@mod.route('/delete/char/', methods=['GET', 'POST'])
def delete_char():
    if request.method == "POST":
        # TODO: Need to validate user owns char id
        char_id = request.form["char_id"]

        message = db_users.delete_char(char_id)
        flash(message["message"])

        return redirect(url_for("users.user"))
    else:
        return redirect(url_for("users.user"))


# @user.logged_in
@mod.route('/edit/char', methods=['GET', 'POST'])
def edit_char():
    admin = False
    print("/user/edit/char")
    print(request.form)
    if request.method == "POST":
        char_id = request.form["char_id"]

        print(char_id)

        character = db_users.get_character_by_id(char_id)

        if "name" in request.form.keys():
            char_name = request.form["name"]
            character.set_character_name(char_name)

        if "rank" in request.form.keys():
            rank_to = request.form["rank"]
            character.set_rank_to(rank_to)

        if "admin" in request.form.keys():
            if request.form["admin"] == 'true':
                admin = True
            else:
                admin = False

        print(character.character_name)

        db_users.update_character(character)
        if admin:
            return redirect(url_for("admin.admin"))
        else:
            return redirect(url_for("users.user"))
    else:
        message = {"error": True, "message": "Method not allowed"}
        flash(message)
        return redirect(url_for("users.user"))


@mod.route('/level/char', methods=['GET', 'POST'])
def level_char():
    if request.method == "POST":
        char_id = request.form["character_id"]
        char = db_users.get_character_by_id(char_id)

        rank = char.rank_value

        if rank > 0:
            char.add_ability(Rank(char.rank_value + 1).name, request.form["ability"])
            char.rank_up()

        if rank == 0:
            char_class = request.form["character_class"]
            char.set_character_class(db_class(char_class))
            char.rank_up()

        db_users.update_character(char)
        return redirect(url_for("users.user"))
    else:
        return redirect(url_for("users.user"))


@mod.route('/edit/password', methods=['GET', 'POST'])
def edit_password():
    if request.method == "POST":
        if request.form["new_password"] == request.form["new_password"]:
            db_users.update_password(session["email"], request.form["new_password"])
            return redirect(url_for("users.logout"))
        else:
            return redirect(url_for("users.user"))
    else:
        return redirect(url_for("users.user"))


@mod.route('/edit/email', methods=['GET', 'POST'])
def edit_email():
    if request.method == "POST":
        if valid.email(request.form["new_email"]):
            message = db_users.update_email(request.form["new_email"], session["email"])
            if message["error"]:
                flash(message["message"])
                return redirect(url_for("users.user"))
            else:
                flash(message["message"])
                return redirect(url_for("users.user") + "#profile")
        else:
            return redirect(url_for("users.user"))
    else:
        return redirect(url_for("users.user"))


@mod.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        if valid.new_user(request.form):
            email = request.form["email"]
            # print(email)
            user_name = request.form["user_name"]
            # print(user_name)
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
            message = db_users.login(r_data["user"], r_data["password"])
            flash(message["message"])
            return redirect(url_for("users.user"))
        else:
            return redirect(url_for("home.index"))
    else:
        return redirect(url_for("home.index"))


@mod.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == "POST":
        message = db_users.end_session()
        flash(message["message"])
        return redirect(url_for("home.index"))
    else:
        message = db_users.end_session()
        flash(message["message"])
        return redirect(url_for("home.index"))


@mod.route('/edit/user', methods=['GET', 'POST'])
def edit_user():
    if request.method == "POST":
        print(request.form)

        db_user = db_users.get_user_by_id(request.form["user_id"])

        if "admin" in request.form.keys():
            db_user.set_admin(request.form["admin"])
        if "verified" in request.form.keys():
            db_user.set_verified(request.form["verified"])
        if "banned" in request.form.keys():
            db_user.set_banned(request.form["banned"])

        db_users.update_user(db_user)

        return redirect(url_for("admin.admin"))
    else:
        return redirect(url_for("home.index"))


@mod.route('/validate/<nonce>', methods=['GET', 'POST'])
def validate(nonce: str):
    if request.method == "GET":
        email_user = db_users.get_user_by_nonce(str(nonce))
        if email_user:
            db_users.validate_email(email_user.email, email_user.temp_email)
            return redirect(url_for("users.user") + "#profile")
        else:
            return redirect(url_for("users.user"))
    else:
        return redirect(url_for("home.index"))


@mod.route('/validate/resend', methods=['GET', 'POST'])
def resend_confirm():
    if request.method == "POST":
        # TODO: resend validation email
        return redirect(url_for("users.user"))
    else:
        return redirect(url_for("home.index"))

