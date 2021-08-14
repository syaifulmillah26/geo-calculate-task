import os
from flask import Flask
from logging import getLogger

from app.tools.blueprints import discover_blueprints
from app.config import Config

error_logger = getLogger("error")


def create_app(test: bool = False) -> Flask:
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    blueprints = discover_blueprints(
        os.path.dirname(os.path.abspath(__file__)))
    with app.app_context():
        for blueprint in blueprints:
            try:
                app.register_blueprint(blueprint)
            except Exception as e:
                error_logger.error(
                    f"Failed to register blueprint {blueprint}: {e}")

    return app


app = create_app()


def getenv(value, key):
    return os.getenv(key, value)


app.jinja_env.filters['getenv'] = getenv
