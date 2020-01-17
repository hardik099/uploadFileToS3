This repo is python flask integration with S3 bucket and dynamodb

With this user can upload the file that will be validated based on size and file type.
Then that file will be save to S3 bucket.
After that file will be saved at server. Row wise file contents are checked and based on that 
file contents will be shown to user with which confirmation will be asked from user whether
to store it in dynamodb or not. If yes then it will be saved to dynamoDb else not.

There is a handler for mysql database also. That uses SqlAlchemy to write to db.
In app.py if you want to use mysql db then change the import

To make things work 
User needs to add S3 bucket name , dynamoDb config in botoHandler files and Mysql user , passw, localhost, port

Reference : 
https://leportella.com/english/2019/01/10/sqlalchemy-basics-tutorial.html
https://medium.com/swlh/how-to-insert-data-from-csv-file-into-a-sqlite-database-using-python-82f7d447866a