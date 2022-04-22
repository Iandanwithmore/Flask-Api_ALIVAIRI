import os

# Find the absolute file path to the top level project directory
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    SECURE = True
    SECRET_KEY = "BatmanisBruceWayne"
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_DIR = os.path.split(APP_DIR)[0]
    ROOT_DIR = os.path.split(PROJECT_DIR)[0]

    LOG_FILE = PROJECT_DIR + "/log/api_server.log"
    PATH_PDF_SRC = APP_DIR + "/PDF/assets"
    PATH_FILE = "C:/xampp/htdocs/CLANAD/Docs/PACIENTE"

    ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "csv"}
    MAX_CONTENT_LENGTH = 16000

    API_CONECTION = (
        "host=localhost dbname=ALIVIARI user=postgres password=postgres port=5434"
    )
    APP_PORT = "4000"
    API_URL = "http://127.0.0.1:4000"


class ProductionConfig(Config):
    FLASK_ENV = "Production"
    pass


class DevelopmentConfig(Config):
    FLASK_ENV = "Develop"
    DEBUG = True
    SECURE = False


class TestingConfig(Config):
    FLASK_ENV = "Test"
    TESTING = True
    SECURE = False
