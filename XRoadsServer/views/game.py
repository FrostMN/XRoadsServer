from flask import Blueprint, request, redirect, url_for, jsonify, render_template
from flask_api import status

mod = Blueprint('game', __name__)


@mod.route('/')
def mobile():
    return render_template('game/game.html')
