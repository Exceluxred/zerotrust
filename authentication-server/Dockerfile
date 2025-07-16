FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install flask flask-cors pyjwt

CMD ["python", "auth_server.py"]