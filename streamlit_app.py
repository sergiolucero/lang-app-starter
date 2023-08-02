import streamlit as st
from textlib import COMPLETION_MODEL, TRANSCRIPTION_MODEL, VERSION
#, API_KEY
from linelib import linetabs
from datetime import datetime
##############################################
st.set_page_config(layout="wide")
#fecha = datetime.now().strftime('%Y-%m-%d')
fecha = '2023-07-25'  # HARDCODED IN DAVIS!

st.title('👨‍⚕️CETRAM QuantMed LLM Doctor🤖')
dropline = f'(version {VERSION}). Fecha={fecha}. Modelos: [complete={COMPLETION_MODEL}, transcribe={TRANSCRIPTION_MODEL}]'
st.write(dropline)
############################
tabs = linetabs(fecha)
selected_tab = st.sidebar.selectbox("Paciente", list(tabs.keys()))
tabs[selected_tab]()

