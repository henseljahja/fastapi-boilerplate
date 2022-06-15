import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.main_router import router
from app.api.on_start import create_start_app_handler
from app.core.config import API_PREFIX, DEBUG, HOST, PORT, RELOAD

app = FastAPI(
    docs_url=API_PREFIX + "/docs",
    title="Title Goes Here",
    openapi_url=API_PREFIX + "/openapi.json",
    redoc_url=API_PREFIX + "/redoc",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_event_handler("startup", create_start_app_handler(app))

app.include_router(router, prefix=API_PREFIX)
if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host=HOST,
        port=PORT,
        debug=DEBUG,
        reload=RELOAD,
        # **UVICORN_CONFIG
    )
