# Local application imports
from app import create_app
from app.config import DevelopmentConfig, ProductionConfig, TestingConfig
from waitress import serve

app = create_app()


@app.route("/")
def hello():
    return {"DATA": "Hello from API!"}


if __name__ == "__main__":
    # app.run(port=app.config["APP_PORT"])
    serve(app, host="0.0.0.0", port=app.config["APP_PORT"])
