from flask import Blueprint, render_template, redirect, url_for
import XRoadsServer.utils.mailer.mailer as email

mod = Blueprint('home', __name__)


@mod.route('/')
def index():
    return render_template("home/home.html")


@mod.route('/create')
def temp_create():
    return render_template("home/temp_create.html")


@mod.route('/login')
def temp_login():
    return render_template("home/temp_login.html")


@mod.route('/test/email')
def test_email():
    # email.send_test()
    # email.new_test()
    email.send_confirmation("asouer@gmail.com", "test_nonce")
    return redirect(url_for("home.index"))



