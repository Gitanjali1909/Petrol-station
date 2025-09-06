import streamlit as st
import pandas as pd
from data_processing import load_data, get_top_rated_pumps, rating_distribution
from globe_plot import create_globe

st.set_page_config(layout="wide", page_title="Petrol Pump Ratings Dashboard")

df = load_data("data/data-petrol.csv")
cities = df['City'].sort_values().unique().tolist()
states = df['State'].sort_values().unique().tolist()

st.title("Interactive Petrol Pump Ratings & Reviews Dashboard")

with st.sidebar:
    st.header("Filter Pumps")
    selected_state = st.selectbox("Select State", ["All"] + states)

    if selected_state != "All":
        cities_in_state = df[df['State'] == selected_state]['City'].sort_values().unique().tolist()
    else:
        cities_in_state = cities

    selected_city = st.selectbox("Select City", ["All"] + cities_in_state)

filtered_df = df.copy()
if selected_state != "All":
    filtered_df = filtered_df[filtered_df['State'] == selected_state]
if selected_city != "All":
    filtered_df = filtered_df[filtered_df['City'] == selected_city]

st.subheader(f"Showing {len(filtered_df)} Petrol Pumps")
st.plotly_chart(create_globe(filtered_df), use_container_width=True)

st.subheader("Top Rated Petrol Pumps")
top_pumps = get_top_rated_pumps(filtered_df, top_n=10)
st.table(top_pumps[['Pump Name','Brand','City','State','Rating']])

st.subheader("Rating Distribution")
rating_counts = rating_distribution(filtered_df)
st.bar_chart(rating_counts)

st.subheader("Add Your Review")
with st.form("review_form"):
    state_input = st.selectbox("State", ["Select"] + states)
    if state_input != "Select":
        cities_in_state = df[df['State'] == state_input]['City'].sort_values().unique().tolist()
    else:
        cities_in_state = []
    city_input = st.selectbox("City", ["Select"] + cities_in_state)

    pump_name_input = st.text_input("Pump Name")
    brand_input = st.text_input("Brand")
    rating_input = st.slider("Rating", 1.0, 5.0, 3.0, 0.1)
    review_input = st.text_area("Your Comment")
    submit_button = st.form_submit_button("Submit Review")

    if submit_button:
        if state_input == "Select" or city_input == "Select" or not pump_name_input or not brand_input or not review_input:
            st.warning("Please fill all fields before submitting.")
        else:
            new_review = {
                "PumpID": len(df)+1,
                "Pump Name": pump_name_input,
                "Brand": brand_input,
                "City": city_input,
                "State": state_input,
                "Latitude": 0,
                "Longitude": 0,
                "Rating": rating_input,
                "Review": review_input
            }
            st.success("Review submitted! (Note: Not saved permanently in CSV in this version)")
