import streamlit as st
from audiorecorder import audiorecorder
from recorder import *

st.set_page_config(layout="wide")
st.title('👨‍⚕️CETRAM QuantMed LLM Doctor🤖')
#openai_logo()
st.write(f'(version {VERSION}). Modelos: [complete={COMPLETION_MODEL}, transcribe={TRANSCRIPTION_MODEL}]')
audio = audiorecorder("Presione para grabar", "Grabando... presione para terminar")

def chunksum(text):
    result = []
    with st.form('summarize_form', clear_on_submit=True):
        with st.spinner('Calculating...'):
            response = generate_response(text)
            result.append(response)
    
    if len(result):
        st.info(response)

if len(audio) > 0:
    st.audio(audio.tobytes())

    text, soap, dts = output(audio.tobytes())
    col1, col2 = st.columns(2)

    with col1:
        st.header(f'AUDIO:')   # [dt={dts[0]} secs]
        st.write(text)
                
    with col2:
        #st.write('add thumbs up/dn buttons to regenerate/accept!')
        st.header(f'resumen SOAP:') # [dt={dts[1]} secs]
        st.write(soap)
        st.write('-'*80)
        chunksum(text)

        
