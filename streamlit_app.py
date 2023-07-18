import streamlit as st
from audiorecorder import audiorecorder
from recorder import process
from textlib import COMPLETION_MODEL, TRANSCRIPTION_MODEL, VERSION, API_KEY
from linelib import fileread, linetab
from datetime import datetime
##############################################
st.set_page_config(layout="wide")
fecha = datetime.now().strftime('%Y-%m-%d')
st.title('👨‍⚕️CETRAM QuantMed LLM Doctor🤖')
dropline = f'(version {VERSION}). Fecha={fecha}. Modelos: [complete={COMPLETION_MODEL}, transcribe={TRANSCRIPTION_MODEL}]'
st.write(dropline)
############################
lines = fileread(fecha)
tabs = {line.split(chr(10))[0]: linetab(line) for line in lines}
selected_tab = st.sidebar.selectbox("Paciente", list(tabs.keys()))
tabs[selected_tab]()

