import pandas as pd
import numpy as np

TEMP_DATA_PATH = "data/temperature_df_full.csv"
ENERGY_DATA_PATH = "data/energy_df_full.csv"

# Temperature dataframe for Tab 1 Use
temperature_df_full = pd.read_csv("data/temperature_df_full.csv").astype({"date": "datetime64"})
temperature_df_full = temperature_df_full.iloc[:, np.r_[1,8:19]] #reduce number of columns being imported into tab1

# Energy dataframe for Tab 2 Use
energy_df_full = pd.read_csv("data/energy_df_full.csv").astype({"date": "datetime64"})
energy_df_full = energy_df_full.iloc[:, np.r_[1,2,3, 22:36]] #reduce number of columns being imported into tab2