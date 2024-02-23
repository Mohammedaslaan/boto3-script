import boto3
import json
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

def print_json(json_obj):
    formatted_json = json.dumps(json_obj, indent=4, cls=CustomEncoder)
    print(formatted_json)

codedeploy = boto3.client('codedeploy')
autoscaling = boto3.client('autoscaling')

deployment = codedeploy.get_deployment(
    deploymentId='d-X70Z7YTG3'
)

application = deployment['deploymentInfo']['applicationName']
group = deployment['deploymentInfo']['deploymentGroupName']
group = codedeploy.get_deployment_group(
    applicationName=application,
    deploymentGroupName=group,
)

print_json(group['deploymentGroupInfo']['autoScalingGroups'][0]['name'])

