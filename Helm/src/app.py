from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

@app.route("/")
def user():
    return render_template("index.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/details")
def details():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return render_template("details.html", HOSTNAME=hostname,IP=ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
