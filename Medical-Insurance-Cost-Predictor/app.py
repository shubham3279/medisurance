# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:08:09 2022

@author: SHUBHAM KUMAR
"""

import numpy as np
import joblib
import streamlit as st
from PIL import Image
from annotated_text import annotated_text

# loading the  model
loaded_model = joblib.load('https://github.com/shubham3279/Machine-Learning-and-Deep-Learning/blob/main/Medical-Insurance-Cost-Predictor/trained_model.sav')



def insurance_charge(input_data):
    
    # to numpy array and reshaping
    numpy_input = np.asarray(input_data)
    proper_input = numpy_input.reshape(1, -1)

    prediction = loaded_model.predict(proper_input)
    return ('Your medical insurance will cost you around:$', prediction[0])




def main():
    
    # webpage setup
    
    img = Image.open('OIP.jpeg')
    st.set_page_config(page_title = 'Medical Insurance Cost Predictor', page_icon = img )
    st.title('Medical Insurance Cost Predictor')
    
    # TAKING INPUTS FROM THE USER
    
    # Age input
    age = st.slider("Your age!", 0, 130, 30)
    
    # Sex input
    sex = st.selectbox("Your gender please!", options = ['Male','Female'])
    if sex == 'Male':
        sex_value = 0
    else:
        sex_value = 1
           
    # BMI input
    bmi = st.slider("What is your BMI?", 0.00, 188.00, 30.00)
    
    # Children Input
    children = st.selectbox("No. of childrens you have!", options = ['0','1','2','3','4','5'])
    
    # Smoker Input
    smoker =  st.selectbox("You smoke?", options = ['Yes','No'])
    if smoker == 'Yes':
        smoker_value = 0
    else:
        smoker_value = 1
        
    # Region Input       
    region = st.selectbox("Where do you live?", options=['Southeast','Northwest','Southwest','Northeast'])
    if region == 'Southeast':
        region_value = 0
    elif region == 'Northwest':
        region_value = 1
    elif region == 'Southwest':
        region_value = 2
    else:
        region_value = 3


    # code for prediction:
        
    cost = ''
    
    if st.button("Predict the Insurance Cost"):
        input_list = [age,sex_value,bmi,children,smoker_value,region_value]
        cost = insurance_charge(input_list)
        
    st.success(cost)
    
    
    annotated_text(('Made by', "Shubham", "#394F8A"))
    
    
    
    
    
if __name__ == '__main__':
    main()
        
        
