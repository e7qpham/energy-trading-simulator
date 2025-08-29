import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="darkgrid")

# Load data
weather = pd.read_csv(r"C:\Users\Quynh Pham\energy-trading-simulator\data\raw\weather_berlin.csv", parse_dates=["time"])
prices = pd.read_csv(r"C:\Users\Quynh Pham\energy-trading-simulator\data\raw\prices.csv", parse_dates=["utc_timestamp"])

# Rename columns for easier merging
weather = weather.rename(columns={"time": "timestamp"})
prices = prices.rename(columns={"utc_timestamp": "timestamp"})

# Remove timezone from prices timestamp
prices["timestamp"] = prices["timestamp"].dt.tz_convert(None)

# Merge datasets on timestamp
df = pd.merge(prices, weather, on="timestamp", how="inner")

# Save merged data
df.to_csv(r"C:\Users\Quynh Pham\energy-trading-simulator\data\processed\merged_data.csv", index=False)


