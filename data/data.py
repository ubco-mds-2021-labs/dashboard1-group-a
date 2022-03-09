import pandas as pd

from data_functions import (
    drop_and_rename_columns,
    add_date_features,
    pivot_longer_by_humidity_and_temperature,
    add_location_features,
    add_features_for_energy_comparison,
)

DATA_PATH = "data/energydata_complete.csv"

# Temperature dataframe for Tab 1 Use
temperature_df_full = (
    pd.read_csv(DATA_PATH)
    .pipe(drop_and_rename_columns)
    .pipe(add_date_features)
    .pipe(pivot_longer_by_humidity_and_temperature)
    .pipe(add_location_features)
)

# Energy dataframe for Tab 2 Use
energy_df_full = (
    pd.read_csv(DATA_PATH)
    .pipe(drop_and_rename_columns)
    .pipe(add_date_features)
    .pipe(add_features_for_energy_comparison)
)

# THIS FILE IS NOT INTENDED TO BE EXECUTED DIRECTLY. THE RELATIVE
# IMPORT WILL BREAK.
# However, it will work as intended if you import the temperature_df_full
# and related objects from somewhere else.

# Write to .csv file to save space in memory on the heroku app.
if __name__ == "__main__":
    temperature_df_full.to_csv("data/temperature_df_full.csv")
    energy_df_full.to_csv("data/energy_df_full.csv")
