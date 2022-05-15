from typing import Dict, List
import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')

class S3UtilsException (Exception):
    pass

class S3Utils:
    
    @staticmethod
    def put_s3_files(filename:str, bucket:str, key:str )->str:
        
        try:
            s3.meta.client.upload_file(filename, bucket, key)
        
        except (ClientError, FileNotFoundError, ValueError) as error:
            raise S3UtilsException(error) from error

    @staticmethod
    def create_bucket(bucketname:str, region:str="us-east-1")->Dict:
        
        try:
            response = s3.create_bucket(
                Bucket=bucketname,
               )
            return response
        except (ClientError, ValueError) as error:
            raise S3UtilsException(error) from error


    @staticmethod
    def list_s3_folder(bucket:str, folder: str) -> List[str]:
        client = boto3.client('s3')
        try:
            response = client.list_objects(Bucket=bucket, Prefix=folder)
            content_keys = [content.get("Key") for content in response.get("Contents")]

        except (ClientError) as error:
            raise S3UtilsException(error) from error

        return content_keys


    @staticmethod
    def delete_s3_file(bucket: str, key: str) -> dict:
        client = boto3.client('s3')
        try:
            response = client.delete_object(Bucket=bucket, Key=key)

        except (ClientError) as error:
            raise S3UtilsException(error) from error

        return response