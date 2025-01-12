# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:09:06 2024

@author: Priyanka Kala
"""

import streamlit as st
from streamlit_option_menu import option_menu
import pickle

diabetes_model=pickle.load(open('C:/Users/Priyanka Kala/OneDrive/Desktop/Model/Multiple Disease Prediction/diabetes_model.sav','rb'))

heart_disease_model=pickle.load(open('C:/Users/Priyanka Kala/OneDrive/Desktop/Model/Multiple Disease Prediction/heart_disease_model.sav','rb'))

parkinsons_model=pickle.load(open('C:/Users/Priyanka Kala/OneDrive/Desktop/Model/Multiple Disease Prediction/parkinsons_model.sav','rb'))

with st.sidebar:
    selected= option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          
                          icons=['activity','heart','person'],
                          
                          default_index=0)
    
# Diabetes page
if (selected=='Diabetes Prediction'):
    # page title
    st.title('Diabetes Prediction')
    
    #Getting the data from the input user
    #The order of the columns must be maintained
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of pregnancies')
        
    with col2:
        Glucose=st.text_input('Glucose Level')
        
    with col3:
        BloodPressure=st.text_input('Blood Pressure Value')
        
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin=st.text_input('Insulin Level')
        
    with col3:
        BMI=st.text_input('BMI Value')
    
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
        Age=st.text_input('Age of a person')
    
    #code for prediction
    diab_diagnosis=''
    
    #creating button for prediction
    if st.button('Result'):
        # 2 sq brackets are put inside the function then only it understands. Also maintain the order
        diab_pred = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_pred[0]==1):
            diab_diagnosis='The person is Diabetic'
        else:
            diab_diagnosis='The person is not Diabetic'
    st.success(diab_diagnosis)



    
# Heart Disease page
if (selected=='Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction')

    #Getting the input from the user
    col1, col2, col3= st.columns(3)
    with col1:
        age=st.text_input('Age')
    
    with col2:
        sex=st.text_input('Sex')
    
    with col3:
        cp=st.text_input('Chest Pain types')
        
    with col1:
        trestbp=st.text_input('Resting Blood Pressure in mg/dl')
        
    with col2:
        chol=st.text_input('Cholestrol')
        
    with col3:
        fbs=st.text_input('Fasting blood sugar > 120 mg/dl')
        
    with col1:
        rchol=st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    
    # code for Prediction
    heart_diagnosis =''

    # creating a button for Prediction

    if st.button('Result'):

       user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

       user_input = [float(x) for x in user_input]

       heart_prediction = heart_disease_model.predict([user_input])

       if heart_prediction[0] == 1:
           heart_diagnosis = 'The person is having heart disease'
       else:
           heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
        


# Parkinsons page
if (selected=='Parkinsons Prediction'):
    # page title
    st.title('Parkinsons Prediction')    

    #Getting the input from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col1:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col2:
        RAP = st.text_input('MDVP:RAP')

    with col3:
        PPQ = st.text_input('MDVP:PPQ')

    with col4:
        DDP = st.text_input('Jitter:DDP')

    with col1:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col2:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col3:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col4:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col1:
        APQ = st.text_input('MDVP:APQ')

    with col2:
        DDA = st.text_input('Shimmer:DDA')

    with col3:
        NHR = st.text_input('NHR')

    with col4:
        HNR = st.text_input('HNR')

    with col1:
        RPDE = st.text_input('RPDE')

    with col2:
        DFA = st.text_input('DFA')

    with col3:
        spread1 = st.text_input('spread1')

    with col4:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis =''

    # creating a button for Prediction    
    if st.button("Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        #user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)