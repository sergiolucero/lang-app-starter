import boto3

def s3_upload(files, AWS_ID, AWS_KEY):
    s3 = boto3.client('s3', 
                        aws_access_key_id=AWS_ID,
                        aws_secret_access_key=AWS_KEY)
    for file in files:     
        filename = f'UPLOAD/{file}'
        s3.upload_fileobj(open(file,'rb'), FELIX_BUCKET, filename)
