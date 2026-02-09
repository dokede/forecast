import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

csv_path = Path("data/raw/weather_history.csv")
df = pd.read_csv(csv_path)
df['date'] = pd.to_datetime(df['date'])


plt.figure(figsize=(12,5))
plt.plot(df['date'], df['temperature_max'], marker='.', linestyle='-')
plt.title("Maksymalna temperatura dzienna - Warszawa")
plt.xlabel("Data")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.show()

df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek

# Boxplot wg miesięcy
plt.figure(figsize=(10,5))
df.boxplot(column='temperature_max', by='month')
plt.title("Rozkład temperatur wg miesiąca")
plt.suptitle("")
plt.xlabel("Miesiąc")
plt.ylabel("Temperatura (°C)")
plt.show()