import streamlit as st
import pandas as pd
from data_processing import load_data, get_top_rated_pumps, rating_distribution
from globe_plot import create_globe

st.set_page_config(layout="wide", page_title="Petrol Pump Ratings Dashboard")

df = load_data("data/data-petrol.csv")
cities = df['City'].dropna().sort_values().unique().tolist()
states = df['State'].dropna().sort_values().unique().tolist()

st.title("Petrol Pump Ratings & Reviews")

col1, col2 = st.columns(2)
with col1:
    search_state = st.selectbox("Select State", ["All"] + states)
with col2:
    if search_state != "All":
        cities_in_state = df[df['State'] == search_state]['City'].dropna().sort_values().unique().tolist()
    else:
        cities_in_state = cities
    search_city = st.selectbox("Select City", ["All"] + cities_in_state)

filtered_df = df.copy()
if search_state != "All":
    filtered_df = filtered_df[filtered_df['State'] == search_state]
if search_city != "All":
    filtered_df = filtered_df[filtered_df['City'] == search_city]

st.subheader(f"Showing {len(filtered_df)} Petrol Pumps")
st.plotly_chart(create_globe(filtered_df), use_container_width=True)

st.subheader("Top Rated Petrol Pumps")
top_pumps = get_top_rated_pumps(filtered_df, top_n=10)
st.table(top_pumps[['Pump Name','Brand','City','State','Rating']])

st.subheader("Rating Distribution")
rating_counts = rating_distribution(filtered_df)
st.bar_chart(rating_counts)

st.subheader("Add Your Review")

col1, col2 = st.columns(2)
with col1:
    state_input = st.selectbox("State", ["Select"] + states, key="form_state")
with col2:
    if state_input != "Select":
        cities_in_state = df[df['State'] == state_input]['City'].dropna().sort_values().unique().tolist()
    else:
        cities_in_state = []
    city_input = st.selectbox("City", ["Select"] + cities_in_state, key="form_city")

col3, col4 = st.columns(2)
with col3:
    pump_name_input = st.text_input("Pump Name")
with col4:
    brand_input = st.text_input("Brand")

rating_input = st.slider("Rating", 1.0, 5.0, 3.0, 0.1)
review_input = st.text_area("Your Comment", placeholder="Share your experience here...")

rating_color = "green" if rating_input >= 4 else ("orange" if rating_input >= 2.5 else "red")
st.markdown(f"<p style='color:{rating_color}; font-size:18px;'>Selected Rating: {rating_input} {'⭐'*int(round(rating_input))}</p>", unsafe_allow_html=True)

with st.form("review_form"):
    submit_button = st.form_submit_button("Submit Review 🚀")
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
            st.success("🎉 Review submitted successfully! (Note: Not saved permanently in this version)")
