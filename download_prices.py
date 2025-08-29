import pandas as pd
import os

# download historical German electricity prices
def download_german_prices(save_path):
    url = 'https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv'
    df = pd.read_csv(url, parse_dates=['utc_timestamp'], index_col='utc_timestamp')

    # filter German price (DE_LU) - day-ahead prices
    price_column = 'DE_LU_price_day_ahead'
    if price_column not in df.columns:
        raise ValueError(f"Price column {price_column} not found in dataset.")
    
    prices = df[[price_column]].dropna()
    prices = prices.rename(columns={price_column: 'price_EUR_per_MWh'})

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    prices.to_csv(save_path)
    print(f"Saved German day-ahead prices to {save_path}")

if __name__ == "__main__":
    download_german_prices('../data/raw/prices.csv')    