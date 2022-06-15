from sqlalchemy import create_engine

from app.core.config import POSTGRES_DATABASE_URL, POSTGRES_SCHEMA

ENGINE = create_engine(
    POSTGRES_DATABASE_URL,
    echo=True,
    connect_args={"options": "-csearch_path={}".format(POSTGRES_SCHEMA)},
)
