# Aug 21 session
from flask import Flask, request, jsonify
import __mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host="localhost", user='root', passwd="Jaijai1@11")
cursor = mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable (name varchar(30) , number int)")


@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get("mail_id")
    return "this is my 1st function for get {} {} {}".format(get_name, mobile_number, mail_id)


@app.route('/get_data')
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con = conn.connect(host="localhost", user="root", password="Jaijai1@11", database=db)
        cur = con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)


# http://127.0.0.1:5003/testfun?get_name=arpit%20shah&mobile=1234&mail_id=abc
if __name__ == '__main__':
    app.run(debug=True, port=5003)
