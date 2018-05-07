import os


_basedir = os.path.abspath(os.path.dirname(__file__))


# Creates the default Config Object
class Config(object):
    # APP Settings
    TITLE = "XRoads"
    DEBUG = False
    TESTING = False

    SECRET_KEY = "testing_secret_key"

    # Database Config
    MYSQL_HOST = "localhost"
    MYSQL_PORT = "3306"
    MYSQL_USER = "xroads_user"
    MYSQL_PASSWORD = os.getenv("XROADS_PASSWORD")
    MYSQL_DB = "xroads"
    MYSQL_TEMPLATE = "mysql://{}:{}@{}:{}/{}"

    MYSQL_CONN = MYSQL_TEMPLATE.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)

    # Email Config
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv("XROADS_MAIL_USER")
    MAIL_PASSWORD = os.getenv("XROADS_MAIL_PWORD")
    MAIL_DEFAULT_SENDER = "XRoadsServer"


# Overrides the default Config Object for Production
class ProductionConfig(Config):
    MYSQL_HOST = "change to production value"
    pass


# Overrides the default Config Object for Development
class DevelopmentConfig(Config):
    DEBUG = True
    # DATABASE_URI = os.path.join(_basedir, "XRoad.db")
    pass


# Overrides the default Config Object for Testing
class TestingConfig(Config):
    TESTING = True

    # database configuration
    MYSQL_DB = "xroads_test"
    pass


del os
