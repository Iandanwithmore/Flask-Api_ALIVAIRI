import importlib.util
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import json

from flask import Flask, has_request_context, request

# Standard library imports
from .config import Config

# from logging.handlers import SMTPHandler


def create_app():
    app = Flask(__name__)

    register_blueprints(app)

    app.config.from_object(Config)
    print(f"ENV is set to:\n   {json.dumps(app.config, indent=3, sort_keys=True)}")
    app.secret_key = Config["SECRET_KEY"]

    class RequestFormatter(logging.Formatter):
        def format(self, record):
            if has_request_context():
                record.url = request.url
                record.remote_addr = request.remote_addr
            else:
                record.url = None
                record.remote_addr = None
            return super().format(record)

    formatter = RequestFormatter(
        "{'TIME':%(asctime)s,'ADDRESS':'%(remote_addr)s','URL': '%(url)s','TYPE':'%(levelname)s','MODULE':'%(module)s','MSG':{%(message)s}}"
    )
    handler = TimedRotatingFileHandler(
        Config["LOG_FILE"], when="midnight", interval=1, encoding="utf8"
    )
    handler.suffix = "%Y-%m-%d"
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    return app


def register_blueprints(app, dir):
    try:
        route_dir = os.listdir(Config["ROUTES_DIR"])
    except OSError:
        print("NO SE PUDIERON CARGAR LAS BLUEPRINTS")
    else:
        for route in route_dir:
            if route != "__pycache__":
                name_class = route.split(".py")[0]
                module = importlib.import_module("app." + dir + "." + name_class)
                app.register_blueprint(getattr(module, name_class))
