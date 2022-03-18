import pandas as pd

##### GENERAL WRANGLING #####


def resample_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Downsamples the dataframe to one-row-per-hour by averaging
    all numerical columns.

    Parameters
    ----------
    df : pd.DataFrame
        Our raw energydata_complete data BEFORE
        other transformations are applied.

    Returns
    -------
    pd.DataFrame
        The downsampled dataframe.
    """
    df["date"] = pd.to_datetime(df["date"])
    df = df.resample("H", on="date").mean().reset_index()
    return df


def trim_df_dates_to_full_days(df: pd.DataFrame) -> pd.DataFrame:
    """
    Trims down our time series dates to our first and last full
    days (from 00h00 to 23h00)

    Parameters
    ----------
    df : pd.DataFrame
        Our dataframe after resampling with a date column to filter on.

    Returns
    -------
    pd.DataFrame
        Our passed in df, with rows removed from the
        begining and end of the time series.
    """
    # Programatically get Date Boundaries to trim to full days.
    start_date_boundary = df.loc[df["date"].dt.hour == 0].head(1)["date"].item()

    end_date_boundary = df.loc[df["date"].dt.hour == 23].tail(1)["date"].item()

    # Trim df to only dates between our boundaries.
    trimmed_df = df[
        (df["date"] >= start_date_boundary) & (df["date"] <= end_date_boundary)
    ]

    return trimmed_df


def drop_and_rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drops irrelevent random columns and renames remaining columns
    to descriptive, readable names.

    Parameters
    ----------
    df : pd.DataFrame
        Our raw dataframe read in from the energydata_complete dataset.

    Returns
    -------
    pd.DataFrame
        The dataframe with tidied column names.
    """
    df = df.drop(columns=["rv1", "rv2"])
    df = df.rename(
        columns={
            "Appliances": "energy_appliances",
            "lights": "energy_lights",
            "Press_mm_hg": "pressure",
            "Tdewpoint": "dewpoint",
        }
    ).rename(
        columns={
            column: (
                column.replace("T", "temperature_")
                .replace("RH", "humidity")
                .replace("out", "outside")
                .replace("1", "kitchen")
                .replace("2", "living_room")
                .replace("3", "laundry_room")
                .replace("4", "office")
                .replace("5", "bathroom")
                .replace("6", "northside")
                .replace("7", "ironing_room")
                .replace("8", "teen_bedroom")
                .replace("9", "parent_bedroom")
                .replace("__", "_")
                .lower()
            )
            for column in df.columns
        }
    )
    return df


def add_date_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fixes the date column to our dataframe, then generates
    a handful of new feature columns based on those values.

    Parameters
    ----------
    df : pd.DataFrame
        The renamed dataframe from drop_and_rename_columns()

    Returns
    -------
    pd.DataFrame
        The dataframe with a datetime index and several new columns
    """
    df["day_of_week"] = df["date"].dt.day_name()
    df["hour_of_day"] = df["date"].dt.hour
    df["month"] = df["date"].dt.month_name()
    df["workday"] = df["day_of_week"].apply(
        lambda day: "Weekend" if day in ["Saturday", "Sunday"] else "Weekday"
    )

    def get_time_of_day_from_hour(hour):
        """
        Helper function to the time of day based on a passed in hour.
        """
        # Subjectively decided hour-of-the-day thresholds to determine time of day.
        night_morning_threshold = 6
        morning_afternoon_threshold = 12
        afternoon_night_threshold = 18
        evening_night_threshold = 24
        if (hour < night_morning_threshold) or (evening_night_threshold <= hour):
            time_of_day = "Night"
        elif (night_morning_threshold <= hour) and (hour < morning_afternoon_threshold):
            time_of_day = "Morning"
        elif (morning_afternoon_threshold <= hour) and (
            hour < afternoon_night_threshold
        ):
            time_of_day = "Afternoon"
        elif (afternoon_night_threshold <= hour) and (hour < evening_night_threshold):
            time_of_day = "Evening"
        return time_of_day

    df["time_of_day"] = df["date"].dt.hour.apply(get_time_of_day_from_hour)

    return df


##### WRANGLING FOR TEMPERATURE DF #####


def pivot_longer_by_humidity_and_temperature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reshapes the dataframe by collapsing all of the temperature and humidity
    columns into an temperature, humidity, and location column

    Parameters
    ----------
    df : pd.DataFrame
        The cleaned and renamed dataframe from add_date_features().

    Returns
    -------
    pd.DataFrame
        A much longer dataframe with an exposed location column
        to perform operations on.
    """
    # Need to melt both variables individually, which creates
    # a ton of meaningless rows in the second melt.
    temporary_df = df.melt(
        id_vars=[colname for colname in df.columns if "temp" not in colname],
        var_name="temperature_location",
        value_name="temperature",
        ignore_index=False,
    )
    temporary_df = temporary_df.melt(
        id_vars=[
            colname for colname in temporary_df.columns if "humidity" not in colname
        ],
        var_name="humidity_location",
        value_name="humidity",
        ignore_index=False,
    )
    temporary_df["temperature_location"] = temporary_df[
        "temperature_location"
    ].str.replace("temperature_", "")
    temporary_df["humidity_location"] = temporary_df["humidity_location"].str.replace(
        "humidity_", ""
    )

    # We know all measurements come from slices of time that contain a measurement of both humidity
    # and temperature from one location, so if we combine the location columns we can drop
    # the extra rows created during the second melt.
    df = temporary_df[
        temporary_df["temperature_location"] == temporary_df["humidity_location"]
    ]
    df = df.drop(columns=["humidity_location"]).rename(
        columns={"temperature_location": "measurement_location"}
    )
    return df


