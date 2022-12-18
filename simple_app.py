# A simple Streamlit app for Food Ordering

import streamlit as st


food_items_dict = {
    "Burger": 50,
    "Pizza": 100,
    "Pasta": 150,
    "Sandwich": 200,
    "French Fries": 100,
}

# Title
st.title("Food Ordering App")

# Text Input for Name
name = st.text_input("Enter your name")

# Text Input for Address
address = st.text_input("Enter your address")

# Distance from the restaurant
distance = st.slider("Distance from the restaurant in KM", 0, 10)

if distance > 5:
    st.write("Sorry, we do not deliver beyond 5 KM")

# Multi-Selectbox for food items
if distance <= 5:
    food_items = st.multiselect("Select your food items", ["Burger", "Pizza", "Pasta", "Sandwich", "French Fries"])

    # Button
    button = st.button("Place Order")
    if button:
        total = 0
        for item in food_items:
            total = total + food_items_dict[item]

        st.write("Your order has been placed and the total amount is {}".format(total))

