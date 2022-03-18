import pandas as pd

TEMP_DATA_PATH = "data/temperature_df_full.csv"
ENERGY_DATA_PATH = "data/energy_df_full.csv"

# Temperature dataframe for Tab 1 Use
temperature_df_full = pd.read_csv("data/temperature_df_full.csv").astype(
    {"Date": "datetime64"}
)

# Energy dataframe for Tab 2 Use
energy_df_full = pd.read_csv("data/energy_df_full.csv").astype({"date": "datetime64"})