def add_location_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds extra features generated from the location column,
    returning the updated dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        The long-form dataframe with a location column
        resulting from pivot_longer_by_humidity_and_temperature()

    Returns
    -------
    pd.DataFrame
        The same dataframe with extra floor and
        room_type features added on.
    """
    # Define Helper Functions to get Floor, Room Type, and Direction Facing
    def get_floor_from_location(location):
        """
        Helper function to the floor of the house based on a
        passed in measurement location.
        """
        floor = None
        # from data source https://github.com/LuisM78/Appliances-energy-prediction-data
        lower_floor_locations = ["kitchen", "living_room", "laundry_room", "office"]
        upper_floor_locations = [
            "bathroom",
            "ironing_room",
            "teen_bedroom",
            "parent_bedroom",
        ]
        outside_locations = ["northside", "outside"]
        if location in lower_floor_locations:
            floor = "Ground Floor"
        elif location in upper_floor_locations:
            floor = "Second Floor"
        elif location in outside_locations:
            floor = "Outside"
        return floor

    def get_room_type_from_location(location):
        """
        Returns the type of the room based on a passed-in measurement location.
        """
        room_type = None
        # Subjectively created through room function.
        # Currently not too happy with group splits here,
        # but we constrained ourselves to max 4 "types" of locations.
        outside_locations = ["northside", "outside"]
        bedroom_locations = ["teen_bedroom", "parent_bedroom"]
        living_locations = ["living_room", "office"]
        functional_locations = ["kitchen", "laundry_room", "ironing_room", "bathroom"]
        if location in outside_locations:
            room_type = "Outside"
        elif location in bedroom_locations:
            room_type = "Bedroom"
        elif location in living_locations:
            room_type = "Living Area"
        elif location in functional_locations:
            room_type = "Functional Space"
        return room_type

    def get_direction_from_location(location):
        """
        Helper function to turn a passed in room location into which
        sun direction it faces in the house (east or west).
        """
        # as gleaned from https://github.com/LuisM78/Appliances-energy-prediction-data/blob/master/Second%20Floor_lines%20removed.png
        east_locations = ["living_room", "laundry_room", "northside", "parent_bedroom"]
        west_locations = [
            "kitchen",
            "office",
            "bathroom",
            "ironing_room",
            "teen_bedroom",
        ]
        outside_locations = ["outside"]

        if location in west_locations:
            direction = "West Facing"
        elif location in east_locations:
            direction = "East Facing"
        elif location in outside_locations:
            direction = "Outside"
        return direction

    # Apply the helper functions to create new columns
    df["floor"] = df["measurement_location"].apply(get_floor_from_location)
    df["room_type"] = df["measurement_location"].apply(get_room_type_from_location)
    df["direction"] = df["measurement_location"].apply(get_direction_from_location)

    return df


def get_temperature_df_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns only those features we use in our tab 1 temperature tab
    from the passed in data frame, and tidies up their column names.

    Parameters
    ----------
    df : pd.DataFrame
        Our cleaned and wrangled df.

    Returns
    -------
    pd.DataFrame
        The subset of specific columns from our
        passed in df, with Capital and Space column
        names.
    """
    df_selection = df[
        [
            "date",
            "day_of_week",
            "hour_of_day",
            "month",
            "measurement_location",
            "temperature",
            "humidity",
            "workday",
            "time_of_day",
            "floor",
            "room_type",
            "direction",
        ]
    ]
    df_selection_renamed = df_selection.rename(
        columns={
            column: column.replace("_", " ").title().replace(" Of ", " of ")
            for column in df_selection.columns
        }
    ).rename(
        columns={
            "Temperature": "Temperature (C)",
            "Humidity": "Relative Humidity (%)",
        }
    )
    return df_selection_renamed


