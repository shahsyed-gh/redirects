FROM python:3.11-slim

WORKDIR /app

COPY app.py .
COPY static/ static/

RUN pip install flask

EXPOSE 8080

CMD ["python", "-m", "flask", "--app", "app", "run", "--host", "0.0.0.0", "--port", "8080"]