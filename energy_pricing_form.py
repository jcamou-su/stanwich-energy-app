import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Initialize session state for submission tracking and confirmation dialog
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'confirm_submit' not in st.session_state:
    st.session_state.confirm_submit = False

# Google Sheets authentication
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Your Google Sheet Name").sheet1  # Replace with your sheet name

# Function to save data to Google Sheets
def save_data_to_gsheet(data):
    try:
        sheet.append_row(data)
        return True
    except Exception as e:
        st.error(f"An error occurred while saving the data to Google Sheets: {e}")
        return False

# Form submission logic
def submit_form():
    data = [
        st.session_state.supplier,
        st.session_state.price1,
        st.session_state.price2,
        st.session_state.price3,
        st.session_state.price4,
        st.session_state.price5,
        st.session_state.price6,
        st.session_state.price7,
        st.session_state.price8
    ]
    if save_data_to_gsheet(data):
        st.session_state.submitted = True
        st.session_state.confirm_submit = False

# Display form or thank you message based on submission state
if not st.session_state.submitted:
    if not st.session_state.confirm_submit:
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
                st.experimental_rerun()  # Force immediate rerun to display only the thank you message

        with col2:
            if st.button("No, go back"):
                st.session_state.confirm_submit = False

# Show thank you message after submission
if st.session_state.submitted:
    st.title("Thank You!")
    st.write("Your submission has been received.")
