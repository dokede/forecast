import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro

# wczytanie danych
df = pd.read_csv("data/raw/weather_history.csv")

df['date'] = pd.to_datetime(df['date'])

# tworzymy kolumnę z miesiącem
df['month'] = df['date'].dt.month

# grupowanie po miesiącu i średnia temperatura
monthly_avg = df.groupby('month')['temperature_max'].mean()

print(df.head())
print(df.describe())

# wykres słupkowy
monthly_avg.plot(kind='bar', title="Średnia temperatura wg miesiąca", figsize=(10,6))
plt.xlabel("Miesiąc")
plt.ylabel("Średnia maksymalna temperatura (°C)")
plt.show()

# wykres temperatury w czasie
plt.figure(figsize=(12,6))
plt.plot(df['date'], df['temperature_max'], color='orange', label='Maksymalna temperatura')
plt.title("Maksymalna temperatura w czasie")
plt.xlabel("Data")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
plt.hist(df['temperature_max'], bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram maksymalnej temperatury")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Liczba dni")
plt.show()