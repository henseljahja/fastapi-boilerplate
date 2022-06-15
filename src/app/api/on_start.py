from typing import Any, Callable, Coroutine

from app.core.config import DROP_TABLES, INIT_DATA, INIT_DB
from app.db import init_db
from app.db.session import SessionMaker
from fastapi import FastAPI


def create_start_app_handler(
    app: FastAPI,
) -> Callable[[], Coroutine[Any, Any, None]]:
    async def start_app() -> None:
        if DROP_TABLES:
            init_db.drop_tables(SessionMaker)
        if INIT_DB:
            init_db.create_database(SessionMaker)
        if INIT_DATA:
            init_db.init_data()

    return start_app
