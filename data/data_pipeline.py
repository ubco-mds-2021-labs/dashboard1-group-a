# THIS FILE IS INTENDED TO PERFORM THE DATA PIPELINE ON OUR
# RAW DATA AND SAVE IT TO .CSV FILES

import pandas as pd

from data_functions import (
    resample_df,
    drop_and_rename_columns,
    add_date_features,
    pivot_longer_by_humidity_and_temperature,
    add_location_features,
    add_features_for_energy_comparison,
    get_temperature_df_features,
    get_energy_df_features,
)

DATA_PATH = "data/energydata_complete.csv"

# Temperature dataframe for Tab 1 Use
temperature_df_full = (
    pd.read_csv(DATA_PATH)
    .pipe(resample_df)
    .pipe(drop_and_rename_columns)
    .pipe(add_date_features)
    .pipe(pivot_longer_by_humidity_and_temperature)
    .pipe(add_location_features)
    .pipe(get_temperature_df_features)
)

# Energy dataframe for Tab 2 Use
energy_df_full = (
    pd.read_csv(DATA_PATH)
    .pipe(resample_df)
    .pipe(drop_and_rename_columns)
    .pipe(add_date_features)
    .pipe(add_features_for_energy_comparison)
    .pipe(get_energy_df_features)
)

# Write to .csv file to save space in memory on the heroku app.
if __name__ == "__main__":
    temperature_df_full.to_csv("data/temperature_df_full.csv")
    energy_df_full.to_csv("data/energy_df_full.csv")
