import pandas as pd
from pathlib import Path

# Ścieżki
RAW_PATH = Path("data/raw/weather_history.csv")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True) 
PROCESSED_PATH = PROCESSED_DIR / "weather_clean.csv"

# 1️⃣ Wczytanie danych
df = pd.read_csv(RAW_PATH)

# 2️⃣ Czyszczenie danych
# usuwamy brakujące wartości
df = df.dropna()

df['date'] = pd.to_datetime(df['date'])

# 3️⃣ Dodanie dodatkowych cech
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['dayofweek'] = df['date'].dt.dayofweek

# 4️⃣ Zapisanie przetworzonych danych
df.to_csv(PROCESSED_PATH, index=False)

print(f"Dane przygotowane i zapisane w: {PROCESSED_PATH}")
