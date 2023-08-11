FROM python:3.10-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY . .

RUN pip install poetry && poetry install

CMD ["python", "src/index.py"]
