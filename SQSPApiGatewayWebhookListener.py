import os
import json
import boto3
import datetime

session = boto3.Session()
s3 = session.resource('s3')

def handler(event, context):
    '''
    Parse a proxy API Gateway object's `body` parameter and save to S3.
    '''

    timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    if 'body' in event:
        event_data = event.get('body')
        data = json.loads(event_data)
        if 'data' in data:
            # Test Changes
            obj = s3.Object(os.environ.get('BUCKET'), f'sqsp/order_{timestamp}.json')
            res = obj.put(Body=json.dumps(data, indent=4))
            return {
                'statusCode': 200,
                'body': json.dumps({'status': 'success'})
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'status': 'failed'})
            }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps({'status': 'failed'})
        }
