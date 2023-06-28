import streamlit as st
from audiorcorder import audiorecorder

st.set_page_config(layout="wide")
st.title('🎈 CETRAM QuantMed LLM Doctor')
#st.write(f'(version {VERSION}). Modelos: [complete={COMPLETION_MODEL}, transcribe={TRANSCRIPTION_MODEL}]')
audio = audiorecorder("Presione para grabar", "Grabando... presione para terminar")
