import streamlit as st
from textlib import chunk_summary, diagnostico

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
