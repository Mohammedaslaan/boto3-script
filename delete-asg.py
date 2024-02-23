import boto3
import sys

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
        

if __name__ == "__main__":
    # Check if the ASG name substring is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <substring>")
        sys.exit(1)
    
    # Get the ASG name substring from the command-line argument
    asg_name_contain = sys.argv[1]
    delete_auto_scaling_group_with_name_containing(asg_name_contain)
