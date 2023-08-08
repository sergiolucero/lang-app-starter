import streamlit as st
from textlib import COMPLETION_MODEL, TRANSCRIPTION_MODEL, VERSION
from linelib import simple_recorder # was linetabs
from datetime import datetime
##############################################
st.set_page_config(layout="wide")
#fecha = datetime.now().strftime('%Y-%m-%d')
fecha = '2023-07-25'  # HARDCODED IN DAVIS!

st.title('👨‍⚕️CETRAM QuantMed LLM Doctor🤖')
dropline = f'(version {VERSION}). Fecha={fecha}. Modelos: [complete={COMPLETION_MODEL}, transcribe={TRANSCRIPTION_MODEL}]'
st.write(dropline)
############################
simple_recorder()
