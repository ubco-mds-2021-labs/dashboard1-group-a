import pandas as pd

from .data_functions import (
    drop_and_rename_columns,
    add_date_features,
    pivot_longer_by_humidity_and_temperature,
    add_location_features,
    add_features_for_energy_comparison,
)

# Temperature dataframe for Tab 1 Use
temperature_df_full = (
    pd.read_csv("energydata_complete.csv")
    .pipe(drop_and_rename_columns)
    .pipe(add_date_features)
    .pipe(pivot_longer_by_humidity_and_temperature)
    .pipe(add_location_features)
)
# TODO: Apply group_by() aggregation to create
# day-of-week dataframe (temperature_df_daily) and a
# hour-of-the-day dataframe (temperature_df_hourly) for
# the timescale adjustment.

# temperature_df_hourly =
# temperature_df_daily =

# Energy dataframe for Tab 2 Use
energy_df_full = (
    pd.read_csv("energydata_complete.csv")
    .pipe(drop_and_rename_columns)
    .pipe(add_date_features)
    .pipe(add_features_for_energy_comparison)
)
# TODO: Apply group_by() aggregation to create
# day-of-week dataframe (energy_df_daily) and a
# hour-of-the-day dataframe (energy_df_hourly) for
# the timescale adjustment.

# energy_df_hourly =
# energy_df_daily =


# THIS FILE IS NOT INTENDED TO BE EXECUTED DIRECTLY. THE RELATIVE
# IMPORT WILL BREAK.
# However, it will work as intended if you import the temperature_df_full
# and related objects from somewhere else.
