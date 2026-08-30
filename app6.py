# ============================================================
# TRAFFIC ACCIDENT RISK PREDICTION
# STREAMLIT APPLICATION
# ============================================================

import streamlit as st
import pandas as pd
import pickle


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(

    page_title="Traffic Accident Risk Prediction",

    page_icon="🚗",

    layout="wide"

)


# ============================================================
# LOAD MODEL
# ============================================================



model = model = pickle.load(open("Traffic_accidentrisk_model.pkl","rb"))


# ============================================================
# TITLE
# ============================================================

st.title(
    "🚗🚦 Traffic Accident Risk Prediction"
)

st.write(
    "Enter Driver, Vehicle, Road and Environmental "
    "Conditions To Predict Accident Risk."
)


st.divider()


# ============================================================
# DRIVER INFORMATION
# ============================================================

st.subheader(
    "👤 Driver Information"
)


col1, col2, col3 = st.columns(3)


with col1:

    age = st.number_input(

        "Driver Age",

        min_value=18,

        max_value=100,

        value=30

    )


with col2:

    driver_experience = st.selectbox(

        "Driver Experience",

        [
            "Beginner",
            "Intermediate",
            "Experienced"
        ]

    )


with col3:

    driver_distraction = st.selectbox(

        "Driver Distraction",

        [
            "No",
            "Yes"
        ]

    )


# ============================================================
# VEHICLE INFORMATION
# ============================================================

st.subheader(
    "🚘 Vehicle Information"
)


col1, col2, col3 = st.columns(3)


with col1:

    vehicle_type = st.selectbox(

        "Vehicle Type",

        [
            "Car",
            "Bike",
            "Truck",
            "Bus"
        ]

    )


with col2:

    vehicle_speed = st.number_input(

        "Vehicle Speed",

        min_value=0.0,

        max_value=250.0,

        value=60.0

    )


with col3:

    number_of_vehicles = st.number_input(

        "Number of Vehicles",

        min_value=1,

        max_value=100,

        value=3

    )


# ============================================================
# ROAD INFORMATION
# ============================================================

st.subheader(
    "🛣️ Road Information"
)


col1, col2, col3 = st.columns(3)


with col1:

    road_type = st.selectbox(

        "Road Type",

        [
            "Highway",
            "Urban",
            "Rural",
            "Intersection"
        ]

    )


with col2:

    road_condition = st.selectbox(

        "Road Condition",

        [
            "Dry",
            "Wet",
            "Icy",
            "Damaged"
        ]

    )


with col3:

    road_width = st.number_input(

        "Road Width",

        min_value=1.0,

        max_value=100.0,

        value=10.0

    )


# ============================================================
# TRAFFIC INFORMATION
# ============================================================

st.subheader(
    "🚦 Traffic Information"
)


col1, col2, col3 = st.columns(3)


with col1:

    traffic_density = st.number_input(

        "Traffic Density",

        min_value=0.0,

        max_value=1000.0,

        value=70.0

    )


with col2:

    traffic_control = st.selectbox(

        "Traffic Control",

        [
            "Signal",
            "Stop Sign",
            "None",
            "Other"
        ]

    )


with col3:

    junction_type = st.selectbox(

        "Junction Type",

        [
            "None",
            "T-Junction",
            "Crossroad",
            "Roundabout"
        ]

    )


# ============================================================
# ENVIRONMENT INFORMATION
# ============================================================

st.subheader(
    "🌦️ Environmental Information"
)


col1, col2, col3 = st.columns(3)


with col1:

    weather = st.selectbox(

        "Weather",

        [
            "Clear",
            "Rain",
            "Fog",
            "Storm"
        ]

    )


with col2:

    temperature = st.number_input(

        "Temperature",

        min_value=-50.0,

        max_value=60.0,

        value=28.0

    )


with col3:

    visibility = st.number_input(

        "Visibility",

        min_value=0.0,

        max_value=100.0,

        value=10.0

    )


col1, col2, col3 = st.columns(3)


