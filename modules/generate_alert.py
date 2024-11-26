import streamlit as st
import requests
import urllib.parse

def main():
    # Ensure the user is logged in
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.warning("Please log in to access this page.")
        st.stop()

    # Title and introduction
    st.title("⚠️ Generate Alerts with WhatsApp Notifications")
    st.markdown("""
    Use this tool to generate alerts and notify relevant stakeholders via WhatsApp for:
    - **Flood Susceptibility**: Highlight areas at risk of flooding.
    - **Oil Spillage Risk**: Notify about spill incidents and danger assessments.
    """)

    # Sidebar for task selection
    alert_task = st.sidebar.radio("Choose Alert Type", ["Flood Alert", "Oil Spillage Alert"])

    # CallMeBot API setup
    api_url = "https://api.callmebot.com/whatsapp.php"
    api_key = "8595808"  # Replace with your actual API key
    default_phone_number = "2348105994390"  # Replace with your default phone number

    # Helper function to send WhatsApp messages
    def send_whatsapp_message(phone_number, message):
        try:
            # Encode the message for URL compatibility
            encoded_message = urllib.parse.quote(message)
            response = requests.get(f"{api_url}?phone={phone_number}&text={encoded_message}&apikey={api_key}")
            
            # Check if the API request was successful
            if response.status_code == 200:
                return True, f"Message sent successfully to {phone_number}."
            elif response.status_code == 403:
                return False, (
                    "Failed to send message. Error: 403 Forbidden. "
                    "This could be due to an invalid API key, an unregistered phone number, "
                    "or exceeding the allowed rate limit. Please check your CallMeBot account."
                )
            else:
                return False, f"Failed to send message. Error: {response.status_code} - {response.text}"
        except Exception as e:
            return False, f"An error occurred: {str(e)}"

    # Generate Flood Alert
    if alert_task == "Flood Alert":
        st.subheader("🏞️ Generate Flood Alert")
        st.markdown("Provide the details below to create a flood alert and notify people in the area via WhatsApp.")

        # Input fields for flood alert
        location = st.text_input("Location Name")
        predicted_level = st.selectbox(
            "Predicted Flood Susceptibility Level",
            ["Low", "Moderate", "High", "Very High"]
        )
        additional_details = st.text_area("Additional Details (Optional)")
        phone_numbers = st.text_area(
            "Enter phone numbers (comma-separated)",
            placeholder="e.g., 2348105994390, 2347012345678"
        )

        # Generate Alert and Send WhatsApp button
        if st.button("⚠️ Generate and Notify"):
            if location and predicted_level and phone_numbers:
                # Create the alert message
                alert_message = f"🚨 Flood Alert 🚨\nLocation: {location}\nRisk Level: {predicted_level}"
                if additional_details:
                    alert_message += f"\nDetails: {additional_details}"
                
                # Send messages to each phone number
                phone_numbers_list = [num.strip() for num in phone_numbers.split(",")]
                for phone_number in phone_numbers_list:
                    success, feedback = send_whatsapp_message(phone_number, alert_message)
                    st.write(feedback)
            else:
                st.error("Please provide all required information (Location, Risk Level, and Phone Numbers).")

    # Generate Oil Spillage Alert
    elif alert_task == "Oil Spillage Alert":
        st.subheader("🛢️ Generate Oil Spillage Alert")
        st.markdown("Provide the details below to create an oil spillage alert and notify people in the area via WhatsApp.")

        # Input fields for oil spillage alert
        location = st.text_input("Facility or Location Name")
        estimated_quantity = st.number_input("Predicted Spill Quantity (liters)", min_value=0.0, step=0.1)
        danger_status = st.selectbox(
            "Danger Assessment",
            ["No Danger", "Danger"]
        )
        additional_details = st.text_area("Additional Details (Optional)")
        phone_numbers = st.text_area(
            "Enter phone numbers (comma-separated)",
            placeholder="e.g., 2348105994390, 2347012345678"
        )

        # Generate Alert and Send WhatsApp button
        if st.button("⚠️ Generate and Notify"):
            if location and estimated_quantity >= 0 and phone_numbers:
                # Create the alert message
                alert_message = f"🚨 Oil Spillage Alert 🚨\nLocation: {location}\nEstimated Quantity: {estimated_quantity:.2f} liters\nDanger: {danger_status}"
                if additional_details:
                    alert_message += f"\nDetails: {additional_details}"
                
                # Send messages to each phone number
                phone_numbers_list = [num.strip() for num in phone_numbers.split(",")]
                for phone_number in phone_numbers_list:
                    success, feedback = send_whatsapp_message(phone_number, alert_message)
                    st.write(feedback)
            else:
                st.error("Please provide all required information (Location, Spill Quantity, and Phone Numbers).")

    # Footer
    st.markdown("""
    ---
    🌍 *Proactively manage environmental risks with timely alerts.*
    """)

