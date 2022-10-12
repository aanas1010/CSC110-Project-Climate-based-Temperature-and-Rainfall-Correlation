"""CSC110 Fall 2020: Project Phase 2

Module Description
==================
This module contains functions for converting cvs files of rainfall and temperature data
into Pandas DataFrame objects satisfying a specified format. The cvs files are for 5 specified
countries as outlined in the project's written submission.

- Data taken from: https://climateknowledgeportal.worldbank.org/download-data

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students and Faculty
involved in CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2020 Shayaan Khan, Markus Nimi, Matthew Chan and Aabid Anas.
"""

import datetime as dt
from typing import Dict
import pandas as pd


def get_path(country: str, data_type: str) -> str:
    """
    Return the path of the csv file corresponding to the given
    country and data type (either rain or temp)

    Preconditions:
        - country in {'Belarus', 'Great Britain', 'Greenland', 'Malaysia', 'Saudi Arabia'}
        - data_type == 'rain' or data_type == 'temp'

    >>> get_path('Belarus', 'rain')
    'datasets/pr_1901_2016_BLR.csv'
    """
    types = {"rain": "pr", "temp": "tas"}
    paths = {
        "Belarus": "BLR",
        "Great Britain": "GBR",
        "Greenland": "GRL",
        "Malaysia": "MYS",
        "Saudi Arabia": "SAU"
    }

    pathname = "datasets/" + types[data_type] + "_1901_2016_" + paths[country] + ".csv"
    return pathname


def convert_csv_to_dataframe(filepath: str) -> pd.DataFrame:
    """
    A function that converts the .csv data into a pandas DataFrame.

    Preconditions:
    - filepath is the path to a valid csv file

    >>> convert_csv_to_dataframe("datasets/datasets/pr_1901_2016_BLR.csv")
          Rainfall - (MM)   Year    Statistics   Country  ISO3
    0             25.1116   1901   Jan Average   Belarus   BLR
    1             31.8982   1901   Feb Average   Belarus   BLR
    2             45.5625   1901   Mar Average   Belarus   BLR
    3             54.3134   1901   Apr Average   Belarus   BLR
    4             32.6396   1901   May Average   Belarus   BLR
    ...               ...    ...           ...       ...   ...
    1387          49.8312   2016   Aug Average   Belarus   BLR
    1388          24.5396   2016   Sep Average   Belarus   BLR
    1389         104.4580   2016   Oct Average   Belarus   BLR
    1390          55.1826   2016   Nov Average   Belarus   BLR
    1391          48.6336   2016   Dec Average   Belarus   BLR
    <BLANKLINE>
    [1392 rows x 5 columns]
    """

    data = pd.read_csv(filepath)
    return data


def change_df_value(df: pd.DataFrame, col: str, row: int, val: any) -> None:
    """Change the value of df for the given cell at col and row to val

    Preconditions:
        - col in df
        - row < len(df[col])
    """
    df.iloc[row, df.columns.get_loc(col)] = val


def get_df_value(df: pd.DataFrame, col: str, row: int) -> any:
    """Return the value at the given cell in df

    Preconditions:
        - col in df
        - row < len(df[col])
    """
    col_index = list(df.axes[1]).index(col)
    return df.values[row][col_index]


def reformat_df(df: pd.DataFrame) -> None:
    """Mutate df to remove and modify column names where appropriate

    Preconditions:
        - " Statistics" in df
        - " ISO3" in df
        - " Year" in df
        - " Country" in df
        - all(isinstance(row[1], int) for row in list(df.values))
        - all(" " in row[2] for row in list(df.values))
        - all(row[2].split(" ")[1] in
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for row in list(df.values))
    """

    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
        "Nov", "Dec"
    ]
    # For each row, change the " Statistics" column to a datetime.date value given
    # the row's year and month
    for row_num in range(0, len(df.values)):
        row = list(df.values[row_num])
        current_year = row[1]
        # We add 1 because the index for a given month is
        # 1 less than the datetime.datetime value for the month
        current_month = months.index(row[2].split(" ")[1]) + 1
        new_date = dt.date(current_year, current_month,
                           1)  # Day is not tracked; values are always 1

        change_df_value(df, " Statistics", row_num, new_date)

    del df[" ISO3"]
    del df[" Year"]
    del df[" Country"]
    if df.axes[1][0] == "Rainfall - (MM)":
        df.columns = ["rain", "date"]
    elif df.axes[1][0] == "Temperature - (Celsius)":
        df.columns = ["temp", "date"]


def sort_by_month(df: pd.DataFrame) -> Dict[int, pd.DataFrame]:
    """
    Return a set mapping month number to a dataframe consisting of data for that month

    Preconditions:
        - "date" in df
        - all([isinstance(get_df_value(df, "date", row_num), dt.datetime)
        for row_num in range(0, len(df.values))])
    """
    df_dict = {month: pd.DataFrame(None, columns=df.columns) for month in range(0, 12)}

    for row_num in range(0, len(df.values)):
        month_of_row = get_df_value(df, "date", row_num).month
        key = (month_of_row - 1) % 12

        row = list(df.values[row_num])

        new_val = row[0]
        new_date = row[1]
        df2 = pd.DataFrame([[new_val, new_date]], columns=df.columns)
        df_dict[key] = df_dict[key].append(df2, ignore_index=True)

    return df_dict


def combine_df(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Combine two dataframes into one

    Preconditions:
        - "date" in df1 and "date" in df2
        - "temp" in df1 and "temp" in df2
        - "rain" in df1 and "rain" in df2
    """
    new_df = df1.copy()
    another_df = df2.copy()
    new_df[another_df.columns[0]] = another_df[another_df.columns[0]]

    new_df = new_df[["date", "temp", "rain"]]

    return new_df


def get_country_data(country: str) -> Dict[int, pd.DataFrame]:
    """
    Return a dict mapping month indexes to corresponding combine_df outputs for the given country

    Preconditions:
        - country in {"Belarus", "Great Britain", "Greenland", "Malaysia", "Saudi Arabia"}
    """

    # DataFrame for country's rain data
    rain = convert_csv_to_dataframe(get_path(country, "rain"))
    reformat_df(rain)

    # DataFrame for country's temp data
    temp = convert_csv_to_dataframe(get_path(country, "temp"))
    reformat_df(temp)

    rain_by_month = sort_by_month(rain)
    temp_by_month = sort_by_month(temp)

    df_dict = {
        month: pd.DataFrame(None, columns=["date", "temp", "rain"])
        for month in range(0, 12)}
    for i in range(0, 12):
        df_dict[i] = combine_df(rain_by_month[i], temp_by_month[i])

    return df_dict


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1000)
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas', 'datetime', 'sys'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200'],
        'max-nested-blocks': 4
    })

    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
