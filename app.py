import numpy as np
import pandas as pd
import streamlit as st
import joblib


# Loading the trained model

model = joblib.load("claim_model.pkl")


st.set_page_config(
    page_title="Insurance Claim Prediction",
    page_icon="🎗️",
    layout="wide"
)


st.markdown("""

<style>

.stApp {
    background: linear-gradient(#FADADD, #CAF1DE, grey);
    border: solid;
    border-color: black;
    margin-top: -15px;
}

h1 {
    color: Violet;
    font-size: 24px;
    text-align: center;
    margin-top: -15px;
}

.stApp p, .stApp label {
    color: Black;
    font-weight: bold;
    font-size: 19px;
}

.stButton > button:hover {
    background: linear-gradient(90deg,  Green);
    color: white;
    border: none;
    transform: scale(1.03);
}






</style>

""", unsafe_allow_html=True)


st.title("Insurance Claim Prediction")

st.write("Enter customer and vehicle details.")


# ROW 1
col1, col2, col3 = st.columns(3)


with col1:

    customer_age = st.slider(
        "customer_age",
        min_value=18,
        max_value=89,
        value=30
    )


with col2:

    vehicle_age = st.slider(
        "vehicle_age",
        min_value=0,
        max_value=30,
        value=3
    )


with col3:

    subscription_length = st.slider(
        "subscription length",
        min_value=0.0,
        max_value=20.0,
        value=1.0
    )

# ROW 2

col1, col2, col3 = st.columns(3)


with col1:

    region_density = st.slider(
        "Region Density",
        min_value=0,
        max_value=100000,
        value=5000
    )


with col2:

    fuel_type = st.selectbox(
        "Fuel Type",
        [0, 1, 2]
    )


with col3:

    vehicle_model = st.selectbox(
        "Model",
        [
            "M1",
            "M2",
            "M3",
            "M4",
            "M5",
            "M6",
            "M7",
            "M8",
            "M9"
        ]
    )

# ROW 3

col1, col2, col3 = st.columns(3)


with col1:

    cylinders = st.number_input(
        "Cylinder",
        min_value=0,
        max_value=4,
        value=2
    )


with col2:

    region_code = st.selectbox(
        "Region Code",
        ["C1", "C2", "C3","C4", "C5", "C6", "C7","C8","C9","C10", "C11", "C12","C13"]
    )


with col3:

    length = st.slider(
        "Length", min_value=2000, max_value=4500, value=3445
    )

# ROW 4

col1, col2, col3 = st.columns(3)


with col1:

    engine_type = st.selectbox(
        "Engine Type",
        ["1.5 L U2 CRDi","i-DTEC","F8D Petrol Engine","1.5 Turbocharged Revotorq",
         "1.2 L K Series Engine", "K Series Dual jet","K10C","1.0 SCe","1.2 L K12N Dualjet",
         "G12B","1.5 Turbocharged Revotron"]
    )


with col2:
    transmission_type = st.selectbox(
        "Transmission Type",["Automatic","Manual"]
    )


with col3:

    steering_type = st.selectbox(
        "Steering type",["Power","Manual"]
    )


# ROW 5

col1, col2, col3 = st.columns(3)


with col1:

    turning_radius = st.slider(
        "turning_radius", min_value=0.1, max_value=5.2, value=1.6
    )


with col2:

    width = st.slider(
        "width", min_value=1400, max_value=2000, value=1515
    )
with col3:

    gross_weight = st.slider(
        "gross_weight", min_value=500, max_value=5000, value=1000
    )

# ROW 6

col1, col2, col3 = st.columns(3)


with col1:

    is_rear_window_defogger = st.selectbox(
        "is_rear_window_defogger",[0, 1]
    )


with col2:

    is_front_fog_lights = st.selectbox(
        "is_front_fog_lights", [0, 1]
    )


with col3:

    is_rear_window_wiper = st.selectbox(
        "is_rear_window_wiper", [0, 1]
    )


# ROW 7

col1, col2, col3 = st.columns(3)


with col1:

    airbags = st.number_input(
        "Airbags", min_value=0, max_value=10, value=2
    )

with col2:

    is_esc = st.selectbox(
        "is_esc", [0, 1]
    )

with col3:

    is_tpms = st.selectbox(
        "is_tpms", [0, 1]
    )

# ROW 8

col1, col2, col3 = st.columns(3)


with col1:

    is_adjustable_steering = st.selectbox(
        "is_adjustable_steering",
        [0, 1]
    )


with col2:

    is_parking_sensors = st.selectbox(
        "is_parking_sensors",
        [0, 1]
    )


with col3:

    is_parking_camera = st.selectbox(
        "is_parking_camera",
        [0, 1]
    )


