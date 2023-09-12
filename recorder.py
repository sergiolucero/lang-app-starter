import glob, os
import time
import streamlit as st
from textlib import text_and_soap
from timelib import chile_time
###############################
def process(audio): #, fecha, paciente):
    t0 = chile_time()
    fn = f'AUDIO/{t0}.wav'
    audio.export(fn, format='wav')
    #audiosave(fn, audio_bytes)
    
    return text_and_soap(fn) #, fecha, paciente)
