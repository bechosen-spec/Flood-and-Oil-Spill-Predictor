import streamlit as st
import pandas as pd
import os

# File path to store user credentials
USER_DATA_FILE = "data/users.csv"

# Ensure user data file exists
if not os.path.exists(USER_DATA_FILE):
    pd.DataFrame(columns=["Username", "Password"]).to_csv(USER_DATA_FILE, index=False)

def main():
    # Sign-Up Page Content
    st.title("📝 Sign Up")
    st.markdown("Create a new account to access the app's features.")

    # Input fields for sign up
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    # Sign-Up button
    if st.button("Sign Up"):
        if username and password and confirm_password:
            # Load user data
            users = pd.read_csv(USER_DATA_FILE)

            # Check if the username already exists
            if username in users["Username"].values:
                st.error("Username already exists. Please choose another one.")
            elif password != confirm_password:
                st.error("Passwords do not match. Please try again.")
            else:
                # Add new user to the file
                new_user = pd.DataFrame({"Username": [username], "Password": [password]})
                new_user.to_csv(USER_DATA_FILE, mode="a", header=False, index=False)
                
                # Set session state to indicate the user is logged in
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                
                # Redirect user to the Predictions page
                st.session_state["redirect_to"] = "Predictions"  # Set the redirect flag
                
                st.success(f"Account created successfully! Welcome, {username}.")
                
                # Stop the app to process the redirection
                st.stop()
        else:
            st.error("All fields are required.")
