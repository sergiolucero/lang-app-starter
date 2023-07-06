import streamlit as st
from audiorecorder import audiorecorder
from recorder import process
from textlib import COMPLETION_MODEL, TRANSCRIPTION_MODEL, VERSION, chunk_summary, API_KEY

st.set_page_config(layout="wide")
st.title('👨‍⚕️CETRAM QuantMed LLM Doctor🤖')
#openai_logo()
#st.write(f'API={API_KEY}')
st.write(f'(version {VERSION}). Modelos: [complete={COMPLETION_MODEL}, transcribe={TRANSCRIPTION_MODEL}]')
audio = audiorecorder("Presione para grabar", "Grabando... presione para terminar")

if len(audio) > 0:
    st.audio(audio.tobytes())
    with st.spinner('procesando...'):
        text, soap, dts = process(audio.tobytes())
        col1, col2 = st.columns(2)
    
        with col1:
            st.header(f'AUDIO:')   # [dt={dts[0]} secs]
            st.write(text)
                    
        with col2:
            #st.write('add thumbs up/dn buttons to regenerate/accept!')
            st.header(f'resumen SOAP:') # [dt={dts[1]} secs]
            st.write(soap)
            st.write('-'*80)
            chunk_summary(text)
