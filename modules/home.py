import streamlit as st

def main():
    # Custom CSS for styling the page
    st.markdown(
        """
        <style>
        /* Main page custom styles */
        .main { 
            background-color: #f9f9f9; 
            padding: 20px; 
            border-radius: 10px; 
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
        }

        h1, h2, h3 { 
            color: #ffffff;  /* White headers */
        }

        p { 
            font-size: 16px; 
            color: #333333;  /* Body text with a darker color */
        }

        .stButton > button { 
            background-color: #0056d6; 
            color: white; 
            border-radius: 10px; 
        }

        .stButton > button:hover { 
            background-color: #0041a3; 
        }

        /* Sidebar background color */
        .css-1d391kg {  /* Sidebar container */
            background-color: #000000;  /* Black background */
        }

        /* Sidebar items (Menu text) */
        .css-1k0s5h0 {  /* Sidebar item text */
            color: #ffffff;  /* White text for readability */
            font-size: 18px;
        }

        /* Hover effect for sidebar items */
        .css-1k0s5h0:hover {
            color: #FF6347;  /* Change text color to tomato on hover */
        }

        /* Sidebar radio button style */
        .stRadio>label {
            color: white !important; /* Ensure label text is white */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # App title and description
    st.title("🌊 Flood & Oil Spillage Prediction App")
    st.markdown("""
    Welcome to the **Flood & Oil Spillage Prediction App**!  
    Use this platform to:
    - Predict **Flood Susceptibility** based on environmental factors.
    - Assess **Oil Spillage Risks** and their severity.
    - Generate **Alerts** to inform stakeholders of potential disasters.
    """)

    # Main content of the homepage (without quick navigation)
    st.markdown("### Welcome to the Home Page")
    st.markdown("""
    This app is a tool for predicting flood risks based on environmental data and assessing oil spillage risks.
    You can navigate through the app using the sidebar on the left to explore the various features such as:
    - Predicting flood risks and oil spillage risks
    - Generating alerts for potential disasters
    - Contacting us for support or inquiries
    - Logging in to access advanced features.
    """)

    # Footer
    st.markdown("""
    ---
    🌍 *Your trusted partner in environmental disaster management.*
    """)

