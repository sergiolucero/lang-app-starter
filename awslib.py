import boto3
import streamlit as st

FELIX_BUCKET = 'cetram-felix'
AWS_KEY = st.secrets['AWS_KEY'] 
AWS_ID = st.secrets['AWS_ID']

def t3_upload(files):
    pass

def s3_upload(files):
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