##### WRANGLING FOR ENERGY DF #####


def add_features_for_energy_comparison(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds in several features based on the quantiles
    of numerical environmental columns for comparison
    of energy use.

    Parameters
    ----------
    df : pd.DataFrame
        Our cleaned and renamed dataframe from
        drop_and_rename_columns()

    Returns
    -------
    pd.DataFrame
        The same dataframe with extra total_energy,
        outside_temperature_status, windspeed_status,
        and outside_humidity_status added on.
    """
    df["total_energy"] = df["energy_appliances"] + df["energy_lights"]

    # Bins various numerical columns into their quantiles.
    df["windspeed_status"] = pd.cut(
        df["windspeed"],
        bins=4,
        labels=[
            "Low Windspeed",
            "Mid-Low Windspeed",
            "Mid-High Windspeed",
            "High Windspeed",
        ],
    )

    df["visibility_status"] = pd.cut(
        df["visibility"],
        bins=4,
        labels=[
            "Low Visibility",
            "Mid-Low Visibility",
            "Mid-High Visibility",
            "High Visibility",
        ],
    )

    df["dewpoint_status"] = pd.cut(
        df["dewpoint"],
        bins=4,
        labels=[
            "Low Dewpoint",
            "Mid-Low Dewpoint",
            "Mid-High Dewpoint",
            "High Dewpoint",
        ],
    )

    df["outside_temperature_status"] = pd.cut(
        df["temperature_outside"],
        bins=4,
        labels=[
            "Low Outside Temperature",
            "Mid-Low Outside Temperature",
            "Mid-High Outside Temperature",
            "High Outside Temperature",
        ],
    )

    df["outside_humidity_status"] = pd.cut(
        df["humidity_outside"],
        bins=4,
        labels=[
            "Low Outside Humidity",
            "Mid-Low Outside Humidity",
            "Mid-High Outside Humidity",
            "High Outside Humidity",
        ],
    )
    return df


def get_energy_df_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns only those features we use in our tab 2 energy tab
    from the passed in data frame, and tidies up their column names.

    Parameters
    ----------
    df : pd.DataFrame
        Our cleaned and wrangled df.

    Returns
    -------
    pd.DataFrame
        The subset of specific columns from our
        passed in df with presentable variable names.
    """
    df_selection = df[
        [
            "date",
            "day_of_week",
            "hour_of_day",
            "month",
            "energy_appliances",
            "energy_lights",
            "temperature_outside",
            "humidity_outside",
            "dewpoint",
            "pressure",
            "windspeed",
            "visibility",
        ]
    ]
    df_selection_renamed = df_selection.rename(
        columns={
            column: column.replace("_", " ").title().replace(" Of ", " of ")
            for column in df_selection.columns
        }
    ).rename(
        columns={
            "Energy Appliances": "Energy Use - Appliances (Wh)",
            "Energy Lights": "Energy Use - Lights (Wh)",
            "Temperature Outside": "Temperature Outside (C)",
            "Humididty Outside": "Humididty Outside (%)",
            "Dewpoint": "Dewpoint (C)",
            "Pressure": "Air Pressure (mm Hg)",
            "Windspeed": "Windspeed (m / s)",
            "Visibility": "Visibility (km)",
        }
    )
    return df_selection_renamed
