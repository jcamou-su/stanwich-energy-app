import streamlit as st
from google.oauth2 import service_account
import gspread
import pandas as pd

# Specify the required scope
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Use secrets to authenticate
creds = service_account.Credentials.from_service_account_info(
    st.secrets["google_api"], scopes=scope
)

client = gspread.authorize(creds)
sheet = client.open("Stanwich").sheet1

# Read data from the sheet
data = sheet.get_all_records()
df = pd.DataFrame(data)

st.dataframe(df)

# Form for adding new supplier data
with st.form(key="supplier_form"):
    supplier_name = st.text_input(label="Company Name*")
    price1 = st.number_input('Enter Price 1', min_value=0.0, format="%.6f")
    price2 = st.number_input('Enter Price 2', min_value=0.0, format="%.6f")
    price3 = st.number_input('Enter Price 3', min_value=0.0, format="%.6f")
    price4 = st.number_input('Enter Price 4', min_value=0.0, format="%.6f")
    price5 = st.number_input('Enter Price 5', min_value=0.0, format="%.6f")
    price6 = st.number_input('Enter Price 6', min_value=0.0, format="%.6f")
    price7 = st.number_input('Enter Price 7', min_value=0.0, format="%.6f")
    price8 = st.number_input('Enter Price 8', min_value=0.0, format="%.6f")
    
    submit_button = st.form_submit_button(label="Submit Supplier Details")

if submit_button:
    new_data = [supplier_name, price1, price2, price3, price4, price5, price6, price7, price8]
    sheet.append_row(new_data)
    st.success("Thank you! Your submission has been received.")

