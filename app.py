import os

from flask import Flask, render_template, request, redirect, send_file, url_for

from botoS3handler import fileToBbucket, fileFromBucket, allFileInBucket


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "insert_bucket_name_here"


@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route("/file")
def storage():
    contents = allFileInBucket("flaskdrive")
    return render_template('storage.html', contents=contents)


@app.route("/uploadsuccess", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        fileToBbucket(f"{f.filename}", BUCKET)

        return redirect("/file")


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = fileFromBucket(filename, BUCKET)

        return send_file(output, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
