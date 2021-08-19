# -*- coding: utf-8 -*-
"""
Medical Insurance Regression Problem
"""
import pickle
import streamlit as st

# loading the trained model
pickle_in = open(r"C:\Users\HP\Desktop\Ankush_Projects\Regression_Project(Predict Medical Insurance Charges)\medical_insurance.pkl", 'rb')
regressor = pickle.load(pickle_in)


@st.cache()
# defining the function which will make the prediction using the data which the user inputs
def prediction(age, sex, bmi, children,smoker, region):
    # Pre-processing user input
    
    if sex == "female":
        sex = 0
    else:
        sex = 1
        
    if smoker == "no":
        smoker = 0
    else:
        smoker = 1
        

    if region == "northeast":
        region = 0
    elif region =="northwest":
        region = 1
    elif region =="southeast" :
        region = 2   
    else:
        region = 3


    # Making predictions
    prediction = regressor.predict(
        [[age,sex, bmi, children,smoker,region]])


    return prediction


# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:Orange;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Medical Insurance Cost Prediction ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    age = st.slider("Age",0,100)
    sex = st.selectbox('Sex', ("male", "female"))
    bmi = st.number_input("BMI",0,50)
    children= st.slider("No of children dependent",0,5)
    smoker = st.selectbox('Smoker', ("no", "yes"))
    region = st.selectbox('Region', ("northeast","northwest","southeast", "southwest"))
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(age, sex,bmi, children,smoker,region)
        st.write('Your Medical Insurance Cost is {}'.format(result))


if __name__ == '__main__':
    main()



