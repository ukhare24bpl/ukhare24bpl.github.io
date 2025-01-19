from flask import Flask, request, render_template
import mysql.connector
from werkzeug.security import check_password_hash
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1111",
    database="authentication"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/login', methods=[ 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        l="select password from users where username ="+"'"+username+"'"+";"
        mycursor.execute(l)
        for i in mycursor:
            c=i[0]
            if password==c:
                return render_template('dashboard.html')
            else:
                return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
