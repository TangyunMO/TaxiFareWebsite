import streamlit as st
import requests


st.markdown('''
# Let's Predict Your Taxi Fare in NYC 🏙
## with Our Wonderful Model
''')


pickup_datetime = st.text_input("Your Pickup Date and Time")
pickup_longitude = st.text_input("Your Pickup Longtitude")
pickup_latitude = st.text_input("Your Pickup Latitude")
dropoff_longitude = st.text_input("Your Dropoff Longtitude")
dropoff_latitude = st.text_input("Your Dropoff Latitude")
passenger_count = st.slider('Select a passenger number', 1, 8, 1)



url = 'https://tfmpreditinprodimage-vn22nmmxga-ew.a.run.app/'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


params = {
    'pickup_datetime':pickup_datetime,
    'pickup_longitude':pickup_longitude,
    'pickup_latitude':pickup_latitude,
    'dropoff_longitude':dropoff_longitude,
    'dropoff_latitude':dropoff_latitude,
    'passenger_count':passenger_count
}

params_filled = pickup_datetime and pickup_longitude and pickup_latitude and dropoff_longitude and dropoff_latitude and passenger_count

if st.button('Predict🚕'):
    if params_filled:
        res = requests.get(f"{url}predict", params=params).json()

        st.json(res)
