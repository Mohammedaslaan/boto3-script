import boto3

# Initialize CloudWatch client
client = boto3.client('cloudwatch')

# Call describe_alarms method
response = client.describe_alarms(
    AlarmNames=[
        'ASG-Alarm',
    ],
    # Optionally, you can include other parameters here
    # AlarmNamePrefix='string',
    # AlarmTypes=[
    #     'CompositeAlarm'|'MetricAlarm',
    # ],
    # ChildrenOfAlarmName='string',
    # ParentsOfAlarmName='string',
    # StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
    # ActionPrefix='string',
    # MaxRecords=123,
    # NextToken='string'
)

# Print the response
print(response['MetricAlarms'][0]['Dimensions'][0]['Value'])

