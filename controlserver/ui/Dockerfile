# Use official Python image
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install flask requests

CMD ["python", "server.py"]
