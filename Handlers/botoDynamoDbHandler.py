import boto3

dynamo_client = boto3.client('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
table_name = "employee_table"
def saveInDB(employee_data):
    # return dynamo_client.batch_write_item(employee_data);
    dynamo=boto3.resource('dynamodb');
    t=dynamo.Table(table_name);
    for employee in employee_data:
        t.put_item(employee)

    return "success";


def readAllFromDB():
    return dynamo_client.scan(
        TableName=table_name
    )

def readBasedOnIdFromDB(employee_id):
    try:
        dynamo=boto3.resource('dynamodb');
        t=dynamo.Table(table_name);
        m=t.get_item(  #fetching the items from the table with a certain id
            Key={
                'EMPLOYEE_ID' : employee_id
            })
        m=m['Item'];
        js = json.dumps(m)
        return js;
    except:
        raise Exception("there is something wrong!!!")