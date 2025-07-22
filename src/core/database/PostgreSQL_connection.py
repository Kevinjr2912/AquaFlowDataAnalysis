from databases import Database
from ..config import config

DATABASE_URL = f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_DATABASE}"

database_conn = Database(DATABASE_URL)
