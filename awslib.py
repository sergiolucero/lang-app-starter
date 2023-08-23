import boto3
import streamlit as st

FELIX_BUCKET = 'cetram-felix'
AWS_KEY = st.secrets['AWS_KEY'] 
AWS_ID = st.secrets['AWS_ID']
##############
def s3_client():
    return boto3.client('s3', 
                        aws_access_key_id=AWS_ID,
                        aws_secret_access_key=AWS_KEY)
def t3_upload(files):
    pass

def s3_contents():
    s3 = s3_client()    
    results = s3.list_objects_v2(Bucket=FELIX_BUCKET)  #, Prefix=folder_prefix)
    file_names = []
    for content in results.get('Contents', []):
        file_names.append(content['Key'])
    return file_names
    
def s3_upload(files):
    s3 = s3_client() 
    for file in files:     
        print('S3 save:', file)
        try:
            s3.upload_fileobj(open(file,'rb'), 
                          FELIX_BUCKET, file)
        except Exception as e:
            raise Exception(f'FILE: {file}\n ERROR: {e} ')
