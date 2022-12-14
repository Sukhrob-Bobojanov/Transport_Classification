import streamlit as st
from fastai.vision.all import *
import plotly.express as px
import pathlib
import platform

plt = platform.system()
if plt == 'Linux' : pathlib.WindowsPath = pathlib.PosixPath

#title
st.title("Transportlarni klassifikatsiya qiluvchi model")

#rasmni joylash
file = st.file_uploader("Rasm yuklash", type=['png', 'jpg', 'jpeg', 'gif'])

if file:
    st.image(file)

    #PIL convert
    img = PILImage.create(file)

    #model
    model = load_learner('transport_model.pkl')

    #predict
    pred, pred_id, probs=model.predict(img)
    st.success(f'Bashorat: {pred}')
    st.success(f'Ehtimolligi: {probs[pred_id]*100:.1f}%')
    
    #plotting
    fig=px.bar(x=probs*100, y=model.dls.vocab)
    st.plotly_chart(fig)
