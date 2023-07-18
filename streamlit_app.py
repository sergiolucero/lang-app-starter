import streamlit as st
from audiorecorder import audiorecorder
from recorder import process
from textlib import COMPLETION_MODEL, TRANSCRIPTION_MODEL, VERSION, API_KEY
from textlib import chunk_summary, diagnostico
from datetime import datetime
import os
##############################################
st.set_page_config(layout="wide")
st.title('👨‍⚕️CETRAM QuantMed LLM Doctor🤖')
#openai_logo()
#st.write(f'API={API_KEY}')
############################ tabbing 
def tab(lines):   # should pass date+paciente
    #html = open(filename).read()
    slines = lines.lstrip().split(chr(10))
    head = slines[0]
    body = slines[1:]
    st.write(head)
    st.write(body)
    
    audio = audiorecorder("Presione para grabar", 
                          "Grabando... presione para terminar",
                         key = head)
    
    if len(audio) > 0:
        st.audio(audio.tobytes())
        with st.spinner('procesando...'):
            text, soap, dts = process(audio.tobytes())
            col1, col2 = st.columns(2)
        
            with col1:
                st.header(f'TRANSCRIPCION AUDIO:')   # [dt={dts[0]} secs]
                st.info(text)  # was write
                #diagnostico(text)
                        
            with col2:
                #st.write('add thumbs up/dn buttons to regenerate/accept!')
                st.header(f'resumen SOAP:') # [dt={dts[1]} secs]
                st.write(soap)
                st.write('-'*80)
                chunk_summary(text)

# make this block a function call
fecha = datetime.now().strftime('%Y-%m-%d')
pfn = f'previo-{fecha}.txt'
if os.path.exists(pfn):
    lines = open(pfn, encoding='utf-8').read()
    lines = lines.split('-'*80)
    #lines = [line.split(chr(10)) for line in lines]
    
dropline = f'(version {VERSION}). Fecha={fecha}. Modelos: [complete={COMPLETION_MODEL}, transcribe={TRANSCRIPTION_MODEL}]'
st.write(dropline)
# Create a dictionary with tab names as keys and corresponding functions as values
tabs = {line.split(chr(10))[0]: tab(line) for line in lines}
selected_tab = st.sidebar.selectbox("Paciente", list(tabs.keys()))
tabs[selected_tab]()

