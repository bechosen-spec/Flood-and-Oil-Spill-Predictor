import streamlit as st

def main():
    # Custom CSS for styling the page
    st.markdown(
        """
        <style>
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

        /* Main page custom styles */
        .main { 
            background-color: #f9f9f9; 
            padding: 20px; 
            border-radius: 10px; 
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
        }

        /* Headings with white color */
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

        a { 
            font-weight: bold; 
            color: #0056d6;
        }

        a:hover {
            text-decoration: underline;
            color: #0041a3; /* Change color on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # About page title
    st.title("ℹ️ About the Flood & Oil Spillage Prediction App")

    # Introduction
    st.markdown("""
    Welcome to the **Flood & Oil Spillage Prediction App**, your comprehensive tool for assessing environmental risks. This application leverages cutting-edge technology to:
    - **Predict Flood Susceptibility** using topographical and hydrological data.
    - **Analyze Oil Spillage Risks** with detailed severity evaluations.
    - **Generate Alerts** to notify stakeholders about potential disasters.
    """)

    # Vision and Purpose
    st.subheader("🌟 Vision and Purpose")
    st.markdown("""
    Our goal is to empower communities, organizations, and disaster management authorities with actionable insights, enabling them to:
    - Prepare effectively for flood risks.
    - Mitigate the environmental impact of oil spillages.
    - Take proactive measures to ensure safety and sustainability.

    By combining machine learning models with user-friendly tools, we aim to make disaster management more efficient and accessible.
    """)

    # Features
    st.subheader("🚀 Features")
    st.markdown("""
    1. **Flood Prediction**:
       - Input hydrological data to predict flood risk levels.
       - Assess susceptibility: **Low**, **Moderate**, **High**, or **Very High**.

    2. **Oil Spillage Risk Assessment**:
       - Provide facility and location details to estimate spill quantities.
       - Receive danger status for immediate action.

    3. **Generate Alerts**:
       - Notify stakeholders about high-risk scenarios.
       - Use alerts to coordinate emergency responses.

    4. **User-Friendly Interface**:
       - Intuitive design for seamless navigation.
       - Accessible on both desktop and mobile devices.
    """)

    # Footer
    st.markdown("""
    ---
    🌍 *Together, we can build a safer and more sustainable future.*
    """)

