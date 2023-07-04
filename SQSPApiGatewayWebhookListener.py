import os
import json
import boto3
import datetime

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S'
session = boto3.Session()
s3 = session.resource('s3')

'''
Parse a proxy API Gateway object's `body` parameter and save to S3.
'''

def handler(event, context):
    try:
        if 'body' in event:
            event_data = event['body']
            data = json.loads(event_data)
            if 'data' in data:
                timestamp = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
                bucket_name = os.environ.get('BUCKET')
                obj = s3.Object(bucket_name, f'sqsp/order_{timestamp}.json')
                obj.put(Body=json.dumps(data, indent=4))
                return {
                    'statusCode': 200,
                    'body': json.dumps({'status': 'success'})
                }
            else:
                raise ValueError('Missing data in the request body')
        else:
            raise ValueError('Missing body parameter in the request')
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'status': 'failed', 'error': str(e)})
        }
