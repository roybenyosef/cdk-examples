import random
import unittest

import boto3

tenants = [
    'd0805f79-527a-4093-9acc-1aeadd103537',
    '031f8ee9-da13-4fd2-a1a2-3a082e7c878a',
    '3d348d4b-51ea-4af1-a95c-3ee1f9a795b1',
    'ee873119-7f49-4957-b1b6-235df1760083'
]

def test_init_db():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('MultiTenantTable')

    tenant_id = random.choice(tenants)
    data = 2015

    response = table.put_item(
        Item={
            'tenant_id': tenant_id,
            'title': title,
            'info': {
                'plot': "Nothing happens at all.",
                'rating': decimal.Decimal(0)
            }
        }
    )