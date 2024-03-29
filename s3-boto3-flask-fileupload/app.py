import boto3
import uuid

from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png'}

def allowd_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_filname = db.Column(db.String(100))
    filename = db.Column(db.String(100))
    bucket = db.Column(db.String(100))
    region = db.Column(db.String(100))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file-to-save"]
        if not allowd_file(uploaded_file.filename):
            return "FILE NOT ALLOWED"

        new_filename = uuid.uuid4().hex + '.' + uploaded_file.filename.rsplit('.', 1)[1].lower()
        bucket_name = "boto-test202030430-01"

        s3 = boto3.resource("s3")
        s3.Bucket(bucket_name).upload_fileobj(uploaded_file, new_filename)

        # DBを使用しない場合不要
        file = File(original_filname=uploaded_file.filename, filename=new_filename, bucket=bucket_name, region="ap-northeast-1")
        db.session.add(file)
        db.session.commit()
        # ここまで
    
        return redirect(url_for("index"))
    
    files = File.query.all()

    return render_template("index.html", files=files)