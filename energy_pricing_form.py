import streamlit as st
import pandas as pd
import os

print("Script started.")  # First point of execution

# Initialize the session state for submission tracking
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

print("Session state initialized.")  # Confirm session state initialization

# File to save the data
data_file = '/Users/jeronimocamou/Downloads/Stanwich_Energy/supplier_data.xlsx'

# Check if the directory exists
if os.path.exists('/Users/jeronimocamou/Downloads/Stanwich_Energy'):
    print("Directory exists.")
else:
    print("Directory does not exist. Creating directory.")
    os.makedirs('/Users/jeronimocamou/Downloads/Stanwich_Energy')

def save_data(data):
    print(f"Attempting to save file to: {data_file}")
    try:
        # Check if the Excel file exists
        if os.path.exists(data_file):
            print("File exists. Appending data.")
            # Load existing data
            df = pd.read_excel(data_file)
            # Append new data
            df = df.append(data, ignore_index=True)
        else:
            print("File does not exist. Creating new file.")
            # Create new DataFrame
            df = pd.DataFrame([data])
        
        # Save the data to Excel
        df.to_excel(data_file, index=False)
        print(f"Data successfully saved to {data_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def submit_form():
    print("Form submitted.")  # Confirm form submission
    st.session_state.submitted = True
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

# Display form if not submitted
if not st.session_state.submitted:
    print("Displaying form.")  # Confirm form display
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
    submitted = st.button("Submit", on_click=submit_form)

# Show thank you message if submitted
if st.session_state.submitted:
    st.write("### Thank you for your submission!")

 


