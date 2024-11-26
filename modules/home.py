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
        h1, h2, h3 { 
            color: #0041a3; 
        }
        p { 
            font-size: 16px; 
            color: #333333; 
        }
        .stButton > button { 
            background-color: #0056d6; 
            color: white; 
            border-radius: 10px; 
        }
        .stButton > button:hover { 
            background-color: #0041a3; 
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

    # Subheading for navigation
    st.subheader("Quick Navigation")
    st.markdown("""
    - **🏠 Home:** Learn about the app's purpose.
    - **ℹ️ About:** Discover more about its features.
    - **📞 Contact Us:** Reach out for support or inquiries.
    - **🔐 Login:** Access your account to start predictions.
    - **⚠️ Generate Alert:** Notify stakeholders based on prediction results.
    """)

    # Add a visual divider
    st.markdown("---")

    # Call to action
    st.markdown("""
    ### Ready to Get Started?  
    - [🔐 Login](#login) if you already have an account.
    - [📝 Sign Up](#signup) to create a new account and begin exploring.
    """)

    # Footer
    st.markdown("""
    ---
    🌍 *Your trusted partner in environmental disaster management.*
    """)
