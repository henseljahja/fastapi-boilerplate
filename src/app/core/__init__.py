import os
from pathlib import Path
from urllib.parse import quote

from starlette.config import Config
from starlette.datastructures import Secret

config = Config(f"{Path(__file__).resolve().parents[2]}/.env")
print(f"{Path(__file__).resolve().parents[2]}/.env")
API_PREFIX: str = config("API_PREFIX", cast=str, default="/v1")
DEBUG: bool = config("DEBUG", cast=bool, default=True)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default=os.urandom(32))
POSTGRES_DB: str = config("POSTGRES_DB", cast=str, default="postgresql")
POSTGRES_USERNAME: str = config("POSTGRES_USERNAME", cast=str, default="hensel")
POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD", cast=str, default="wXyz0909!")
if POSTGRES_USERNAME == "dbmon":
    POSTGRES_PASSWORD = quote(POSTGRES_PASSWORD)
POSTGRES_HOST: str = config(
    "POSTGRES_HOST", cast=str, default="127.0.0.1",
)
POSTGRES_PORT: str = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DATABASE: str = config("POSTGRES_DATABASE", cast=str, default="chatbot")
POSTGRES_SCHEMA: str = config("POSTGRES_SCHEMA", cast=str, default="chatbot")

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

"""MODEL NAME"""
MODEL_NAME = "DASHBOARD"

"""
ADD FILES DIRECTORY TO CONFIG
"""
"""CURRENT DIRECTORY"""
CURRENT_DIRECTORY = os.path.dirname(Path(__file__).resolve().parents[0])
"""DATA PATH"""
DATA_PATH = os.path.join(CURRENT_DIRECTORY, "resources/data_chatbot")

"""CONFIG YML FILE"""
CONFIG_FILE = "resources/data_chatbot/conf/config.yml"
CONFIG_FILE_PATH = os.path.join(CURRENT_DIRECTORY, CONFIG_FILE)

"""CREDENTIALS YML FILE"""
CREDENTIALS_FILE = "resources/data_chatbot/conf/credentials.yml"
CREDENTIALS_FILE_PATH = os.path.join(CURRENT_DIRECTORY, CREDENTIALS_FILE)

"""DOMAIN YML FILE"""
DOMAIN_FILE = "resources/data_chatbot/conf/domain.yml"
DOMAIN_FILE_PATH = os.path.join(CURRENT_DIRECTORY, DOMAIN_FILE)

"""ENDPOINTS YML FILE"""
ENDPOINTS_FILE = "resources/data_chatbot/conf/v1.yml"
ENDPOINTS_FILE_PATH = os.path.join(CURRENT_DIRECTORY, ENDPOINTS_FILE)

"""NLU YML FILE"""
NLU_FILE = "resources/data_chatbot/data/nlu.yml"
NLU_FILE_PATH = os.path.join(CURRENT_DIRECTORY, NLU_FILE)

"""RULES YML FILE"""
RULES_FILE = "resources/data_chatbot/data/rules.yml"
RULES_FILE_PATH = os.path.join(CURRENT_DIRECTORY, RULES_FILE)

"""STORIES YML FILE"""
STORIES_FILE = "resources/data_chatbot/data/stories.yml"
STORIES_FILE_PATH = os.path.join(CURRENT_DIRECTORY, STORIES_FILE)

"""INIT SQL FILES"""
INIT_SQL_FILE = "resources/sql/init_data"
INIT_SQL_FILE_PATH = os.path.join(CURRENT_DIRECTORY, INIT_SQL_FILE)

"""QUERIES SQL FILES"""
QUERIES_SQL_FILE = "resources/sql/queries_data"
QUERIES_SQL_FILE_PATH = os.path.join(CURRENT_DIRECTORY, QUERIES_SQL_FILE)

"""TRAINING SCRIPT"""
TRAINING_SCRIPT = "resources/scripts/train.sh"
TRAINING_SCRIPT_PATH = os.path.join(CURRENT_DIRECTORY, TRAINING_SCRIPT)

"""MODEL PATH LOCAL"""
MODEL_FILE = "/resources/models"
MODEL_FILE_PATH = os.path.join(CURRENT_DIRECTORY, MODEL_FILE)

DATETIME_FORMAT = "%Y_%m_%d_%H_%M"
