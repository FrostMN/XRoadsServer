from XRoadsServer.application import app
from flask import render_template
from flask_api import status

from XRoadsServer.views import home
from XRoadsServer.views import users
from XRoadsServer.views import mobile
from XRoadsServer.views import game
from XRoadsServer.views import admin

# register blueprints
app.register_blueprint(home.mod)
app.register_blueprint(users.mod, url_prefix='/user')
app.register_blueprint(mobile.mod, url_prefix='/mobile')
app.register_blueprint(game.mod, url_prefix='/game')
app.register_blueprint(admin.mod, url_prefix='/admin')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', error=e), status.HTTP_404_NOT_FOUND


if __name__ == '__main__':
    # app.config["DEBUG"] = False
    # app.run(host="0.0.0.0")
    app.run()
