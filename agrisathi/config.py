import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-this")

    # MySQL connection settings — edit these to match your local setup
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "Harsh3930")
    MYSQL_DB = os.environ.get("MYSQL_DB", "agridb")
