import cv2
import streamlit as st
from audiorecorder import audiorecorder

audio = audiorecorder("Presione para grabar", 
                          "Grabando... presione para terminar",
                         key = head)
if len(audio) > 0:
    #st.audio(audio.tobytes())   # esto muestra el audio para su revisión
    with st.spinner('procesando...'):
        text, soap = process(audio.tobytes(), fecha, nombre_paciente)
