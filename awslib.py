import boto3

FELIX_BUCKET = 'cetram-felix'

def s3_upload(files, AWS_ID, AWS_KEY):
    s3 = boto3.client('s3', 
                        aws_access_key_id=AWS_ID,
                        aws_secret_access_key=AWS_KEY)
    
    for file in files:     
        print('S3 save:', file)
        try:
            s3.upload_fileobj(open(file,'rb'), 
                          FELIX_BUCKET, file)
        except Exception as e:
            raise Exception(f'FILE: {file}\n ERROR: {e} ')