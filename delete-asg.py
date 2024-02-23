import boto3

def delete_auto_scaling_group_with_name_containing(substring):
    # Initialize the Boto3 Auto Scaling client
    autoscaling_client = boto3.client('autoscaling')

    # Describe Auto Scaling groups to find the one with the specified substring in its name
    response = autoscaling_client.describe_auto_scaling_groups()
    found = False
    # Iterate through the Auto Scaling groups
    for group in response['AutoScalingGroups']:
        if substring in group['AutoScalingGroupName']:
            found = True
            # Delete the Auto Scaling group
            print(f"Deleting Auto Scaling group: {group['AutoScalingGroupName']}")
            autoscaling_client.delete_auto_scaling_group(
                AutoScalingGroupName=group['AutoScalingGroupName'],
                ForceDelete=True  # Set to True to force deletion even if there are instances in the group
            )
    if not found :
        print("Named ASG not Exits")
        

# Call the function with the substring to search for in the Auto Scaling group names

asg_name_contain = "d-DXVTVCXG3"
delete_auto_scaling_group_with_name_containing(asg_name_contain)
