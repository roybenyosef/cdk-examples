#!/usr/bin/env python3

from aws_cdk import core

from dynamodb_isolation_poc.dynamodb_isolation_poc_stack import DynamodbIsolationPocStack


app = core.App()
DynamodbIsolationPocStack(app, "dynamodb-isolation-poc")

app.synth()
