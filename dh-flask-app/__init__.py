from flask import Flask
from .extensions import db
from .commands import createDb,dropDB
from .routes import dhApp

def create_app(config_file="settings.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    app.cli.add_command(createDb)
    app.cli.add_command(dropDB)
    app.register_blueprint(dhApp)
    return app