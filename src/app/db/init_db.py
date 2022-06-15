import os
from typing import Any

from app.core.config import INIT_SQL_FILE_PATH
from app.db.base import Base
from app.db.engine import ENGINE
from sqlalchemy import text
from sqlalchemy.orm import Session, sessionmaker


def create_database(db: Session) -> None:
    Base.metadata.create_all(bind=ENGINE)
    print("database created")
    with Session(ENGINE) as session:
        try:
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
            raise
        finally:
            session.close()


def execute_sql_scripts(filename: str, ENGINE: Any) -> None:
    if filename.endswith(".sql"):
        try:
            sql_file = open(filename, "r")
            escaped_sql = text(sql_file.read())
            with Session(ENGINE) as session:
                try:
                    session.execute(escaped_sql)
                    session.commit()
                except Exception as e:
                    print(e)
                    session.rollback()
                    raise
                finally:
                    session.close()
            sql_file.close()

        except Exception as e:
            print(e)
            print("Error: failed to execute sql file: " + filename)


def init_data() -> None:
    for sql_file in os.listdir(INIT_SQL_FILE_PATH):
        execute_sql_scripts(os.path.join(INIT_SQL_FILE_PATH, sql_file), ENGINE)


def drop_tables(db: sessionmaker) -> None:
    Base.metadata.drop_all(bind=ENGINE)
