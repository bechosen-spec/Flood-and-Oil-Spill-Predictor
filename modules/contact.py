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
        p, a { font-size: 16px; color: #333333; }
        a { text-decoration: none; font-weight: bold; }
        a:hover { text-decoration: underline; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Page title
    st.title("📞 Contact Us")

    # Contact Details
    st.markdown("""
    We’re here to help! If you have questions, need assistance, or want to provide feedback, please reach out to us using the information below:

    ### 📧 Email
    For general inquiries:  
    [info@floodoilprediction.com](mailto:info@floodoilprediction.com)

    For support:  
    [support@floodoilprediction.com](mailto:support@floodoilprediction.com)

    ---

    ### ☎️ Phone
    You can reach us Monday to Friday, 9:00 AM to 5:00 PM:  
    +1 (555) 123-4567

    ---

    ### 📍 Address
    Flood & Oil Spillage Prediction Solutions  
    123 EcoTech Lane,  
    Green City, Planet Earth

    ---

    ### 🌐 Social Media
    Follow us on social media to stay updated:  
    - [Twitter](https://twitter.com/floodoilprediction)
    - [LinkedIn](https://linkedin.com/company/floodoilprediction)
    - [Facebook](https://facebook.com/floodoilprediction)
    """)

    # Contact Form (Optional, if functionality needed in the future)
    st.subheader("💬 Leave Us a Message")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if name and email and message:
            st.success("Thank you for reaching out! We’ll get back to you shortly.")
        else:
            st.error("Please fill out all fields before submitting.")

    # Footer
    st.markdown("""
    ---
    🌍 *Together, we can predict and prevent disasters.*
    """)

