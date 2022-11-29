from flask import Flask, render_template
# from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"]= 'localhost'
app.config["MYSQL_USER"]= 'root'
app.config["MYSQL_PASSWORD"]= 'root'
app.config["MYSQL_DB"]= 'shuubham1'

from flaskext.mysql import MySQL
mysql = MySQL()
mysql.init_app(app)
cursor = mysql.get_db().cursor()

@app.route("/")
def user():
    fname="Shubham"
    lname="Sirsat"
    cur = mysql.connection.curser()
    cur.execute("INSERT INTO user(id, Name) VALUES(%s %s)", (fname,lname))
    mysql.connection.commit()
    cur.close()
    return "Success"

if __name__ == '__main__':
    app.run(debug=True)
