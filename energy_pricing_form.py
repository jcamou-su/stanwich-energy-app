import streamlit as st
import pandas as pd
import os

# Initialize session state for submission tracking and confirmation dialog
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'confirm_submit' not in st.session_state:
    st.session_state.confirm_submit = False

# Define the CSV file name with an absolute path
csv_file = '/absolute/path/to/your/directory/supplier_data.csv'

# Function to save data to a CSV file directly
def save_data_to_csv(data):
    st.write("Attempting to save the following data to CSV:", data)  # Debugging line
    try:
        file_exists = os.path.isfile(csv_file)
        df = pd.DataFrame([data])
        df.to_csv(csv_file, mode='a', header=not file_exists, index=False)
        st.write(f"Data successfully saved to {csv_file}")  # Confirm save
        return True
    except Exception as e:
        st.error(f"An error occurred while saving the data to the CSV file: {e}")
        return False

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
    st.write("Data to be saved:", data)  # Debugging line
    if save_data_to_csv(data):
        st.session_state.submitted = True
        st.session_state.confirm_submit = False

# Display form or thank you message based on submission state
if not st.session_state.submitted:
    if not st.session_state.confirm_submit:
        st.title('Energy Supplier Pricing Form')
        st.write("Please fill in all required fields.")
        
        st.write(f"Current working directory: {os.getcwd()}")  # Check directory

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

        # Initial Submit button
        if st.button("Submit"):
            st.session_state.confirm_submit = True

    # Confirmation dialog logic
    if st.session_state.confirm_submit:
        st.write("### Are you sure you want to submit?")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Yes, submit"):
                submit_form()

        with col2:
            if st.button("No, go back"):
                st.session_state.confirm_submit = False

# Show thank you message after submission
if st.session_state.submitted:
    st.title("Thank You!")
    st.write("Your submission has been received.")
