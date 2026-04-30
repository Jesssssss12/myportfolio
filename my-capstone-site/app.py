import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

st.title("Met Chinese Art Dashboard")

csv_path = Path(__file__).resolve().parent / "static" / "data" / "Met-database-csv.csv"

if not csv_path.exists():
    st.error(f"Data file not found: {csv_path}")
    st.stop()

df = pd.read_csv(csv_path)

# Basic cleaning
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["Classification"] = df["Classification"].fillna("Unknown")
df["Object Name"] = df["Object Name"].fillna("Unknown Object")
df["Artist Display Name"] = df["Artist Display Name"].fillna("Unidentified artist")
df["Dynasty"] = df["Dynasty"].fillna("Unknown")

# Keep valid years only
df = df.dropna(subset=["year"])
df = df[(df["year"] >= 0) & (df["year"] <= 2025)]

show_all = st.checkbox("Show all data", value=False)

st.subheader("Distribution of Chinese Artworks by Year and Classification")

fig = px.scatter(
    df,
    x="year",
    y="Classification",
    color="Classification",
    custom_data=["Object Name", "Artist Display Name", "Dynasty"],
    title="Distribution of Chinese Artworks by Year and Classification",
    opacity=0.7
)

fig.update_traces(
    marker=dict(size=8),
    hovertemplate=
    "<b>%{customdata[0]}</b><br>" +
    "Classification: %{y}<br>" +
    "Year: %{x}<br>" +
    "Artist: %{customdata[1]}<br>" +
    "Dynasty: %{customdata[2]}<extra></extra>"
)

# Default: hide all data. Check "Show all data" to display everything.
if not show_all:
    for trace in fig.data:
        trace.visible = "legendonly"

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Object Classification",
    height=800,
    legend_title="Click to Show Classification",
    xaxis=dict(
        range=[0, 2025],
        tickformat="d",
        exponentformat="none",
        rangeslider=dict(visible=True),
        rangeselector=dict(
            buttons=[
                dict(count=200, label="200y", step="year", stepmode="backward"),
                dict(count=500, label="500y", step="year", stepmode="backward"),
                dict(count=1000, label="1000y", step="year", stepmode="backward"),
                dict(step="all", label="All")
            ]
        )
    )
)

st.plotly_chart(fig, use_container_width=True)