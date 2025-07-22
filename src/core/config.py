from dotenv import load_dotenv
import os

load_dotenv()  

class Config:
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_DATABASE = os.getenv("DB_DATABASE")
    DB_PORT = os.getenv("DB_PORT")
    SECRET_KEY = os.getenv("SECRET_KEY")
    PORT_SERVER = os.getenv("PORT_SERVER")
    SALT = os.getenv("SALT")
    HTTP_ONLY = os.getenv("HTTP_ONLY", "True") == "True"
    AVAILABLE_DOMAINS = os.getenv("AVAILABLE_DOMAINS")

config = Config()
