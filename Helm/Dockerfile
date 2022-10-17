FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV FLASK_RUN_HOST=0.0.0.0
COPY src src
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT [ "python","./src/app.py" ]


# FROM python:3.10-alpine
# WORKDIR /app
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_ENV = development
# COPY requirements.txt requirement.txt
# RUN pip install -r requirement.txt
# COPY . .
# CMD ["python","./src/app.py"]
