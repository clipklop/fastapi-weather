FROM python:3.11

WORKDIR /app

# COPY source dest

EXPOSE 8000

RUN pip install --no-cache-dir --upgrade poetry

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
