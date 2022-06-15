from typing import Generator

from sqlalchemy.orm import Session, sessionmaker

from app.db.engine import ENGINE

SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)


def get_session() -> Generator:
    try:
        db = SessionMaker()
        yield db
    finally:
        db.close()
