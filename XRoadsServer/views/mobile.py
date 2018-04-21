from flask import Blueprint, request, redirect, url_for, jsonify
from flask_api import status

mod = Blueprint('mobile', __name__)


@mod.route('/')
def mobile():
    return redirect(url_for("home.index"))


@mod.route('/login', methods=['GET', 'POST'])
def mobile_login():
    if request.method == "POST":
        return ""
    else:
        return jsonify({"errors": True, "message": "Method not allowed"}), status.HTTP_405_METHOD_NOT_ALLOWED


@mod.route('/logout', methods=['GET', 'POST'])
def mobile_logout():
    if request.method == "POST":
        return ""
    else:
        return jsonify({"errors": True, "message": "Method not allowed"}), status.HTTP_405_METHOD_NOT_ALLOWED
