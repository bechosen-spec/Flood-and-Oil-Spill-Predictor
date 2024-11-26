import streamlit as st
import pandas as pd
import os

def main():
    USER_DATA_FILE = "data/users.csv"

    # Ensure the CSV file exists and has the correct structure
    if not os.path.exists(USER_DATA_FILE) or os.stat(USER_DATA_FILE).st_size == 0:
        # Create the file with headers if it doesn't exist or is empty
        pd.DataFrame(columns=["Username", "Password"]).to_csv(USER_DATA_FILE, index=False)

    st.title("📝 Sign Up")
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if username and password and confirm_password:
            if password == confirm_password:
                try:
                    users = pd.read_csv(USER_DATA_FILE)  # Load the users file
                    if username in users["Username"].values:
                        st.error("Username already exists.")
                    else:
                        # Append the new user to the CSV file
                        new_user = pd.DataFrame({"Username": [username], "Password": [password]})
                        new_user.to_csv(USER_DATA_FILE, mode="a", header=False, index=False)
                        
                        # Set session state for logged-in user
                        st.session_state["logged_in"] = True
                        st.session_state["username"] = username
                        st.session_state["redirect_to_predictions"] = True  # Set redirection flag
                        
                        # Show success message and redirect
                        st.success("Sign up successful! Redirecting to the Predictions page...")
                        st.rerun()  # Reload the app
                except Exception as e:
                    st.error(f"An error occurred while processing your request: {e}")
            else:
                st.error("Passwords do not match.")
        else:
            st.error("All fields are required.")
