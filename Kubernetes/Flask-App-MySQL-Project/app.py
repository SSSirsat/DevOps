from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"]= '192.168.59.100'
app.config["MYSQL_USER"]= 'root'
app.config["MYSQL_PASSWORD"]= 'test1234'
app.config["MYSQL_DB"]= 'mydatabase'

mysql = MySQL(app)
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/adddata', methods =["GET", "POST"])
def adata():
    if request.method == "POST":
        personid = request.form.get("id")
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        city = request.form.get("cname")
        cur = mysql.connection.cursor()
        # cur.execute("CREATE TABLE PERSONS(personid int,fname varchar(10),lname varchar(10),city varchar(10)")
        cur.execute("INSERT INTO persons(personid,fname,lname,city) VALUES(%s,%s,%s,%s)", (personid, first_name, last_name, city))
        mysql.connection.commit()
        cur.close()
        return render_template("success.html")
        # return "Your name is " + first_name + last_name + "Your Data in Inserted into the MYSQL Database."
    return render_template("form.html")

@app.route('/getdata',methods=['GET', "POST"])
def gdata():
    # try:
    if request.method == "POST":
        id = request.form.get("id")
        cur = mysql.connection.cursor()
        sql_select_query = f"""select * from persons where personid = {id}"""
        cur.execute(sql_select_query)
        record = cur.fetchall()
        id = str(record[0][0])
        fname = record[0][1]
        lname = record[0][2]
        cname = record[0][3]
        return f"<h1> Name of person is {fname} {lname} of city {cname} having Id {id}"
    return render_template("details.html")

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True,host="0.0.0.0", port=int("3000"))

