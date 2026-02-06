FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip \
    && pip config set global.timeout 120 \
    && pip config set global.retries 10 \
    && pip config set global.progress_bar off

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

