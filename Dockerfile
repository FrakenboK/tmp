FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN curl -sSL https://install.python-poetry.org | python3 - 

ENV PATH="/root/.local/bin:$PATH"
WORKDIR /app

COPY pyproject.toml .

RUN poetry config virtualenvs.create false 
RUN poetry install --no-root
RUN mkdir -p /data

ADD fastapi_app .
ADD entry.sh .

CMD ["/bin/sh", "entry.sh"]