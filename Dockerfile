FROM python:3.11-bullseye

RUN apt-get update && \
    apt-get update -y && \
    pip install --upgrade pip && \
    curl -sSL https://install.python-poetry.org | python3 - 
    
ENV PATH="${PATH}:/root/.local/bin" \
    POETRY_HOME="/app" \    
    POETRY_VIRTUALENVS_CREATE=false

RUN poetry self update

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry install