import boto3
import datetime
import json

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    for instance in instances:
        print(instance.id, instance.instance_type, instance.tags )
    
        i = 0
        for tag in instance.tags:
            data = json.loads(json.dumps(tag))
            if data['Key'] == 'ScheduledStartStop':
                i = 1
                if data['Value'] == 'true':
                    ec2.instances.filter(InstanceIds=[instance.id]).start()
    
    
    return "Start instances"