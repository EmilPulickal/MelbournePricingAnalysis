import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('Melbourne1.pkl','rb'))
st.title("House Price Predictor")

car = int(st.text_input("Number of car parking provided: ","1"))
area = int(st.text_input("Area of the Building: ","75"))
year = int(st.text_input("Year Built: ","1970"))
size = int(st.text_input("Landsize: ","220"))

featureInput = np.array([[car,size,area,year]])

sal = model.predict(featureInput)

st.write(f'Hello, *World!* :sunglasses: . Customer Group : {sal} ')
