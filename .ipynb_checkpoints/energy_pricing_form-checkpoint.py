import streamlit as st

# Title of the form
st.title('Energy Supplier Pricing Form')

# Instructions
st.write("Please fill in all required fields.")

# Form fields for input
with st.form("supplier_form"):
    price1 = st.number_input('Enter Price 1', min_value=0.0, format="%.6f")
    price2 = st.number_input('Enter Price 2', min_value=0.0, format="%.6f")
    price3 = st.number_input('Enter Price 3', min_value=0.0, format="%.6f")
    price4 = st.number_input('Enter Price 4', min_value=0.0, format="%.6f")
    price5 = st.number_input('Enter Price 5', min_value=0.0, format="%.6f")
    price6 = st.number_input('Enter Price 6', min_value=0.0, format="%.6f")
    price7 = st.number_input('Enter Price 7', min_value=0.0, format="%.6f")
    price8 = st.number_input('Enter Price 8', min_value=0.0, format="%.6f")

    # Submit button
    submitted = st.form_submit_button("Submit")

# Perform calculations and display results
if submitted:
    total_price = sum([price1, price2, price3, price4, price5, price6, price7, price8])
    avg_price = total_price / 8

    st.write("### Calculated Prices")
    st.write(f"Total Price: ${total_price:.2f}")
    st.write(f"Average Price: ${avg_price:.2f}")

# Footer
st.write("Ensure all fields are filled before submission.")

# Clear the form and show a thank you message
st.write("### Thank you for your submission!")
    