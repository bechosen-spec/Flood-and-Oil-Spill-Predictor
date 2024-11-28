import streamlit as st
import base64  # For encoding the background image
from modules import home, about, contact, login, signup, prediction, generate_alert

# Page configuration - must be the first Streamlit command
st.set_page_config(
    page_title="Flood & Oil Spillage Prediction App",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to set the background image
def set_background(image_file):
    try:
        with open(image_file, "rb") as image:
            encoded_string = base64.b64encode(image.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/jpeg;base64,{encoded_string});
                background-size: cover;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error(f"Background image '{image_file}' not found. Please check the path.")

# Set the background image
set_background("assets/background.jpeg")  # Ensure the path is correct and the image exists

# Handle login redirection
if "redirect_to" in st.session_state:
    redirect_to = st.session_state["redirect_to"]
    del st.session_state["redirect_to"]  # Remove the redirection flag
    if redirect_to == "Predictions":
        prediction.main()
        st.stop()

# Sidebar navigation
with st.sidebar:
    selected = st.radio(
        "Main Menu",
        ["Home", "About", "Contact Us", "Login", "Sign Up", "Predictions", "Generate Alert"]
    )

# Sidebar styling
st.markdown(
    """
    <style>
    .css-1d391kg {  /* Sidebar container */
        background-color: #000000;  /* Black background */
    }

    .css-1k0s5h0 {  /* Sidebar item text */
        color: #ffffff;  /* White text for readability */
        font-size: 18px;
    }

    .css-1k0s5h0:hover {
        color: #FF6347;  /* Change text color to tomato on hover */
    }

    .stRadio>label {
        color: white !important; /* Ensure label text is white */
    }
    </style>
    """, unsafe_allow_html=True
)

# Logout logic
def logout():
    # Clear session state variables related to the user
    if "logged_in" in st.session_state:
        del st.session_state["logged_in"]
    if "username" in st.session_state:
        del st.session_state["username"]
    st.success("You have logged out successfully!")
    
    # Set redirect to Home page
    st.session_state["redirect_to"] = "Home"
    
    # Stop the app execution (this will be picked up when the app reruns)
    st.stop()

# Display the logout button if the user is logged in
if "logged_in" in st.session_state and st.session_state["logged_in"]:
    if st.sidebar.button("Log Out"):
        logout()

# Navigation Logic
if selected == "Home":
    home.main()
elif selected == "About":
    about.main()
elif selected == "Contact Us":
    contact.main()
elif selected == "Login":
    login.main()
elif selected == "Sign Up":
    signup.main()
elif selected == "Predictions":
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        prediction.main()
    else:
        st.warning("You need to log in to access the Predictions page.")
elif selected == "Generate Alert":
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        generate_alert.main()
    else:
        st.warning("You need to log in to access the Generate Alert page.")

# Footer
st.markdown("---")
st.markdown("🌍 *Proactively managing environmental risks for a safer future.*")
