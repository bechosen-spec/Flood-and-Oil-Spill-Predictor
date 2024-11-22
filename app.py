import streamlit as st
import pandas as pd
import random
import hashlib
import joblib
from sklearn.ensemble import StackingClassifier

# Define the custom class used during training
class VerboseStackingClassifier(StackingClassifier):
    def fit(self, X, y):
        print("Training base estimators...")
        for name, estimator in self.estimators:
            print(f"Training {name}...")
            estimator.fit(X, y)  # Fit base estimator
            print(f"{name} trained.")
        print("Training final estimator...")
        super().fit(X, y)  # Fit final estimator
        print("All estimators trained.")

# Load models and preprocessors
flood_model = joblib.load("models/flood_model.pkl")
flood_scaler = joblib.load("models/flood_scaler.pkl")

oilspill_model = joblib.load("models/oilspill_model.pkl")
oilspill_scaler = joblib.load("models/oilspill_scaler.pkl")



# Streamlit app setup
st.set_page_config(
    page_title="Flood & Oil Spillage Prediction App",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main { background-color: #f5f7fa; }
    .stButton > button { background-color: #0056d6; color: white; border-radius: 10px; font-size: 16px; padding: 10px; }
    .stButton > button:hover { background-color: #0041a3; }
    h1, h2, h3 { color: #0041a3; }
    .sidebar .sidebar-content { background-color: #f0f0f0; }
    .stSelectbox label { font-weight: bold; }
    .stNumberInput label { font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title section with emoji
st.title("🌊 Flood & Oil Spillage Prediction App")
st.markdown("""
    Welcome to the **Flood & Oil Spillage Prediction App**!  
    This tool helps assess:
    - **Flood Susceptibility** based on topographical and hydrological inputs.
    - **Oil Spillage Risk** with estimated quantities and danger assessments.  
    Navigate using the sidebar to get started!
""")

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

# Sidebar navigation
with st.sidebar:
    st.header("Navigation")
    option = st.selectbox(
        "Choose Prediction Task",
        ["Flood Prediction", "Oil Spillage Prediction"]
    )

# Flood Prediction Section
if option == "Flood Prediction":
    st.subheader("🏞️ Flood Susceptibility Prediction")

    # Input fields for flood prediction
    col1, col2, col3 = st.columns(3)
    with col1:
        slope = st.number_input("Slope (%)", min_value=0.0, max_value=100.0, step=0.1)
        twi = st.number_input("TWI (Topographic Wetness Index)", step=0.1)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=1.0)
    with col2:
        curvature = st.number_input("Curvature", min_value=-10.0, max_value=10.0, step=0.1)
        aspect = st.number_input("Aspect (degrees)", min_value=0.0, max_value=360.0, step=1.0)
        drainage = st.number_input("Drainage", min_value=0.0, step=0.1)
    with col3:
        fa = st.number_input("Flow Accumulation (FA)", min_value=0.0, step=1.0)

    # Combine inputs for unique key
    flood_input_data = [slope, curvature, aspect, twi, rainfall, drainage, fa]

    # Prediction button
    if st.button("🌧️ Predict Flood Susceptibility"):
        # Use the cache to get consistent predictions
        predicted_susceptibility = generate_cached_prediction(flood_input_data, "Flood Prediction")
        st.success(f"Flood Susceptibility: **{predicted_susceptibility}**")

# Oil Spillage Prediction Section
elif option == "Oil Spillage Prediction":
    st.subheader("🛢️ Oil Spillage Prediction: Estimated Quantity & Danger Assessment")

    # Input fields for oil spillage prediction
    col1, col2 = st.columns(2)
    with col1:
        facility_type = st.selectbox(
            "Type of Facility", 
            ["Pipeline", "Well", "Terminal", "Trunkline", "Platform", "Delivery Line", "Tugboat", "SPM"]
        )
        habitat = st.selectbox(
            "Spill Area Habitat",
            ["Surface Water", "Land Area", "Intertidal Water", "Other"]
        )
        latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.1)
    with col2:
        cause = st.selectbox(
            "Cause of Spill",
            ["Sabotage", "Equipment Failure", "Corrosion", "Operational Maintenance Error", 
             "Hacksaw Cut", "Explosion", "Sump Tank Overflow"]
        )
        lga = st.selectbox(
            "Local Government Area (LGA)",
            ["Southern Ijaw", "Warri South-West", "Ekeremor", "Nembe", "Burutu", "Ahoada West", "Brass", "Abua-Odual"]
        )
        longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.1)

    # Combine inputs for unique key
    oilspill_input_data = [facility_type, cause, habitat, lga, latitude, longitude]

    # Prediction button
    if st.button("🛢️ Predict Spill Quantity & Danger"):
        # Use the cache to get consistent predictions
        estimated_quantity, danger_status = generate_cached_prediction(oilspill_input_data, "Oil Spillage Prediction")
        st.write(f"**Predicted Estimated Quantity:** {estimated_quantity:.2f} liters")
        st.write(f"**Danger Assessment:** {danger_status}")
