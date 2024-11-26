import streamlit as st
import pandas as pd
import os

# File path to store user credentials
USER_DATA_FILE = "data/users.csv"

# Ensure user data file exists
if not os.path.exists(USER_DATA_FILE):
    pd.DataFrame(columns=["Username", "Password"]).to_csv(USER_DATA_FILE, index=False)

def main():
    # Login Page Content
    st.title("🔐 Login")
    st.markdown("Welcome back! Please log in to access the app's features.")

    # Input fields for login
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Sign In"):
        if username and password:
            # Load user data
            users = pd.read_csv(USER_DATA_FILE)
            
            # Check if the username exists
            if username in users["Username"].values:
                # Verify password
                stored_password = users[users["Username"] == username]["Password"].iloc[0]
                if password == stored_password:
                    st.success(f"Welcome back, {username}!")
                    # Set session state for logged-in user
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.session_state["redirect_to"] = "Predictions"  # Set redirection flag
                else:
                    st.error("Incorrect password. Please try again.")
            else:
                st.error("Username not found. Please sign up first.")
        else:
            st.error("Both fields are required.")

    # Link to Sign Up Page
    st.markdown("Don't have an account? [Sign Up](#sign-up)")

    # Optional logged-in state check for debugging
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        st.info(f"You're currently logged in as: {st.session_state['username']}.")
