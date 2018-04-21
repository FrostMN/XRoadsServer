from flask import Blueprint, render_template

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


