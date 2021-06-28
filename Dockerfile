FROM python:3.9-slim
RUN pip install poetry

COPY ./pyproject.toml .
COPY ./poetry.lock .


RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi


COPY . .

ENTRYPOINT [ "python","manage.py","runserver","" ]
