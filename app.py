import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from scraper import fetch_opensky_data
from insights import generate_insights

st.set_page_config(page_title="Airline Market Demand App", layout="wide")

st.title("✈️ Airline Booking Market Demand Trends (Australia)")

# Sidebar filters
st.sidebar.header("Filter Options")
airport = st.sidebar.selectbox("Choose Airport", ["YSSY", "YMML", "YBBN"])
max_records = st.sidebar.slider("Max Flights to Analyze", 10, 100, 30)

# Data Fetch
st.subheader(f"Live Flight Data for: {airport}")
data = fetch_opensky_data(airport, max_records)
if data.empty:
    st.warning("No data found or API failed.")
else:
    st.dataframe(data.head())

    st.markdown("### ✨ Market Demand Insights")
    input_prompt = f"""Give a brief analysis based on the following raw airline booking data (routes, time, trend, demand):
{data.head(10).to_csv(index=False)}"""
    if st.button("Generate Insights"):
        with st.spinner("Analyzing with AI..."):
            insights = generate_insights(input_prompt)
        st.success("Insights generated!")
        st.markdown(insights)

    # Route Visualization
    if "estDepartureAirport" in data.columns:
        route_counts = data["estDepartureAirport"].value_counts().reset_index()
        route_counts.columns = ["Airport", "Flights"]
        fig = px.bar(route_counts, x="Airport", y="Flights", title="Top Departure Airports")
        st.plotly_chart(fig)

    if "firstSeen" in data.columns:
        data["Date"] = pd.to_datetime(data["firstSeen"], unit="s")
        data["Day"] = data["Date"].dt.date
        trend_data = data.groupby("Day").size().reset_index(name="Flights")
        fig2 = px.line(trend_data, x="Day", y="Flights", title="Flight Demand Over Days")
        st.plotly_chart(fig2)
