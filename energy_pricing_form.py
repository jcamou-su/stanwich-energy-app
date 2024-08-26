import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Connect to Google Sheets
conn = st.experimental_connection('gsheets', type=GSheetsConnection)

# Read existing data from Google Sheets
existing_data = conn.read(worksheet="Stanwich", usecols=list(range(9)), ttl=5)
existing_data = existing_data.dropna(how='all')

st.dataframe(existing_data)

# Initialize session state for submission tracking
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Onboarding New Supplier Form
with st.form(key="supplier_form"):
    # Form fields
    supplier_name = st.text_input(label="Company Name*")
    price1 = st.number_input('Enter Price 1', min_value=0.0, format="%.6f")
    price2 = st.number_input('Enter Price 2', min_value=0.0, format="%.6f")
    price3 = st.number_input('Enter Price 3', min_value=0.0, format="%.6f")
    price4 = st.number_input('Enter Price 4', min_value=0.0, format="%.6f")
    price5 = st.number_input('Enter Price 5', min_value=0.0, format="%.6f")
    price6 = st.number_input('Enter Price 6', min_value=0.0, format="%.6f")
    price7 = st.number_input('Enter Price 7', min_value=0.0, format="%.6f")
    price8 = st.number_input('Enter Price 8', min_value=0.0, format="%.6f")
    
    # Submit button
    submit_button = st.form_submit_button(label="Submit Supplier Details")

# If the submit button is pressed
if submit_button:
    # Create a dictionary with the data
    new_data = {
        'Company Name': supplier_name,
        'Price 1': price1,
        'Price 2': price2,
        'Price 3': price3,
        'Price 4': price4,
        'Price 5': price5,
        'Price 6': price6,
        'Price 7': price7,
        'Price 8': price8
    }

    # Append data to Google Sheets
    conn.write(new_data, worksheet="Stanwich")
    
    st.write("You pressed submit!")
    st.success("Thank you! Your submission has been received.")
    st.session_state.submitted = True

# Display thank you message after submission
if st.session_state.submitted:
    st.title("Thank You!")
    st.write("Your submission has been received.")

