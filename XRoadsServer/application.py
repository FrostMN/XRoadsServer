from flask import Flask
from typing import Union
from XRoadsServer.enums.Ranks import Rank
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)


def get_rank_name(number: Union[int, str]):
    if isinstance(number, str):
        number = int(number)

    return Rank(number + 1).name


# app.add_template_filter(Rank)
app.jinja_env.filters['rank'] = get_rank_name

