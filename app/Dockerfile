FROM python:3.12-slim-bookworm
WORKDIR /app

COPY requirements.txt .
COPY firebase.json .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "app.py"]
