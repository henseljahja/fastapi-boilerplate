FROM python:3.10-slim

RUN pip install --upgrade pip
RUN pip install poetry==1.1.8

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.0

WORKDIR /code

COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
    && poetry install

COPY . /code

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

EXPOSE 8000

CMD ./run.sh
