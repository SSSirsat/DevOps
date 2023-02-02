# Dockerfile , Image , Container
FROM python:3.9-slim-buster
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt
CMD ["python","/app/app.py"]
EXPOSE 5000





