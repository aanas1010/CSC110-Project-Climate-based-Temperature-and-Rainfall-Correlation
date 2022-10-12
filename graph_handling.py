"""CSC110 Fall 2020: Project Phase 2

Module Description
==================
This module contains functions for graphing and finding correlations between data
using the Seaborn and Scipy libraries

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students and Faculty
involved in CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2020 Shayaan Khan, Markus Nimi, Matthew Chan and Aabid Anas.
"""

from scipy.stats import pearsonr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def graph_data(df: pd.DataFrame, country: str, month: int) -> None:
    """
    Graph the df data on a scatterplot

    Preconditions:
        - all(col in df for col in {"rain", "temp", "date"})
        - all(isinstance(df["date"][row], dt.date)
        for row in len(df["date"]))
        - all(isinstance(df["rain"][row], float)
        for row in len(df["rain"]))
        - all(isinstance(df["temp"][row], float)
        for row in len(df["temp"]))
    """

    years = [time.year for time in df['date']]

    ax1 = plt.subplots()[1]
    color = 'Red'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Average Monthly Temperature (°c)', color=color)
    data1 = sns.regplot(x=years, y=df["temp"], order=3,
                        ci=None, ax=ax1, color=color, label="Temperature")
    ax1.tick_params(axis='y', labelcolor=color)
    data1.set(ylabel='Average Monthly Temperature (°c)')

    ax2 = ax1.twinx()
    color = 'Blue'
    ax2.set_ylabel('Monthly Rainfall (mm)', color=color)
    data2 = sns.regplot(x=years, y=df["rain"], order=3,
                        ci=None, ax=ax2, color=color, label="Rainfall")
    ax2.tick_params(axis='y', labelcolor=color)
    data2.set(ylabel='Monthly Rainfall (mm)')

    month_list = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
    plt.title("Monthly Rainfall and Average Temperature\nfor the month of "
              + month_list[month] + " in " + country)
    plt.show()


def get_correlations(df: pd.DataFrame, country: str, month: int) -> (float, str):
    """
    Get the correlations between temperature and rainfall

    Preconditions:
        - all(isinstance(df["date"][row], dt.date)
        for row in len(df["date"]))
        - all(isinstance(df["rain"][row], float)
        for row in len(df["rain"]))
        - all(isinstance(df["temp"][row], float)
        for row in len(df["temp"]))
        - country in {"Belarus", "Great Britain", "Greenland", "Malaysia", "Saudi Arabia"}
        - 0 <= month <= 11
    """

    list_of_months = [
        "January", "Febuary", "March", "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]
    corr_co = float(pearsonr(df["temp"], df["rain"])[0])
    analysis = ""
    if 1 >= corr_co > 0.7:
        analysis = "strong positive"
    elif 0.7 >= corr_co > 0.4:
        analysis = "moderate positive"
    elif 0.4 >= corr_co > 0.1:
        analysis = "weak Positive"
    elif 0.1 >= corr_co >= -0.1:
        analysis = "negligible"
    elif -0.1 > corr_co >= -0.4:
        analysis = "weak Negative"
    elif -0.4 > corr_co >= -0.7:
        analysis = "moderate Negative"
    elif -0.7 > corr_co >= -1:
        analysis = "strong Negative"
    statement = "The correlation between temperature and rainfall was " \
                + str(corr_co) + ". This means there is a " \
                + analysis \
                + " correlation between temperature and rainfall for " \
                + country + " in " + list_of_months[month] + "."
    return corr_co, statement


def correlation_histogram(dict_of_countries: dict, set_of_countries: set) -> None:
    """
    Graph the correlations in dict_of_countries on a
    histogram and compare it to a normal distribution

    Preconditions:
        - all(country in dict_of_countries for country in set_of_countries)
    """

    corr_data = [get_correlations(dict_of_countries[country][num], country, num)[0]
                 for num in range(0, 12) for country in set_of_countries]
    new_df = pd.DataFrame(corr_data, columns=['Correlations between Rain and Temperature'])
    new_df.hist(bins=15)


if __name__ == '__main__':    
    import sys
    # Problem between matplotlib.pyplot and seaborn imports; recursion depth exceeded
    sys.setrecursionlimit(1024)
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas',
                          'seaborn', 'sys', 'matplotlib.pyplot', 'scipy.stats'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200'],
        'max-nested-blocks': 4
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
