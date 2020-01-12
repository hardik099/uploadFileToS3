import os

from flask import Flask, render_template, request, redirect, send_file, url_for

from botoS3handler import fileToBbucket, fileFromBucket, allFileInBucket

from botoDynamoDbHandler import saveInDynamoDB

import openpyxl


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
        else:
            # return because validation failed
            return redirect("/validateFailed");

        # show contents

        return redirect(url_for('.fileContent', file=f));


@app.route("/validateFailed")
def validateFailed():
    return render_template('validateFailed.html')

@app.route("/fileContent")
def fileContent():
    if request.method == "POST":
        # f = request.files['file']
        # f.save(f.filename)
        # text = open(f, 'r+');
        # employeedata = text.read();
        # text.close();
        saveInDynamoDB(employeedata);
        return redirect("/saveToDb");

    file_data = [];
    wb_obj = openpyxl.load_workbook(request.files['file']);
    sheet_obj = wb_obj.active;
    row_obj= sheet_obj.row(row = 1);
    file_data.append(row_obj);
    for row in sheet_obj.iter_rows(row_offset=1):
        validate_row(row);
        file_data.append(row_obj)
    return render_template('fileContent.html', contents=file_data)


@app.route("/saveToDb")
def saveToDb(contents):
    return render_template('saveToDb.html', contents=contents)




@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = fileFromBucket(filename, BUCKET)

        return send_file(output, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
