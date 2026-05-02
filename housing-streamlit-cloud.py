# DSC 333: Streamlit app for housing price predictor API
# Intended to run on Streamlit cloud
import streamlit as st
import requests

st.title('House price estimator')

# retrieve IP address from 
VM_IP = st.secrets('VM_IP')

with st.form(key='my_form'):
    bedrooms = st.slider('Bedrooms', 0, 20, 3)
    bathrooms = st.slider('Bathrooms', 0, 10, 2)
    living_sqft = st.slider('Living space (sq. ft.)', 800, 5000, 1500)
    lot_size = st.slider('Lot size (sq. ft.)', 2000, 50000, 10000)
    submitted = st.form_submit_button(label='Estimate price')

    if submitted:
    
        # Replace <IP> with the IP address where the FastAPI 
        # server is running (porbably your VM's IP)
        URL = f'http://{VM_IP}:8080/ia_estimate'
        params = {'bedrooms':int(bedrooms),
                  'bathrooms':int(bathrooms),
                  'living_sqft':int(living_sqft),
                  'lot_size':int(lot_size)}
        r = requests.get(URL, params=params)
        r_json = r.json()
        print(r_json['ia_estimate'])
        st.subheader('Estimated price:')

        estimate = r_json['ia_estimate']

        # remove brackets and decimal values and display result
        estimate = estimate[1:estimate.index('.')]
        st.text('$'+estimate)
