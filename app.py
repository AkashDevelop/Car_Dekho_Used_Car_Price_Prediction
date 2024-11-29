
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import json
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Car Price Prediction App",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url(https://wallpapers.com/images/hd/black-car-4k-wnfjwxcbybpwbs08.jpg);
    background-size: cover;
}

body {
    background-color: #2E2E2E; /* Dark gray background */
    color: #FFFFFF; /* White text for high contrast */
}

.stButton>button {
    background-color: #FF6600; /* Bright orange primary color for buttons */
    color: #FFFFFF; /* White text for buttons */
}

.stSelectbox, .stSlider, .stNumberInput, .stTextInput {
    background-color: #444444; /* Dark gray for input fields */
    color: #FFFFFF; /* White text for inputs */
}

.stCheckbox, .stRadio {
    color: #FFFFFF; /* White text for checkboxes and radios */
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved model and data
model_path = r"E:\CarDeko_used_car_Prediction\Models\gradient_boosting_model_Train.joblib"
model = joblib.load(model_path)

data_path = r"E:\CarDeko_used_car_Prediction\final_combined_dataset\final_cleaned_dataset.joblib"
df = joblib.load(data_path)


st.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <h1 style="font-size: 2.5em; color: #C70039; margin: 0;">🚗 Car Price Prediction App 🚗</h1>
        <p style="font-size: 1.1em; color: #FFFFFF; margin: 0;">Predict car prices and explore the dataset interactively!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
        <div style="box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 10px; background-color: #FAFAFA;">
            <div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div style="text-align: center; margin-top: -10px; margin-bottom: 20px;">
        <h2 style="font-size: 1.8em; color: #C70039;">🔍 Explore Car Filters</h2>
    </div>
    """,
    unsafe_allow_html=True,
)


st.sidebar.title("Filter Options")
st.sidebar.write("🔍 Use the filters below to refine your car search:")

min_price, max_price = st.sidebar.slider(
    "Select Price Range",
    int(df['Car Price'].min()),
    int(df['Car Price'].max()),
    (int(df['Car Price'].min()), int(df['Car Price'].max())),
)

fuel_types = ['All'] + list(df['Fuel Type'].unique())
selected_fuel = st.sidebar.selectbox("Select Fuel Type", fuel_types)

brands = ['All'] + list(df['Car Manufacturer'].unique())
selected_brand = st.sidebar.selectbox("Select Brand", brands)

# Main content (Tabs)
tab1, tab2, tab3 = st.tabs(["🔎 Explore Cars", "💰 Predict Price", "❓ Help & Feedback"])

# Tab 1: Explore Cars
with tab1:
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    lottie_coding = load_lottiefile("E:\CarDeko_used_car_Prediction\Animation - 1732868107827 (1).json")

    # Add Lottie animation
    st_lottie(lottie_coding, speed=1, width=850, height=250, key="car_animation")


    st.markdown(
    """
    <h2 style="text-align: center; color: white;">Welcome to Car Price Prediction App</h2>
    <p style="text-align: center; color: white;">Predict the price of your car based on its features</p>
    """, 
    unsafe_allow_html=True
    )

    st.subheader("Explore the Dataset")

    # Apply filters
    filtered_df = df[
        (df['Car Price'] >= min_price) & (df['Car Price'] <= max_price)
    ]
    if selected_fuel != 'All':
        filtered_df = filtered_df[filtered_df['Fuel Type'] == selected_fuel]
    if selected_brand != 'All':
        filtered_df = filtered_df[filtered_df['Car Manufacturer'] == selected_brand]

    st.markdown("### Filtered Cars")
    if not filtered_df.empty:
        st.dataframe(filtered_df)
    else:
        st.warning("No cars match your criteria. Try adjusting the filters.")

# Tab 2: Predict Price
with tab2:
    st.subheader("Car Price Prediction")

    # User inputs for prediction
    st.markdown("### Enter Car Details")
    year = st.number_input("Year of Manufacture", min_value=1990, max_value=2024, value=2015)
    mileage = st.number_input("Mileage (km/l)", min_value=5.0, max_value=50.0, value=18.0, step=1.0)
    engine = st.number_input("Engine Capacity (cc)", min_value=800, max_value=5000, value=1500, step=10)
    power = st.number_input("Power (bhp)", min_value=20, max_value=500, value=100, step=10)
    seats = st.slider("Number of Seats", min_value=2, max_value=10, value=5)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric"])
    transmission = st.selectbox("Transmission Type", df['Transmission Type'].unique())

    # Predict price
    if st.button("Predict Price"):
        try:
            input_data = pd.DataFrame({
            "Year of Manufacture": [year],
            "Mileage (km/l)": [mileage],
            "Engine Capacity (L)": [engine / 1000],  # Convert from cc to L if the model expects liters
            "Max Power (hp)": [power],
            "Seats Capacity": [seats],
            "Fuel Type": [fuel_type],
            "Transmission Type": [transmission],
            "Car Age (years)": [2024 - year],  # Current year - Year of Manufacture
            "Kilometers Driven": [100000],  # Default value (can be user-defined later)
            "Year of Registration": [year],  # Default: Same as Year of Manufacture
            "Torque (Nm)": [150],  # Default placeholder value
            "Wheel Size (inches)": [15]  # Default placeholder value
        })
        
            predicted_price = model.predict(input_data)
            
            # Display predicted price
            st.success(f"🚗 The predicted price for this car is: ₹ {predicted_price[0]:,.2f}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

    # Add a scatter plot for "Car Price vs. Mileage"
    st.markdown("### Car Price vs. Mileage")
    x_axis = st.selectbox("Select X-axis:", options=["Mileage (km/l)", "Engine Capacity (L)", "Max Power (hp)"])
    y_axis = st.selectbox("Select Y-axis:", options=["Car Price", "Seats Capacity"])
    scatter_fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        color="Fuel Type",
        hover_data=["Car Manufacturer", "Car Model"],  
        title="Price vs. Mileage (Interactive Scatter Plot)"
    )
    st.plotly_chart(scatter_fig, use_container_width=True)

# Tab 3: Help & Feedback
with tab3:
    st.subheader("Help & Support")
    st.write("For more information or help, please contact us at:")
    st.markdown("[support@carpriceprediction.com](mailto:support@carpriceprediction.com)")

    st.subheader("Feedback")
    feedback = st.text_area("We would love to hear your thoughts! Please share your feedback:")
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please provide some feedback before submitting.")

