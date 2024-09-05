import streamlit as st
from predict import make_prediction

st.title('Forest Fire Prediction')

X = st.number_input('X Coordinate', min_value=1, max_value=9, value=7)
Y = st.number_input('Y Coordinate', min_value=2, max_value=9, value=5)
month = st.selectbox('Month', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
day = st.selectbox('Day', ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])
FFMC = st.number_input('FFMC', value=86.2)
DMC = st.number_input('DMC', value=26.2)
DC = st.number_input('DC', value=94.3)
ISI = st.number_input('ISI', value=5.1)
temp = st.number_input('Temperature (°C)', value=25.2)
RH = st.number_input('Relative Humidity (%)', value=50)
wind = st.number_input('Wind Speed (km/h)', value=6.7)
rain = st.number_input('Rainfall (mm)', value=0.0)

input_data = {
    'X': X,
    'Y': Y,
    'month': month,
    'day': day,
    'FFMC': FFMC,
    'DMC': DMC,
    'DC': DC,
    'ISI': ISI,
    'temp': temp,
    'RH': RH,
    'wind': wind,
    'rain': rain
}

if st.button('Predict'):
    prediction = make_prediction(input_data)
    st.write(f'Predicted burned area: {prediction:.2f} ha')
