from flask import Blueprint, render_template, redirect, url_for
import XRoadsServer.utils.mailer.mailer as email

mod = Blueprint('home', __name__)


@mod.route('/')
def index():
    return render_template("home/home.html")
