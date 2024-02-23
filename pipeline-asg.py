import boto3

def get_latest_asg_name():
    client = boto3.client('codedeploy')
    response = client.get_deployment(
        deploymentId='d-7I7P67PG3'
    )
    return response['deploymentInfo']['targetInstances']['autoScalingGroups'][0]

def update_cloudwatch_alarm(auto_scaling_group_name, alarm_name):
    # Initialize CloudWatch client
    cloudwatch_client = boto3.client('cloudwatch')

    try:
        # Describe the alarm to get its current configuration
        response = cloudwatch_client.describe_alarms(
            AlarmNames=[alarm_name]
        )

        # Extract the current alarm configuration
        alarm = response['MetricAlarms'][0]

        # Modify the Auto Scaling Group associated with the alarm
        alarm['Dimensions'] = [{
            'Name': 'AutoScalingGroupName',
            'Value': auto_scaling_group_name
        }]

        # Update the alarm with the modified configuration
        cloudwatch_client.put_metric_alarm(
            AlarmName=alarm_name,
            ActionsEnabled=alarm['ActionsEnabled'],
            OKActions=alarm['OKActions'],
            AlarmActions=alarm['AlarmActions'],
            InsufficientDataActions=alarm['InsufficientDataActions'],
            MetricName=alarm['MetricName'],
            Namespace=alarm['Namespace'],
            Statistic=alarm['Statistic'],
            Dimensions=alarm['Dimensions'],
            Period=alarm['Period'],
            EvaluationPeriods=alarm['EvaluationPeriods'],  # Required parameter
            Threshold=alarm['Threshold'],
            ComparisonOperator=alarm['ComparisonOperator'],  # Required parameter
            TreatMissingData=alarm['TreatMissingData'],
            # ExtendedStatistic=str(alarm.get('ExtendedStatistic', '')),  # Ensure it's a string
            Unit=str(alarm.get('Unit', 'Percent')),  # Ensure it's a string
            Tags=alarm.get('Tags', [])
        )

        print(f"Successfully updated CloudWatch alarm '{alarm_name}' with new Auto Scaling Group '{auto_scaling_group_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    new_asg_name = get_latest_asg_name()
    auto_scaling_group_name = new_asg_name
    alarm_name = 'ASG-Alarm'

    update_cloudwatch_alarm(auto_scaling_group_name, alarm_name)
