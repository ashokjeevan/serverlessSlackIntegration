# serverlessSlackIntegration

To test the implementation, use this code.

```
import boto3

session = boto3.Session(profile_name='default') 

as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName = '<auto scaling group name>', PolicyName = '<auto scaling group policy name>')
```

