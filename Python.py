import boto3
from datetime import datetime, timezone
s3 = boto3.resource('s3')
s3.Object('blueoptimatest', 'ec2.txt').upload_file('/home/ec2-user/ec2.txt')
