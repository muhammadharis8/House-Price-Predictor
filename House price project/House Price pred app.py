
import streamlit as st
import joblib
import numpy as np







model = joblib.load("model.pkl")


st.title("House Price Prediction app")
st.divider()
st.write("This app uses ML for predicting House prices by features of the house . For using this app you can enter inputs by this UI and then use predict button ")
st.divider()
bedrooms = st.number_input("Enter number of bedrooms: ",min_value=0, value=0)
bathrooms = st.number_input("Enter number of bathrooms: ",min_value=0, value=0)
living_area = st.number_input("Enter living area: ",min_value=0, value=2000)
condition = st.number_input("Enter condition of house : ",min_value=0, value=3)
number_of_schools = st.number_input("Enter number of schools: ",min_value=0, value=0)


st.divider()
X = [bedrooms,bathrooms,living_area,condition,number_of_schools]

predict_btn = st.button("Predict!")

if predict_btn:
    st.balloons()

    X_array = np.array(X)
    prediction = model.predict(X_array)
    st.write(f"Price of house is {prediction}")

else:
    st.write("Please use Predict button after entering values")