import os

from flask import Flask, render_template, request, redirect, send_file, url_for

from botoS3handler import fileToBbucket, fileFromBucket, allFileInBucket

from botoDynamoDbHandler import saveInDynamoDB

from werkzeug.utils import secure_filename

import openpyxl

import shutil


app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

BUCKET = "insert_bucket_name_here"

def validate_file(file):
    return True;
    if file.lower().endswith(('.csv', '.xlsx')):
        if os.path.getsize(file) < 20000000:
            return True;
        else:
            return False;
    else:
        return False;

def validate_row(row_obj):
    return True;

@app.route('/')
def entry_point():
    return 'Today we will see an example of uploading a file to s3 then validating it and then storing it in dynamo db'


@app.route("/file")
def main():
    if os.path.isdir(uploads_dir):
        shutil.rmtree(uploads_dir)
    os.makedirs(uploads_dir)
    contents = allFileInBucket("flaskdrive")
    return render_template('main.html', contents=contents)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        #f.save(f.filename)

        # validate file
        if validate_file(f):
            fileToBbucket(f"{f.filename}", BUCKET);
            f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
        else:
            # return because validation failed
            return redirect("/validateFailed");

        # show contents
        return redirect(url_for('.fileContent'));


@app.route("/validateFailed")
def validateFailed():
    return render_template('validateFailed.html')

@app.route("/fileContent")
def fileContent():
    for root, dirs, files in os.walk(uploads_dir):
        for filename in files:
            f = filename
    WORDS = []
    data_file = os.path.join(uploads_dir,secure_filename(f))
    with open(data_file, "r") as file:
        for line in file.readlines():
            validate_row(line);
            WORDS.append(line.rstrip());
    return render_template('fileContent.html', Content=WORDS)


@app.route("/saveToDb", methods=['POST'])
def saveToDb():
    if request.method == "POST":
        for root, dirs, files in os.walk(uploads_dir):
            for filename in files:
                f = filename
        WORDS = []
        data_file = os.path.join(uploads_dir,secure_filename(f))
        with open(data_file, "r") as file:
            for line in file.readlines():
                WORDS.append(line.rstrip())
        print("Saving in dynamo db")
        saveInDynamoDB(WORDS);
        return render_template('saveToDb.html')

    return render_template('saveToDb.html')




@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = fileFromBucket(filename, BUCKET)

        return send_file(output, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