# ROW 9

col1, col2, col3 = st.columns(3)


with col1:

    rear_brakes_type = st.selectbox(
        "rear_brakes_type",
        [
            "Drum",
            "Disc"
        ]
    )


with col2:

    displacement = st.number_input(
        "displacement", min_value=500, max_value=5000, value=1200
    )


with col3:

    ncap_rating = st.number_input(
        "ncap_rating", min_value=0, max_value=5, value=3
    )

# ROW 10

col1, col2, col3 = st.columns(3)


with col1:

    is_rear_window_washer = st.selectbox(
        "is_rear_window_washer", [0, 1]
    )


with col2:

    is_brake_assist = st.selectbox(
        "is_brake_assist", [0, 1]
    )


with col3:

    is_power_door_locks = st.selectbox(
        "is_power_door_locks", [0, 1]
    )

# ROW 11

col1, col2, col3 = st.columns(3)


with col1:

    is_central_locking = st.selectbox(
        "is_central_locking",[0, 1]
    )


with col2:

    is_power_steering = st.selectbox(
        "is_power_steering", [0, 1]
    )


with col3:

    is_driver_seat_height_adjustable = st.selectbox(
        "is_driver_seat_height_adjustable",
        [0, 1]
    )

# ROW 12

col1, col2, col3 = st.columns(3)


with col1:

    is_day_night_rear_view_mirror = st.selectbox(
        "is_day_night_rear_view_mirror",
        [0, 1]
    )


with col2:

    is_ecw = st.selectbox(
        "is_ecw",
        [0, 1]
    )


with col3:

    is_speed_alert = st.selectbox(
        "is_speed_alert",
        [0, 1]
    )


# ROW 13

col1, col2, col3 = st.columns(3)


with col1:

    segment = st.selectbox(
        "Segment", ["A","B","C", "D","E"]
    )


with col2:

    max_torque = st.number_input(
        "Max Torque",min_value=0.0, max_value=500.0,value=100.0
    )


with col3:

    max_power = st.number_input(
        "Max Power",
        min_value=0.0,
        max_value=500.0,
        value=80.0
    )

# ROW 14

vehicle_age_group = ""

if vehicle_age <= 2:

    vehicle_age_group = "New"

elif vehicle_age <= 7:

    vehicle_age_group = "Medium"

else:

    vehicle_age_group = "Old"


# PREDICT BUTTON

if st.button("Predict Claim"):

    # Created input data

    input_data = pd.DataFrame([{

        "customer_age": customer_age,"vehicle_age": vehicle_age, "subscription_length": subscription_length,
        "region_code": region_code,
        "region_density": region_density, "segment": segment,
        "model": vehicle_model,"fuel_type": fuel_type,"max_torque": max_torque,
        "max_power": max_power, "engine_type": engine_type,

        "airbags": airbags, "is_esc": is_esc,"is_adjustable_steering": is_adjustable_steering,

        "is_tpms": is_tpms,
        "is_parking_sensors": is_parking_sensors,

        "is_parking_camera": is_parking_camera,
        "rear_brakes_type": rear_brakes_type,"displacement": displacement,
        "cylinder": cylinders, "transmission_type": transmission_type,

        "steering_type": steering_type,

        "turning_radius": turning_radius,

        "length": length, "width": width,

        "gross_weight": gross_weight,
        "is_front_fog_lights": is_front_fog_lights,

        "is_rear_window_wiper": is_rear_window_wiper,

        "is_rear_window_washer": is_rear_window_washer,
        "is_rear_window_defogger": is_rear_window_defogger,

        "is_brake_assist": is_brake_assist,

        "is_power_door_locks": is_power_door_locks,

        "is_central_locking": is_central_locking,
        "is_power_steering": is_power_steering,

        "is_driver_seat_height_adjustable": is_driver_seat_height_adjustable,

        "is_day_night_rear_view_mirror": is_day_night_rear_view_mirror,
        "is_ecw": is_ecw,"is_speed_alert": is_speed_alert,"ncap_rating": ncap_rating,
        "vehicle_age_group": vehicle_age_group

    }])


    # Prediction

    prediction = model.predict(input_data)[0]


    # Prediction probability

    probability = model.predict_proba(input_data)[0]

    no_claim_probability = probability[0] * 100

    claim_probability = probability[1] * 100


    st.write(
        "No Claim Probability:",
        round(no_claim_probability, 2),"%"
    )

    st.write(
        "Claim Probability:",
        round(claim_probability, 2),"%"
    )

    if prediction == 1:

        st.warning("Prediction: Claim")

    else:

        st.success("Prediction: No Claim")