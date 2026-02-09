# Forecasting Weather

Projekt pokazuje, jak prognozować maksymalne temperatury dla danej lokalizacji w Polsce przy użyciu prostego modelu regresji liniowej.



## 📂 Struktura projektu

forecasting/
├─ pipeline/
│ ├─ 01_fetch.py # Pobranie danych historycznych z API
│ ├─ 02_data_prep.py # Przetwarzanie i czyszczenie danych
│ └─ 03_train_model.py # Trenowanie baseline Linear Regression
├─ data/
│ ├─ raw/ # Surowe dane pobrane z API
│ └─ processed/ # Dane gotowe do modelowania
├─ analytics/ # Eksploracja danych i wykresy
├─ models/ # Zapisany model regresji
├─ app/ # (Opcjonalnie) dashboard w Streamlit
└─ README.md

1. **Kolejność**

   python pipeline/fetch_weather.py            - pobranie danych pogodowych
   python pipeline/data_prep.py                - przygotowanie danych
   python analytics/explore_weatherdata_prep.py - analiza danych
   python pipeline/train_model.py              - budowa modelu
