import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo y el escalador desde archivos
with open('LogRegression.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

#with open('scaler.pkl', 'rb') as scaler_file:
#    scaler = pickle.load(scaler_file)

# Título de la aplicación
st.title('Predicció de la probabilitat de contractar un dipòsit')

#feature_columns = ['Length of Membership', 'Time on App', 'Avg. Session Length']
#target_column = 'Yearly Amount Spent'

# Entrada de datos del usuario
#length_of_membership = st.number_input('Length of Membership (meses)', min_value=0)
#time_on_app = st.number_input('Time on App (minutos)', min_value=0)
#avg_session_length = st.number_input('Avg. Session Length (minutos)', min_value=0)

#feature_columns = ['balance', 'age', 'age2','campaign','dgpoutcome','dhousing','dloan','dgmarital','dgmonth','dcontactcel', 'dcontacttel']
#target_column = 'ndeposit'

# Entrada de dades de l'usuari
balance = st.number_input('Mean balance in your bank account($)', min_value=0)
age = st.number_input('Your age', min_value=0)
age2 = age*age
campaign = st.number_input('Calls in the current campaign', min_value=0)
dgpoutcome = st.number_input('Did you contract a deposit in a previous campaign: (0 or 1)', min_value=0)
dhousing = st.number_input('Did you have a housing mortage: (0 or 1)', min_value=0)
dloan = st.number_input('Did you have any non-housing loan: (0 or 1)', min_value=0)
dgmarital = st.number_input('Are you currently married: (0 or 1)', min_value = 0)
dgmonth = 0
dcontactcel = st.number_input('Have you been contacted by smartphone: (0 or 1)', min_value = 0)
dcontacttel = st.number_input('Have you been contacted by phone: (0 or 1)', min_value = 0)
# Crear un DataFrame amb les entrades
user_data = pd.DataFrame({
    'balance': [balance],
    'age': [age],
    'age2': [age2],
    'campaign' : [campaign],
    'dgpoutcome' : [dgpoutcome],
    'dhousing' : [dhousing],
    'dloan' : [dloan],
    'dgmarital': [dgmarital],
    'dgmonth' : [dgmonth],
    'dcontactcel' : 
    'dcontacttel': [dcontacttel]
})

# Estandarizar las entradas
#user_data_standardized = scaler.transform(user_data)

# Realizar la predicción
prediction = model.predict(user_data)

# Mostrar la predicción
st.write(f'Predicció de la Probabilitat de Contractació: {prediction[0]:.2f}')

