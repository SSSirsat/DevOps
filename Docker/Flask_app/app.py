from flask import Flask, render_template
import os

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

if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port=port)
