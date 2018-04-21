from flask import Flask
import config
# from XRoadsServer.views import home
# from XRoadsServer.views import user
# from XRoadsServer.views import mobile

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

# register blueprints
# app.register_blueprint(home.mod)
# app.register_blueprint(user.mod, url_prefix='/user')
# app.register_blueprint(mobile.mod, url_prefix='/mobile')

