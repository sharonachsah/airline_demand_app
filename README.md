# Airline Booking Market Demand Web App

This Streamlit web app scrapes flight data, processes it, and displays market demand trends and insights using OpenAI or local analysis.

---

## Features

- Scrape airline demand data (from OpenSky)
- Analyze trends: Popular routes, peak days, price patterns
- Generate insights using AI
- Visualize results with tables and charts
- Built with Python, Streamlit, Pandas, OpenAI

---

## Setup Instructions

### 1. Clone the Repo
git clone https://github.com/sharonachsah/airline_demand_app.git
cd airline_demand_app


### 2. Create & Activate Virtual Environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Set OpenAI API Key
cp .env.template .env
OPENAI_API_KEY=your_openai_api_key_here

### Run the App
streamlit run app.py

