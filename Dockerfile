FROM python:3.12

WORKDIR /app

# Copia README e arquivos do Poetry
COPY README.md .
COPY volunteer_management/pyproject.toml volunteer_management/poetry.lock ./volunteer_management/

# Instala Poetry
RUN pip install --no-cache-dir poetry

# Instala dependências (sem instalar o projeto, evita problema de README)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copia todo o código
COPY volunteer_management/ ./volunteer_management/

EXPOSE 8000

CMD ["uvicorn", "volunteer_management.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]