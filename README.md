This repo is python flask integration with S3 bucket and dynamodb

With this user can upload the file that will be validated based on size and file type.
Then that file will be save to S3 bucket.
After that file will be saved at server. Row wise file contents are checked and based on that 
file contents will be shown to user with which confirmation will be asked from user whether
to store it in dynamodb or not. If yes then it will be saved to dynamoDb else not

To make things work 
User needs to add S3 bucket name and dynamoDb config in botoHandler files