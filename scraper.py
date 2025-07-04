import requests
import pandas as pd

def fetch_opensky_data(airport="YSSY", max_flights=50):
    """
    Pull live departures from OpenSky API (Sydney Airport as default).
    """
    url = f"https://opensky-network.org/api/flights/departure?airport={airport}&begin=1672531200&end=1672617600"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            flights = response.json()
            df = pd.DataFrame(flights[:max_flights])
            return df
        else:
            return pd.DataFrame()
    except Exception as e:
        print("Error fetching data:", e)
        return pd.DataFrame()
