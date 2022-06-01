# Local application imports
import os

from app import create_app
from app.adapters import MsgBroker
from app.config import DevelopmentConfig, ProductionConfig, TestingConfig

# from waitress import serve

# create settings object corresponding to specified env
APP_ENV = os.environ.get("APP_ENV", "ProductionConfig")
app = create_app(APP_ENV)

loMsgBroker = MsgBroker()


@app.route("/")
def hello():
    return {"DATA": "Hello from API!"}


@app.before_request
def before_request_message():
    """
    Log request into message broker and assing processID
    """
    loMsgBroker.publish_msg()
    pass


@app.after_request
def after_request_message(response):
    """
    Add response to ProcessID
    """
    loMsgBroker.response_msg()
    return response


if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    app.run(port=app.config["APP_PORT"])
    # serve(app, host="0.0.0.0", port=app.config["APP_PORT"])
