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

# You can keep this if you want to read the data, but remove the display part
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Add a title to the app
st.title("Stanwich Energy")

# Form for adding new supplier data
with st.form(key="supplier_form"):
    supplier_name = st.text_input(label="Bet")
    price1 = st.text_input('Enter Price 1')
    price2 = st.text_input('Enter Price 2')
    price3 = st.text_input('Enter Price 3', )
    notes = st.text_input(label="Additional Notes")
    
    submit_button = st.form_submit_button(label="Submit Supplier Details")

if submit_button:
    new_data = [supplier_name, price1, price2, price3,notes]
    sheet.append_row(new_data)
    st.success("Thank you! Your submission has been received.")

