import boto3
import openai
import glob, os
import tiktoken
import time
from datetime import datetime
from pytz import timezone
import streamlit as st
###############################
openai.api_key = st.secrets['OPEN_AI_KEY']
COMPLETION_MODEL = "text-davinci-003"
TRANSCRIPTION_MODEL = "whisper-1"
TOP_TOKENS = 3800
AWS_COPY = 'aws s3 cp %s s3://cetram-estenio/FELIX/UPLOAD/'
###############################
def chile_time():
    scl = timezone('America/Santiago')
    scl_time = datetime.now(scl).strftime('%Y-%m-%dT%H-%M-%S')
    return scl_time
###############################
def tokens(text, completion_model):
    encoding=tiktoken.encoding_for_model(completion_model)
    return len(encoding.encode(text))

def openai_transcribe(fn):
    audio_file= open(fn, "rb")
    try:
        transcript = openai.Audio.transcribe(TRANSCRIPTION_MODEL, file=audio_file,
            response_format="text",language="es")# text = transcript.to_dict()['text']
    except Exception as e:
        transcript = f'TRANSCRIPCIÓN FALLIDA: (FILE={fn}) \n ERROR={e}'
    
    return transcript
    
def soapit(text, completion_model = COMPLETION_MODEL):
    
    MAX_TOKENS = TOP_TOKENS-tokens(text, completion_model)
    print('MAX_TOKENS:', MAX_TOKENS)
    try:        # should use LangChain Prompts
        response = openai.Completion.create(
          model=completion_model,
          prompt=f"resume este texto en formato médico SOAP:\n\n{text}",
          temperature=1, max_tokens=MAX_TOKENS,
          top_p=1.0,frequency_penalty=0.0,presence_penalty=0.0)
        return response.to_dict()['choices'][0]['text']
    except Exception as e:
        transcript = f'RESUMEN SOAP FALLIDO: {e}'
        return transcript
        
def summarize(text, completion_model = COMPLETION_MODEL):
    MAX_TOKENS = TOP_TOKENS-tokens(text, completion_model)
    try:
        response = openai.Completion.create(
            model=completion_model,
            prompt=f"haz un punteo de este texto:\n\n{text}",
            temperature=1,max_tokens=MAX_TOKENS,
            top_p=1.0, frequency_penalty=0.0,presence_penalty=0.0
            )
    except Exception as e:
        transcript = f'RESUMEN SOAP FALLIDO: {e}'

    return response
##################################################
def text_and_soap(fn):
    t0=time.time()
    text = openai_transcribe(fn)
    t1=time.time()
    print('TEXT:', text)
    soap = soapit(text)
    t2=time.time()
    dts = [round(t1-t0,2), round(t2-t1,2)]

    # uploading audio + 2 texts           (added 06-15)
    txt_fn = fn.replace('.wav','.txt')
    soap_fn = fn.replace('.wav','_soap.txt')

    open(txt_fn, 'w').write(text)
    open(soap_fn, 'w').write(soap)

    for file in [fn, txt_fn, soap_fn]:     
        fcmd = AWS_COPY %file
        print(f'CMD: {fcmd}')
        #os.system(fcmd)
    
    return text, soap, dts
    
def output(audio_bytes):
    t0 = chile_time()
    fn = f'AUDIO/test_{t0}.wav'
    print('saving to:', fn)
    fw = open(fn, 'wb')
    fw.write(audio_bytes)
    fw.close()

    return text_and_soap(fn)
