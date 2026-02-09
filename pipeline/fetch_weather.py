import requests
import pandas as pd
from pathlib import Path

# parametry lokalizacji
lat = 52.23
lon = 21.01
start = "2018-01-01"
end = "2025-12-31"

# przygotowanie URL
url = (
    "https://archive-api.open-meteo.com/v1/archive"
    f"?latitude={lat}&longitude={lon}"
    f"&start_date={start}&end_date={end}"
    "&daily=temperature_2m_max"
)

# pobranie danych
resp = requests.get(url)
data = resp.json()

# wyciągnięcie do DataFrame
df = pd.DataFrame({
    "date": data["daily"]["time"],
    "temperature_max": data["daily"]["temperature_2m_max"]
})

# zapis CSV
raw_dir = Path("data/raw")
raw_dir.mkdir(parents=True, exist_ok=True)
csv_path = raw_dir / "weather_history.csv"
df.to_csv(csv_path, index=False)

print(f"Saved historical weather data to {csv_path}")
