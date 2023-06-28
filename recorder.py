import glob, os
import time
import streamlit as st
from textlib import text_and_soap
import openai
#from timelib import chile_time
###############################
#openai.api_key = st.secrets['OPEN_AI_KEY']
#AWS_KEY = st.secrets['AWS_KEY']
#AWS_ID = st.secrets['AWS_ID']
###############################
from datetime import datetime
from pytz import timezone
def chile_time():
    scl = timezone('America/Santiago')
    scl_time = datetime.now(scl).strftime('%Y-%m-%dT%H-%M-%S')
    return scl_time
###############################
def audiosave(fn, audio_bytes):
    fw = open(fn, 'wb')
    fw.write(audio_bytes)
    fw.close()

def process(audio_bytes):
    t0 = chile_time()
    fn = f'AUDIO/{t0}.wav'
    audiosave(fn, audio_bytes)
    
    return text_and_soap(fn)
