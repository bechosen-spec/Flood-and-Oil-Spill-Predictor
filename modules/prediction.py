import streamlit as st
import random
import hashlib
import joblib
from sklearn.ensemble import StackingClassifier

# Define the custom VerboseStackingClassifier class
class VerboseStackingClassifier(StackingClassifier):
    def fit(self, X, y):
        print("Training base estimators...")
        for name, estimator in self.estimators:
            print(f"Training {name}...")
            estimator.fit(X, y)
            print(f"{name} trained.")
        print("Training final estimator...")
        super().fit(X, y)
        print("All estimators trained.")

# Load models (If you had pre-trained models, uncomment this section)
# flood_model = joblib.load("models/flood_model.pkl")
# oilspill_model = joblib.load("models/oilspill_model.pkl")

# Cache for predictions
@st.cache_data
def generate_cached_prediction(input_data, task):
    """
    Generate a cached prediction based on the input data and task.
    """
    input_str = f"{task}:{input_data}"  # Combine task and input for unique key
    cache_key = hashlib.md5(input_str.encode()).hexdigest()  # Generate a hash key

    if task == "Flood Prediction":
        # Generate a random flood susceptibility level
        susceptibility_levels = ["Low", "Moderate", "High", "Very High"]
        return random.choice(susceptibility_levels)
    elif task == "Oil Spillage Prediction":
        # Generate a random estimated quantity and assess danger
        estimated_quantity = random.uniform(0, 5000)  # Example range
        danger_status = "Danger" if estimated_quantity > 1000 else "No Danger"
        return estimated_quantity, danger_status

def main():
    # Ensure the user is logged in
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.warning("Please log in to access this page.")
        st.stop()

    # Title and introduction
    st.title("🌧️ Flood & Oil Spillage Predictions")
    st.markdown(f"Welcome, **{st.session_state['username']}**! Use the tools below to make predictions.")

    # Sidebar for navigation
    task = st.sidebar.radio("Choose a Prediction Task", ["Flood Prediction", "Oil Spillage Prediction"])

    # Flood Prediction Section
    if task == "Flood Prediction":
        st.subheader("🏞️ Flood Susceptibility Prediction")
        st.markdown("""
        Please provide the following environmental parameters for flood susceptibility prediction.
        The more accurate the data, the better the prediction.
        """)

        # Input fields for flood prediction
        col1, col2, col3 = st.columns(3)
        with col1:
            slope = st.number_input("Slope (%)", min_value=0.0, max_value=100.0, step=0.1, help="The slope of the land. Steeper slopes have a higher risk.")
            twi = st.number_input("Topographic Wetness Index (TWI)", step=0.1, help="A measure of how wet the area tends to be.")
            rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=1.0, help="Amount of rainfall in millimeters.")
        with col2:
            curvature = st.number_input("Curvature", min_value=-10.0, max_value=10.0, step=0.1, help="The land's curvature. Higher curvature may indicate more water accumulation.")
            aspect = st.number_input("Aspect (degrees)", min_value=0.0, max_value=360.0, step=1.0, help="The orientation of the slope (e.g., north or south).")
            drainage = st.number_input("Drainage", min_value=0.0, step=0.1, help="The ability of the area to drain water.")
        with col3:
            flow_accumulation = st.number_input("Flow Accumulation (FA)", min_value=0.0, step=1.0, help="A measure of water flow in the area.")

        flood_input_data = [slope, curvature, aspect, twi, rainfall, drainage, flow_accumulation]

        if st.button("🌧️ Predict Flood Susceptibility"):
            predicted_susceptibility = generate_cached_prediction(flood_input_data, "Flood Prediction")
            st.success(f"Flood Susceptibility: **{predicted_susceptibility}**")

            if predicted_susceptibility == "Very High":
                st.warning("⚠️ **Warning**: Flood risk is very high. Prepare for evacuation!")
            elif predicted_susceptibility == "High":
                st.warning("⚠️ **Warning**: High flood risk. Stay alert and prepare.")
            elif predicted_susceptibility == "Moderate":
                st.info("⚠️ **Moderate Risk**: Monitor the situation closely.")
            else:
                st.info("✅ **Safe**: Low flood risk. No immediate action needed.")

    # Oil Spillage Prediction Section
    elif task == "Oil Spillage Prediction":
        st.subheader("🛢️ Oil Spillage Prediction: Estimated Quantity & Danger Assessment")
        st.markdown("""
        Please provide the following parameters to predict the estimated quantity of oil spill and its danger status.
        """)

        col1, col2 = st.columns(2)
        with col1:
            facility_type = st.selectbox(
                "Type of Facility", 
                ["Pipeline", "Well", "Terminal", "Trunkline", "Platform", "Delivery Line", "Tugboat", "SPM"],
                help="The type of oil facility (e.g., pipeline or platform)."
            )
            habitat = st.selectbox(
                "Spill Area Habitat", 
                ["Surface Water", "Land Area", "Intertidal Water", "Other"],
                help="The environment where the spill is likely to occur."
            )
            latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.1, help="Latitude of the oil facility.")
        with col2:
            cause = st.selectbox(
                "Cause of Spill", 
                ["Sabotage", "Equipment Failure", "Corrosion", "Operational Maintenance Error", 
                 "Hacksaw Cut", "Explosion", "Sump Tank Overflow"],
                help="The likely cause of the oil spill."
            )
            longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.1, help="Longitude of the oil facility.")

        oilspill_input_data = [facility_type, cause, habitat, latitude, longitude]

        if st.button("🛢️ Predict Spill Quantity & Danger"):
            estimated_quantity, danger_status = generate_cached_prediction(oilspill_input_data, "Oil Spillage Prediction")
            st.write(f"**Predicted Estimated Quantity:** {estimated_quantity:.2f} liters")
            st.write(f"**Danger Assessment:** {danger_status}")

            if danger_status == "Danger":
                st.warning("⚠️ **Warning**: High spill quantity detected. Immediate response needed!")
            else:
                st.success("✅ **Safe**: Spill quantity is within manageable levels.")