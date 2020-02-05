from aws_cdk import (
    core,
    aws_dynamodb as dynamodb
)
import boto3


class DynamodbIsolationPocStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        self.accounts_table = dynamodb.Table(self, "MultiTenantTable",
                                             partition_key=dynamodb.Attribute(
                                                 name="tenant_id",
                                                 type=dynamodb.AttributeType.STRING),
                                             billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
                                             removal_policy=core.RemovalPolicy.DESTROY)

