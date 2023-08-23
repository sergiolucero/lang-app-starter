import streamlit as st
from awslib import s3_contents
from textlib import COMPLETION_MODEL, LANGUAGE, PROMPT, TRANSCRIPTION_MODEL, VERSION
from linelib import simple_recorder # was linetabs
from datetime import datetime
##############################################
st.set_page_config(layout="wide")
fecha = datetime.now().strftime('%Y-%m-%d')
#fecha = '2023-07-25'  # HARDCODED IN DAVIS!
tab1, tab2 = st.tabs(['Grabación','Revisión'])
with tab1:
    st.title('👨‍⚕️CETRAM QuantMed LLM Doctor🤖')
    dropline = f'(version {VERSION}). Fecha={fecha}. Modelos: [complete={COMPLETION_MODEL}, transcribe={TRANSCRIPTION_MODEL}]'
    st.write(dropline)
    dropline2 = f'Language: {LANGUAGE}. Prompt: {PROMPT}'
    st.write(dropline2)
    ############################
    # FUTURE: https://blog.streamlit.io/how-to-build-the-streamlit-webrtc-component/   
    simple_recorder()
with tab2:
    st.header('Contents of cetram-felix/AUDIO')
    contents = s3_contents()  # now filter and group by date
    # AUDIO/2023-08-23T08-54-16_soap.txt
    contents = [fn for fn in contents if fn.startswith('AUDIO/')]
    datetimes = list(set([fn[:25] for fn in contents]))
    dt_contents = {dt: [x for x in contents if x.startswith(dt)] 
                   for dt in datetimes}
    st.table(dt_contents)
