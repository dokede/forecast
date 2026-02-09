import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import pickle

csv_path = Path("data/raw/weather_history.csv")
df = pd.read_csv(csv_path)
df['date'] = pd.to_datetime(df['date'])

df['day_of_week'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
df['temp_lag_1'] = df['temperature_max'].shift(1)
df = df.dropna()


X = df[['day_of_week', 'month', 'temp_lag_1']]
y = df['temperature_max']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.2f} °C")

plt.figure(figsize=(12,5))
plt.plot(df['date'].iloc[-len(y_test):], y_test, label='Rzeczywista')
plt.plot(df['date'].iloc[-len(y_test):], y_pred, label='Predykcja', alpha=0.7)
plt.xlabel("Data")
plt.ylabel("Temperatura (°C)")
plt.title("Predykcja vs rzeczywista temperatura")
plt.legend()
plt.grid(True)
plt.show()

model_path = Path("models/baseline_model.pkl")
model_path.parent.mkdir(exist_ok=True)

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"Model zapisany do {model_path}")