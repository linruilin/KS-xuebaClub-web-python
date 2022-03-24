# coding=UTF-8
import boto3

dynamodb = boto3.resource('dynamodb')

class DynamoDB():
    def __init__(self, name):
        self.table = dynamodb.Table(name)

    def put_item(self, item):  # 新增或修改
        try:
            put_items = self.table.put_item(Item=item)
            return put_items
        except BaseException as e:
            return {
                "code": "3001",
                "msg": "DynamoDB put error",
                "error": str(e)
            }

    def get_item(self, item):  # 读取单条数据
        try:
            get_items = self.table.get_item(Key=item)
            return get_items
        except BaseException as e:
            return {
                "code": "3002",
                "msg": "DynamoDB get error",
                "error": str(e)
            }

    def update_item(self, item, update, value):  # 更新单条数据
        try:
            update_items = self.table.update_item(
                Key=item, UpdateExpression=update, ExpressionAttributeValues=value)
            return update_items
        except BaseException as e:
            return {
                "code": "3003",
                "msg": "DynamoDB update error",
                "error": str(e)
            }

    def delete_item(self, item):  # 删除单条数据
        try:
            delete_items = self.table.delete_item(Key=item)
            return delete_items
        except BaseException as e:
            return {
                "code": "3004",
                "msg": "DynamoDB delete error",
                "error": str(e)
            }

    def batch_writer(self, list):  # 批量写入数据
        try:
            with self.table.batch_writer() as batch:
                for i in len(list):
                    batch.put_item(
                        Item=list[i]
                    )
            return {
                "code": "2000",
                "msg": "DynamoDB Success"
            }
        except BaseException as e:
            return {
                "code": "3005",
                "msg": "DynamoDB batch_writer error",
                "error": str(e)
            }

    def query(self, key):  # 扫描数据
        try:
            response = self.table.query(
                KeyConditionExpression=key
            )
            items = response['Items']
            return items
        except BaseException as e:
            return {
                "code": "3006",
                "msg": "DynamoDB query error",
                "error": str(e)
            }

    def scan(self, attr):  # 多条件查询
        try:
            response = self.table.scan(
                FilterExpression=attr
            )
            items = response['Items']
            return items
        except BaseException as e:
            return {
                "code": "3007",
                "msg": "DynamoDB scan error",
                "error": str(e)
            }
