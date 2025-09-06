import plotly.graph_objects as go

def create_globe(df):
    lats = df['Latitude'].tolist()
    lons = df['Longitude'].tolist()
    texts = df.apply(lambda row: f"Name: {row['Pump Name']}<br>Brand: {row['Brand']}<br>Rating: {row['Rating']}<br>Comment: {row['Review']}", axis=1)

    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lon=lons,
        lat=lats,
        text=texts,
        mode='markers',
        marker=dict(
            size=5,
            color='red',
            symbol='circle'
        )
    ))

    fig.update_geos(
        showcountries=True,
        showland=True,
        showocean=True,
        landcolor="lightgreen",
        oceancolor="lightblue",
        projection_type="orthographic"
    )

    fig.update_layout(
        geo=dict(
            projection_scale=1,
            center=dict(lat=20, lon=78),
            lataxis_showgrid=True,
            lonaxis_showgrid=True
        ),
        margin={"r":0,"t":0,"l":0,"b":0}
    )

    return fig
