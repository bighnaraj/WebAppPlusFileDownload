from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy import func
from werkzeug import secure_filename

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:myPassword@localhost/postgres'
#"dbname='postgres' user='postgres' password='myPassword' host='localhost'"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fswzgdbjdfceuf:97c19bf1a69c8a6d4fa8b5baa946ad3591b9de7718d921417addcd4c3511e9de@ec2-23-23-216-40.compute-1.amazonaws.com:5432/d3anqp0rh697k7?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120),unique=True)
    height = db.Column(db.Integer)

    def __init__(self,email,height):
        self.email = email
        self.height = height


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods=["POST"])
def success():
    global file_obj
    if request.method=="POST":
        file_obj = request.files['file']
        file_obj.save(secure_filename("uploaded_"+file_obj.filename))
        return render_template("index.html", btn="download.html")

@app.route('/download')
def download():
    return send_file("uploaded_"+file_obj.filename,attachment_filename="yourfile.csv",as_attachment="True")

if __name__=='__main__':
    app.run(debug=True)
