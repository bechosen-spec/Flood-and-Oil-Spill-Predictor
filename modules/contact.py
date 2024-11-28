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
