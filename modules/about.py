import streamlit as st

def main():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .main { 
            background-color: #f9f9f9; 
            padding: 20px; 
            border-radius: 10px; 
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
        }
        h1, h2, h3 { color: #0041a3; }
        p { font-size: 16px; color: #333333; }
        .stButton > button { background-color: #0056d6; color: white; border-radius: 10px; }
        .stButton > button:hover { background-color: #0041a3; }
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

    # Call to Action
    st.subheader("🔍 Explore More")
    st.markdown("""
    - [🏠 Home](#home): Return to the landing page.
    - [📞 Contact Us](#contact): Reach out for inquiries or support.
    - [🔐 Login](#login): Log in to start using the app.
    """)

    # Footer
    st.markdown("""
    ---
    🌍 *Together, we can build a safer and more sustainable future.*
    """)

