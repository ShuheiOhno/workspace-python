import boto3
s3 = boto3.resource('s3')

# バケットを表示
for bucket in s3.buckets.all():
    print(bucket.name)

# ローカルファイルをアップロード
data = open('test3.txt', 'rb')
s3.Bucket('boto-test202030430-01').put_object(Key='test3.txt', Body=data)

# ローカルファイルをアップロード
data = open('test3.txt', 'rb')
s3.Bucket('boto-test202030430-01').put_object(Key='test3.txt', Body=data)

# バケット作成
# S3.Client.create_bucket('testbucketboto3boto30430')
new_bucket = s3.Bucket('testbucketboto3boto30430')
new_bucket.create()