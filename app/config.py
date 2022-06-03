import os
APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.split(APP_DIR)[0]
ROOT_DIR = os.path.split(PROJECT_DIR)[0]
ROUTES_DIR = APP_DIR + "\\routes"
DOMAIN_DIR = APP_DIR + "\\domain"
LOG_FILE = PROJECT_DIR + "\\log\\api_server.log"
PATH_PDF_SRC = APP_DIR + "\\PDF\\assets"
PATH_FILE = "\\var\\Docs\\PACIENTE"
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "csv"}
MAX_CONTENT_LENGTH = 16000

APP_PORT = "4000"
API_URL = "http://127.0.0.1:4000"
SECURE = True
SECRET_KEY = "BatmanisBruceWayne"

PSQL_DB="ALIVIARI"
PSQL_BD_PORT="5434"
PSQL_DB_USER="postgres"
PSQL_DB_PASSWORD="postgres"
PSQL_MIGRATE_DB_CONECTION = (
    "host=localhost dbname=postgres user="+PSQL_DB_USER+" password="+PSQL_DB_PASSWORD+" port="+PSQL_BD_PORT
)
PSQL_DB_CONECTION_PSQL = (
    "host=localhost dbname="+PSQL_DB+" user="+PSQL_DB_USER+" password="+PSQL_DB_PASSWORD+" port="+PSQL_BD_PORT
    )