FROM alpine:3.14
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./app.py
