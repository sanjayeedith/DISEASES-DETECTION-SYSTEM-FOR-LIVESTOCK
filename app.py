import streamlit as st
import pandas as pd
import joblib
import colorsys

# Load the trained decision tree model
model_filename = r"D:\Patent\animal_decision_tree_model.joblib"
model = joblib.load(model_filename)

# Set the background color
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a function to generate pastel colors dynamically
def generate_pastel_color(seed):
    h, l, s = seed, 0.7, 0.9  # You can adjust these values for different pastel shades
    r, g, b = [int(c * 256) for c in colorsys.hls_to_rgb(h, l, s)]
    return f"rgb({r},{g},{b})"

# Create a Streamlit web app
def main():
    st.title('Animal Health Prediction')

    # Input fields for user to enter data
    temperature = st.slider('Temperature', min_value=35.0, max_value=40.0, value=38.5, step=0.1)
    heart_rate = st.slider('Heart Rate', min_value=60, max_value=100, value=80, step=1)
    weight = st.slider('Weight', min_value=100, max_value=200, value=150, step=1)
    sensor1 = st.slider('Sensor 1', min_value=30.0, max_value=40.0, value=35.0, step=0.1)
    sensor2 = st.slider('Sensor 2', min_value=60.0, max_value=80.0, value=75.0, step=0.1)

    # Selection box for the type of animal
    animal_types = ['Cow', 'Sheep', 'Goat', 'Dog']
    animal_type = st.selectbox('Select the type of animal', animal_types)

    # Use the generate_pastel_color function to dynamically set a pastel color based on the animal type
    pastel_color = generate_pastel_color(animal_types.index(animal_type) / len(animal_types))

    # Set the dynamic pastel color for the submit button
    submit_button = st.button('Submit')

    # Make a prediction when the submit button is pressed
    if submit_button:
        # Make a prediction using the model
        prediction = model.predict([[temperature, heart_rate, weight, sensor1, sensor2]])
        
        # Display the prediction with the dynamic pastel color
        st.subheader('Prediction:')
        if prediction[0] == 1:
            st.success(f'The {animal_type.lower()} may have a health issue.')
        else:
            st.success(f'The {animal_type.lower()} is healthy.')

        # Display the dynamic pastel color
        st.markdown(
            f"""
            <style>
                .stButton {{
                    background-color: {pastel_color};
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

if __name__ == '__main__':
    main()
