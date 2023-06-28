import streamlit as st
from audiorecorder import audiorecorder
from recorder import *

st.set_page_config(layout="wide")
st.title('👨‍⚕️CETRAM QuantMed LLM Doctor🤖')
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhaAzr6jf5YvXano3_RQonb7on-4bJ6DaOtQFMa7Y&s')
#st.write(f'(version {VERSION}). Modelos: [complete={COMPLETION_MODEL}, transcribe={TRANSCRIPTION_MODEL}]')
audio = audiorecorder("Presione para grabar", "Grabando... presione para terminar")

if len(audio) > 0:
    st.audio(audio.tobytes())

    text, soap, dts = output(audio.tobytes())
    col1, col2 = st.columns(2)

    with col1:
        st.header(f'AUDIO:')   # [dt={dts[0]} secs]
        st.write(text)
        files = str(list(glob.glob('AUDIO/*')))
        st.write(f'FILES:', files)
                
    with col2:
        #st.write('add thumbs up/dn buttons to regenerate/accept!')
        st.header(f'resumen SOAP:') # [dt={dts[1]} secs]
        st.write(soap)