with col1:

    rainfall = st.number_input(

        "Rainfall",

        min_value=0.0,

        max_value=1000.0,

        value=0.0

    )


with col2:

    lighting = st.selectbox(

        "Lighting",

        [
            "Daylight",
            "Street Light",
            "Dark"
        ]

    )


with col3:

    area_type = st.selectbox(

        "Area Type",

        [
            "Urban",
            "Rural",
            "Residential",
            "Commercial"
        ]

    )


# ============================================================
# OTHER INFORMATION
# ============================================================

st.subheader(
    "📅 Other Conditions"
)


col1, col2, col3 = st.columns(3)


with col1:

    day_of_week = st.selectbox(

        "Day of Week",

        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]

    )


with col2:

    hour = st.number_input(

        "Hour",

        min_value=0,

        max_value=23,

        value=18

    )


with col3:

    historical_accidents = st.number_input(

        "Historical Accidents",

        min_value=0,

        max_value=100,

        value=2

    )


alcohol_involved = st.selectbox(

    "Alcohol Involved",

    [
        "No",
        "Yes"
    ]

)


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()


if st.button(

    "🔮 🚨 PREDICT ACCIDENT RISK",
            use_container_width=True


):

    # ========================================================
    # CREATE INPUT DATAFRAME
    # ========================================================

    input_data = pd.DataFrame({

        "weather": [
            weather
        ],

        "driver_distraction": [
            driver_distraction
        ],

        "driver_experience": [
            driver_experience
        ],

        "historical_accidents": [
            historical_accidents
        ],

        "road_width": [
            road_width
        ],

        "alcohol_involved": [
            alcohol_involved
        ],

        "road_condition": [
            road_condition
        ],

        "junction_type": [
            junction_type
        ],

        "number_of_vehicles": [
            number_of_vehicles
        ],

        "traffic_control": [
            traffic_control
        ],

        "vehicle_type": [
            vehicle_type
        ],

        "age": [
            age
        ],

        "vehicle_speed": [
            vehicle_speed
        ],

        "hour": [
            hour
        ],

        "lighting": [
            lighting
        ],

        "area_type": [
            area_type
        ],

        "rainfall": [
            rainfall
        ],

        "day_of_week": [
            day_of_week
        ],

        "temperature": [
            temperature
        ],

        "visibility": [
            visibility
        ],

        "road_type": [
            road_type
        ],

        "traffic_density": [
            traffic_density
        ]

    })


    # ========================================================
    # ENSURE COLUMN ORDER
    # ========================================================

    expected_columns = (
        model
        .named_steps[
            "preprocessor"
        ]
        .feature_names_in_
        .tolist()
    )


    input_data = input_data[
        expected_columns
    ]


    # ========================================================
    # PREDICTION
    # ========================================================

    try:

        prediction = model.predict(
            input_data
        )[0]


        # ====================================================
        # PROBABILITY
        # ====================================================

        probability = model.predict_proba(
            input_data
        )[0]


        # ====================================================
        # DISPLAY RESULT
        # ====================================================

        st.subheader(
            "Prediction Result"
        )


        if str(prediction).lower() in [
            "high",
            "1",
            "true"
        ]:

            st.error(
                "🔴 HIGH ACCIDENT RISK"
            )

        else:

            st.success(
                "🟢 LOW ACCIDENT RISK"
            )


        # ====================================================
        # PROBABILITY
        # ====================================================

        classes = (
            model
            .named_steps[
                "classifier"
            ]
            .classes_
        )


        st.subheader(
            "Prediction Probability"
        )


        for class_name, prob in zip(
            classes,
            probability
        ):

            st.write(
                f"{class_name}: "
                f"{prob * 100:.2f}%"
            )


        # ====================================================
        # SHOW INPUT
        # ====================================================

        with st.expander(
            "View Input Data"
        ):

            st.dataframe(
                input_data
            )


    except Exception as e:

        st.error(
            "Prediction Error"
        )

        st.exception(e)