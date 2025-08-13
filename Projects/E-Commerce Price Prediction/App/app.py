import streamlit as st
import numpy as np
import pickle

with open('models/scaler.pkl', 'rb') as f:
    loded_scaler = pickle.load(f)

with open('models/best_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

st.title('E-Commerce Price Prediction')

average_session = st.number_input('Average Session Length')
time_app = st.number_input('Time On App')
membership = st.number_input('Length Of Membership')

if st.button('Predict'):
    data = np.array([average_session, time_app, membership]).reshape(1, -1)
    new_data = loded_scaler.transform(data)
    predict = loaded_model.predict(new_data)

    st.success(f"Yearly Ammount Spent : {predict[0]}")