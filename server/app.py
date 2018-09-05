import os
from flask import Flask
from . config import config_env_files

def register_blueprints(app):
    from . views import root
    app.register_blueprint(root)

def create_app(default_config='dev'):
    app = Flask(__name__, static_url_path='')

    app.config.from_object(
        config_env_files.get(os.getenv('APP_SETTINGS', default_config))
    )
    app.secret_key = app.config['SECRET_KEY']

    for f in [register_blueprints]:
        f(app)
    return app
