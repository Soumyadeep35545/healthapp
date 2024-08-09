# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:22:02 2024

@author: Dell
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heartdisease_model.sav', 'rb'))
insurance_cost_model = pickle.load(open('insurance_cost.sav', 'rb'))
calories_model = pickle.load(open('calories_model.sav', 'rb'))
# sidebar for navigation
with st.sidebar:
    selected = option_menu('Health Care System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Medical Insurance Cost Calculator',
                            'Calories Burnt Calculator'
                           ],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart' ,'currency-dollar','fire'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction ')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level (0-199)')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value  (0-122)')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value (0-99)')

    with col2:
        Insulin = st.text_input('Insulin Level (0-846)')

    with col3:
        BMI = st.text_input('BMI value (0-67)')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value (0.07-2.42)')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction ')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age ')

    with col2:
        sex = st.text_input('Sex (male :0 , female :1)')

    with col3:
        cp = st.text_input('Chest Pain types (0-1)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (94-200)')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl (126-564)')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar >120 (0-NO,1-YES)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0-2)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved (71-202)')

    with col3:
        exang = st.text_input('Exercise Induced Angina (0-NO , 1-Yes)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise (0-6)')

    with col2:
        slope = st.text_input('Slope the peak exercise (0-2)')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0-4)')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''
    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
# Medical Prediction Page
if selected == 'Medical Insurance Cost Calculator':

    # page title
    st.title('Medical Insurance Cost')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('age')

    with col2:
        sex = st.text_input('sex (0-Male 1-Female)')

    with col3:
        BodyMassIndex = st.text_input('BMI (0-67)')

    with col1:
        children = st.text_input('No of Children')

    with col2:
        smoker = st.text_input('Smoker (0-Yes 1-No)')

    with col3:
        Region = st.text_input('Region (SE -0 SW-1 NE-2 NW-3')


    
    if st.button('Calculate Insurance (IN USD)'):

        user_input = [age,sex, BodyMassIndex,children,smoker,Region]

        user_input = [float(x) for x in user_input]

    chargeprediction = insurance_cost_model.predict([user_input])
    st.success(chargeprediction)


# Calories Burnt
if selected == 'Calories Burnt Calculator':

    # page title
    st.title('Calories Burnt Calculator')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
       Gender = st.text_input('Gender (Male-0 Female-1) ')

    with col2:
       Age= st.text_input('Age')

    with col3:
        Height  = st.text_input(' Height (in cms)')

    with col1:
       Weight = st.text_input('Weight (in lbs)')

    with col2:
        Duration  = st.text_input('Exercise Duration (in mins) ')

    with col2:
        Heart_Rate= st.text_input('Heart Rate (60-130)')

    with col3:
        Body_Temp= st.text_input('Body Temp (in Celcuis)')


    
    if st.button('Calculate Calories Burnt'):

        user_input = [0000000,Gender ,Age , Height , Weight , Duration , Heart_Rate , Body_Temp]

        user_input = [float(x) for x in user_input]

    chargeprediction = calories_model.predict([user_input])
    st.success(chargeprediction)
    
