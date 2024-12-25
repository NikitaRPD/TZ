ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim-bullseye as base
ENV PYTHONUNBUFFERED 1
ARG PIP_EXTRA_INDEX_URL
ARG POETRY_VERSION=1.8.2

RUN mkdir -p /code/
WORKDIR /code/


RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get upgrade -y
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install poetry==${POETRY_VERSION}

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.* /code/

# Таргет для разработки, включающий dev зависимости
FROM base AS development

RUN poetry install --no-interaction --no-ansi --with dev -vvv

COPY . /code/

CMD uvicorn src.main:app --host 0.0.0.0 --port=8080 --workers=4 --app-dir src

# Основной таргет, устанавливающий только необходимые зависимости
FROM base AS production

RUN poetry install --no-interaction --no-ansi --only main -vvv

COPY . /code/

CMD uvicorn src.main:app --host 0.0.0.0 --port=8080 --workers=4 --app-dir src