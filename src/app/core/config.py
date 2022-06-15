import os
from pathlib import Path
from urllib.parse import quote

from starlette.config import Config
from starlette.datastructures import Secret

config = Config(f"{Path(__file__).resolve().parents[2]}/.env")

API_PREFIX: str = config("API_PREFIX", cast=str, default="/v1")
DEBUG: bool = config("DEBUG", cast=bool, default=True)
DEBUG: bool = config("DEBUG", cast=bool, default=False)
RELOAD: bool = config("RELOAD", cast=bool, default=False)
PORT: int = config("PORT", cast=int, default=8080)
LOG_LEVEL = config("LOG_LEVEL", cast=str, default="INFO")
LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
LOGGER_NAME: str = "main"
HOST: str = config("HOST", cast=str, default="localhost")

POSTGRES_DB: str = config("POSTGRES_DB", cast=str, default="postgresql")
POSTGRES_USERNAME: str = config(
    "POSTGRES_USERNAME", cast=str, default="hensel"
)
POSTGRES_PASSWORD: str = config(
    "POSTGRES_PASSWORD", cast=str, default="wXyz0909!"
)
if POSTGRES_USERNAME == "dbmon":
    POSTGRES_PASSWORD = quote(POSTGRES_PASSWORD)
POSTGRES_HOST: str = config(
    "POSTGRES_HOST",
    cast=str,
    default="127.0.0.1",
)
POSTGRES_PORT: str = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DATABASE: str = config(
    "POSTGRES_DATABASE", cast=str, default="postgres"
)
POSTGRES_SCHEMA: str = config("POSTGRES_SCHEMA", cast=str, default="mlc")

# FULL URL
# postgresql://hensel:wXyz0909!@localhost:5432/chatbot
# postgresql://dbmon:FinaryaMtiCloud1234%23%40%21@
# pgm-d9j5ee4o3804z68r7o.pgsql.ap-southeast-5.rds.aliyuncs.com:3433/dev_web_admin
POSTGRES_DATABASE_URL: str = config(
    "POSTGRES_DATABASE_URL",
    cast=str,
    default=POSTGRES_DB
    + "://"
    + POSTGRES_USERNAME
    + ":"
    + POSTGRES_PASSWORD
    + "@"
    + POSTGRES_HOST
    + ":"
    + POSTGRES_PORT
    + "/"
    + POSTGRES_DATABASE,
)

INIT_DB: bool = config("INIT_DB", cast=bool, default=False)
INIT_DATA: bool = config("INIT_DATA", cast=bool, default=False)
DROP_TABLES: bool = config("DROP_TABLES", cast=bool, default=False)
