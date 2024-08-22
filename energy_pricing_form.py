import streamlit as st
import pandas as pd
import os

# Initialize the session state for submission tracking
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Define the file name for saving data
data_file = 'supplier_data.xlsx'

def save_data(data):
    try:
        if os.path.exists(data_file):
            # Load existing data
            df = pd.read_excel(data_file)
            # Append new data using pd.concat
            df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        else:
            # Create new DataFrame
            df = pd.DataFrame([data])
        
        # Save the data to Excel
        df.to_excel(data_file, index=False)
    except Exception as e:
        st.error(f"An error occurred while saving the data: {e}")

# Form submission logic
def submit_form():
    data = {
        'Company Name': st.session_state.supplier,
        'Price 1': st.session_state.price1,
        'Price 2': st.session_state.price2,
        'Price 3': st.session_state.price3,
        'Price 4': st.session_state.price4,
        'Price 5': st.session_state.price5,
        'Price 6': st.session_state.price6,
        'Price 7': st.session_state.price7,
        'Price 8': st.session_state.price8
    }
    save_data(data)
    st.session_state.submitted = True

# If the form has not been submitted, display the form
if not st.session_state.submitted:
    with st.form(key='supplier_form'):
        st.title('Energy Supplier Pricing Form')
        st.write("Please fill in all required fields.")

        # Form fields
        st.session_state.supplier = st.text_input('Company Name')
        st.session_state.price1 = st.number_input('Enter Price 1', min_value=0.0, format="%.6f")
        st.session_state.price2 = st.number_input('Enter Price 2', min_value=0.0, format="%.6f")
        st.session_state.price3 = st.number_input('Enter Price 3', min_value=0.0, format="%.6f")
        st.session_state.price4 = st.number_input('Enter Price 4', min_value=0.0, format="%.6f")
        st.session_state.price5 = st.number_input('Enter Price 5', min_value=0.0, format="%.6f")
        st.session_state.price6 = st.number_input('Enter Price 6', min_value=0.0, format="%.6f")
        st.session_state.price7 = st.number_input('Enter Price 7', min_value=0.0, format="%.6f")
        st.session_state.price8 = st.number_input('Enter Price 8', min_value=0.0, format="%.6f")

        # Submit button
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            submit_form()
            st.experimental_rerun()  # Force a rerun of the script to immediately reflect the submission state

# Show thank you message after submission
if st.session_state.submitted:
    st.write("### Thank you for your submission!")
