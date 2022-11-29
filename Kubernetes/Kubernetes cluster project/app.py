from flask import Flask, render_template
import socket
import os

app = Flask(__name__)

@app.route("/")
def user():
    return render_template("index.html")

@app.route("/about")
def ipfind():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return render_template("about.html", IP=IPAddr, HNAME=hostname)

if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port=port)

