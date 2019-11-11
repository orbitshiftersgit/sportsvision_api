from app import app
from flask import request, Response
import boto3
from werkzeug.utils import secure_filename

ACCESS_KEY = " "
SECRET_KEY = " "


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'mp4'


s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file found"
        file = request.files['file']
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            s3.upload_file(Bucket='sportsvision-app', Filename=filename, Key='videos/' + file.filename)
            return "file successfully saved"
        return 'invalid file'


@app.route('/download/<file_name>', methods=['GET'])
def download(file_name):
        try:
            file = s3.get_object(Bucket='sportsvision-app', Key='videos/' + file_name)
            return Response(
               file['Body'].read(),
               mimetype='video/mp4',
                headers={"Content-Disposition": "attachment;filename=" + file_name})
        except:
            return "no file found"
