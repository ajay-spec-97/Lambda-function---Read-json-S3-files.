import json
import urllib.parse
import boto3


s3 = boto3.client('s3')

def lambda_handler(event, context):
    #Get the bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']

    #Get the file/key name which is recently uploaded 
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        #Fetch the file from S3
        response = s3.get_object(Bucket=bucket, Key=key)

        #Deserialize the file's content and store in a object "data"
        text = response["Body"].read().decode()
        data = json.loads(text)
        print(data)

        #Parse and print the Deliveries
        Deliveries = data['Deliveries']
        for record in Deliveries:
            print(record['GoodsType'])
        return 'Successfully Completed the check'

    except Exception as e:
        print(e)
        raise e