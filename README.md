#Petrol Pump Ratings & Reviews 

Explore petrol pumps across India — view ratings, user comments, and pump locations on an interactive map. Submit your own reviews and see live visualizations of top-rated pumps and rating distributions.

## About the Project
This project allows users to explore petrol pumps across India interactively. Users can select a state and city, view pumps on an interactive map with color-coded ratings, and submit reviews that feed into live visualizations.  

**Dataset:** A synthetic dataset was generated, including 550+ petrol pumps across 28 Indian states, with realistic pump names, brands, ratings, reviews, and latitude/longitude for mapping. This demonstrates skills in **data generation, cleaning, and preparation**.

## How It Works
- **Data & Cleaning:** `data/data-petrol.csv` contains Pump_ID, Pump Name, Brand, City, State, Latitude, Longitude, Rating, Review, and Num_Reviews. Cleaned and standardized for visualization.
- **Interactive Map Visualization:** Uses Plotly to display pumps on a map with color-coded markers based on ratings (green = high, red = low). Hovering over a pump shows its details.
- **Filters:** Users can select State and City dynamically to filter pumps.
- **EDA & Stats:** Top-rated pumps table, rating distribution charts, and other summary stats.
- **Interactive Reviews:** Users can submit reviews with Pump Name, Brand, Rating, and Comments. Live preview and rating stars update dynamically.

## Demo
- Streamlit app: Run `main.py` locally with `streamlit run main.py`  
- Kaggle Notebook: [https://www.kaggle.com/code/gitanjalisoni/petrol-pump-ratings](https://www.kaggle.com/code/gitanjalisoni/petrol-pump-ratings)

## Tech Stack
Python (pandas, numpy), Plotly, Streamlit, Matplotlib, Seaborn

## Features
- Interactive map of petrol pumps across India  
- Color-coded markers based on ratings  
- Dynamic filters: State → City cascading dropdowns  
- View top-rated pumps and rating distributions  
- Add new reviews with live preview  
- Synthetic dataset designed with realistic data  
- Clean, interactive, and user-friendly dashboard

## Future Enhancements
- Save reviews permanently to CSV or database  
- Add clustering for nearby pumps on the map  
- Include additional pump attributes like fuel types and amenities  
- Add search functionality and map zoom for better exploration
