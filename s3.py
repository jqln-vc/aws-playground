# criando um bucket com AWS CLI
# aws s3 mb s3://nome-do-bucket

def create_bucket(bucket_name):
    import boto3
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    
