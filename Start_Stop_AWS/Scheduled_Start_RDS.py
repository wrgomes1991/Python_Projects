import boto3
import datetime
import json

rds = boto3.client('rds')

def lambda_handler(event, context):

    instances = rds.describe_db_instances()

    for instance in instances['DBInstances']:
        if 'DBClusterIdentifier' not in instance:

            InstanceID = instance['DBInstanceIdentifier']
            InstanceStatus = instance['DBInstanceStatus']
            InstanceTags = instance['TagList']
            print(InstanceID, InstanceStatus, InstanceTags)

            for tag in instance['TagList']:
                data =  json.loads(json.dumps(tag))
                if data['Key'] == 'ScheduledStartStop' and data['Value'] == 'true' and instance['DBInstanceStatus'].upper() == 'STOPPED':
                    rds.start_db_instance(DBInstanceIdentifier=instance['DBInstanceIdentifier'])


    return "Start RDS"