

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

DT_model = pickle.load(open("dt_model.sav", 'rb'))

SVM_model = pickle.load(open("svc_model.sav",'rb'))

log_model = pickle.load(open("log_model.sav", 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Disease Web App',
                          
                          ['Log Regg',
                           'Support Vector Machines',
                           'DecisionTree'],
                          icons=['Logistic Regression','SVM','DT'],
                          default_index=0)
    
 
        
    
    

# Parkinson's Prediction Page
if (selected == "DecisionTree"):
    
    # page title
   st.title("Decision Tree")
    
   # getting the input data from the user
   col1, col2, col3 = st.columns(3)
   
   with col1:
       age = st.text_input('Age of the Person')
       
   with col2:
       sex = st.text_input('sex')
   
   with col3:
       cp = st.text_input('cp')
   
   with col1:
       trestbps = st.text_input('trestbps value')
   
   with col2:
       chol = st.text_input('chol')
   
   with col3:
       fbs = st.text_input('fbs value')
   
   with col1:
       restecg = st.text_input('restecg value')
   
   with col2:
       thalach = st.text_input('thalach')
       
   with col3:
       exang = st.text_input('exang')
       
   with col1:
       oldpeak = st.text_input('oldpeak')
       
   with col2:
       slope = st.text_input('slope')
       
   with col3:
       ca = st.text_input('ca')
       
   with col1:
       thal = st.text_input('thal')
       
       
   
        
    
    
    # code for Prediction
   DT_diagnosis = ''
    
    # creating a button for Prediction    
   if st.button("DT Test Result"):
        DT_prediction = DT_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (DT_prediction[0] == 1):
          DT_diagnosis = "The Person has Heart Disease"
        else:
          DT_diagnosis = "The Person does not have a Heart Disease"
        
   st.success(DT_diagnosis)


    

# Parkinson's Prediction Page
if (selected == "Support Vector Machines"):
    
    # page title
   st.title("Support Vector Machinese")
    
   # getting the input data from the user
   col1, col2, col3 = st.columns(3)
   
   with col1:
       age = st.text_input('Age of the Person')
       
   with col2:
       sex = st.text_input('sex')
   
   with col3:
       cp = st.text_input('cp')
   
   with col1:
       trestbps = st.text_input('trestbps value')
   
   with col2:
       chol = st.text_input('chol')
   
   with col3:
       fbs = st.text_input('fbs value')
   
   with col1:
       restecg = st.text_input('restecg value')
   
   with col2:
       thalach = st.text_input('thalach')
       
   with col3:
       exang = st.text_input('exang')
       
   with col1:
       oldpeak = st.text_input('oldpeak')
       
   with col2:
       slope = st.text_input('slope')
       
   with col3:
       ca = st.text_input('ca')
       
   with col1:
       thal = st.text_input('thal')
       
       
   
        
    
    
    # code for Prediction
   SVM_diagnosis = ''
    
    # creating a button for Prediction    
   if st.button("SVM Test Result"):
        SVM_prediction = SVM_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (SVM_prediction[0] == 1):
          SVM_diagnosis = "The Person has Heart Disease"
        else:
          SVM_diagnosis = "The Person does not have a Heart Disease"
        
   st.success(SVM_diagnosis)



# Parkinson's Prediction Page
if (selected == "Log Regg"):
    
    # page title
   st.title("Log Regg")
    
   # getting the input data from the user
   col1, col2, col3 = st.columns(3)
   
   with col1:
       age = st.text_input('Age of the Person')
       
   with col2:
       sex = st.text_input('sex')
   
   with col3:
       cp = st.text_input('cp')
   
   with col1:
       trestbps = st.text_input('trestbps value')
   
   with col2:
       chol = st.text_input('chol')
   
   with col3:
       fbs = st.text_input('fbs value')
   
   with col1:
       restecg = st.text_input('restecg value')
   
   with col2:
       thalach = st.text_input('thalach')
       
   with col3:
       exang = st.text_input('exang')
       
   with col1:
       oldpeak = st.text_input('oldpeak')
       
   with col2:
       slope = st.text_input('slope')
       
   with col3:
       ca = st.text_input('ca')
       
   with col1:
       thal = st.text_input('thal')
       
       
   
        
    
    
    # code for Prediction
   log_diagnosis = ''
    
    # creating a button for Prediction    
   if st.button("log Test Result"):
        log_prediction = log_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (log_prediction[0] == 1):
          log_diagnosis = "The Person has Heart Disease"
        else:
          log_diagnosis = "The Person does not have a Heart Disease"
        
   st.success(log_diagnosis)
