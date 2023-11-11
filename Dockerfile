ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION} as requirements-stage

WORKDIR /tmp
 
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:${PYTHON_VERSION} as base


# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

EXPOSE 8000

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
