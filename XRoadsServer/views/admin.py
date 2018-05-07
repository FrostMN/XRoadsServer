from flask import Blueprint, render_template, session, redirect
import XRoadsServer.utils.database.users as db_users

mod = Blueprint('admin', __name__)


@mod.route('/')
def admin():
    if "logged_in" in session.keys() and "admin" in session.keys():
        if session["logged_in"] and session["admin"]:
            players = db_users.get_players()
            return render_template("admin/admin.html", players=players)
        else:
            return redirect("users/user.html")
    else:
        return redirect("home/index.html")
