FROM python:3.12


WORKDIR /app


COPY pyproject.toml poetry.lock ./


RUN pip install --no-cache-dir poetry


RUN poetry install --no-root --only main


COPY volunteer_management/ ./volunteer_management/


EXPOSE 8000


CMD ["poetry", "run", "uvicorn", "volunteer_management.main:app", "--host", "0.0.0.0", "--port", "8000"]