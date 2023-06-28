import glob, os
import time
from datetime import datetime
from pytz import timezone
import streamlit as st
from textlib import text_and_soap
###############################
openai.api_key = st.secrets['OPEN_AI_KEY']
AWS_KEY = st.secrets['AWS_KEY']
AWS_ID = st.secrets['AWS_ID']
FELIX_BUCKET = 'cetram-felix'

VERSION = '0.3'
AWS_COPY = 'aws s3 cp %s s3://cetram-estenio/FELIX/UPLOAD/'
###############################
#def openai_logo():
#    st.markdown(
#   f"""
#   <style>
#   p {background-image: url('openai.png');}
#   </style>
#   """,
#   unsafe_allow_html=True)
    
def chile_time():
    scl = timezone('America/Santiago')
    scl_time = datetime.now(scl).strftime('%Y-%m-%dT%H-%M-%S')
    return scl_time
###############################

def s3_upload(files):
    s3 = boto3.client('s3', 
                        aws_access_key_id=AWS_ID,
                        aws_secret_access_key=AWS_KEY)
    for file in files:     
        filename = f'UPLOAD/{file}'
        s3.upload_fileobj(open(file,'rb'), FELIX_BUCKET, filename)

    
def output(audio_bytes):
    t0 = chile_time()
    fn = f'AUDIO/test_{t0}.wav'
    print('saving to:', fn)
    fw = open(fn, 'wb')
    fw.write(audio_bytes)
    fw.close()

    return text_and_soap(fn)
