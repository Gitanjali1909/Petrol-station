import plotly.graph_objects as go
import numpy as np

def create_globe(df):
    lats = df['Latitude'].tolist()
    lons = df['Longitude'].tolist()
    lats = [lat + np.random.uniform(-0.05, 0.05) for lat in lats]
    lons = [lon + np.random.uniform(-0.05, 0.05) for lon in lons]

    texts = df.apply(
        lambda row: f"{row['Pump Name']} ({row['Brand']})<br>"
                    f"⭐ {row['Rating']} | {row['City']}, {row['State']}",
        axis=1
    )

    colors = df['Rating'].apply(
        lambda x: "green" if x >= 4 else ("orange" if x >= 2.5 else "red")
    ).tolist()

    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lon=lons,
        lat=lats,
        text=texts,
        hoverinfo="text",
        mode="markers",
        marker=dict(
            size=8,
            symbol="circle-cross",
            color=colors,
            line=dict(width=1, color="black")
        )
    ))

    fig.update_geos(
        scope="asia",
        showcountries=True,
        showland=True,
        showocean=True,
        landcolor="rgb(240, 240, 200)",
        oceancolor="rgb(170, 210, 255)",
        countrycolor="black",
        lakecolor="rgb(150, 200, 255)",
        subunitcolor="purple",
        showlakes=True,
        showrivers=True,
        rivercolor="blue",
        projection_type="mercator",
        lataxis_range=[6, 38],
        lonaxis_range=[68, 98]
    )

    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        height=700,
        geo_bgcolor="rgb(245, 230, 255)"
    )

    return fig
