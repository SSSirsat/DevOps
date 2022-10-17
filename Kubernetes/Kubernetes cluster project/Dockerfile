# Dockerfile , Image , Container
FROM python:3.9-slim-buster
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV = development
COPY requirements.txt requirement.txt
RUN pip install -r requirement.txt
COPY . .
CMD ["flask","run"]



