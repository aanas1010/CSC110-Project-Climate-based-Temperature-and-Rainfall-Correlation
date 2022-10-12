"""CSC110 Fall 2020: Project Phase 2

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students and Faculty
involved in CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2020 Shayaan Khan, Markus Nimi, Matthew Chan and Aabid Anas.
"""
from graph_handling import graph_data, get_correlations
from dataframe_handling import get_country_data
import matplotlib.pyplot as plt
import tkinter as tk


class MainMenu:
    """
    A class that sets up the main menu interface with tkinter
    """

    def __init__(self, main) -> None:
        self.analyze_window = None
        self.months = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
            "Oct", "Nov", "Dec"
        ]
        self.countries = [
            "Continental (Belarus)", "Temperate (Great Britain)", "Polar (Greenland)", "Tropical (Malaysia)",
            "Desert (Saudi Arabia)"
        ]

        self.main = main
        main.title("Project Data Analysis")

        self.main_title = tk.Label(
            main, text="Regional Climate Temperature and Rainfall")
        self.main_title.pack()

        self.month_var = tk.StringVar(main)
        self.month_var.set("Jan")
        self.month_label = tk.Label(main, text="Select Month:")
        self.month_label.pack()
        self.month_select = tk.OptionMenu(main, self.month_var, *self.months)
        self.month_select.pack()

        self.country_var = tk.StringVar(main)
        self.country_var.set("Continental (Belarus)")
        self.country_label = tk.Label(main, text="Select Region:")
        self.country_label.pack()
        self.country_select = tk.OptionMenu(main, self.country_var,
                                            *self.countries)
        self.country_select.pack()

        self.graph_button = tk.Button(main, text="Display Graph", command=self.graph)
        self.graph_button.pack()

        self.analyze_button = tk.Button(main, text="Analyze Data", command=self.analyze)
        self.analyze_button.pack()

    def graph(self) -> None:
        """
        Open a new window and graph the given country and month over time
        """
        plt.close(fig=None)
        month_index = list.index(self.months, self.month_var.get())
        country = self.country_var.get().split("(")[1].split(")")[0]
        data = dict_of_countries[country][month_index]
        graph_data(data, country, month_index)

    def analyze(self) -> None:
        """
        Open a new window and show the correlations for the given country's and month's DataFrame
        """
        if self.analyze_window is not None:
            self.analyze_window.destroy()
        self.analyze_window = tk.Toplevel(self.main)
        self.analyze_window.geometry("500x175")
        definition = "The Pearson correlation coefficient, or Pearson’s R for short," \
                     "is a measure of the linear association between two variables. " \
                     "The correlations range from 1 to -1. 1 is a perfect positive correlation, " \
                     "and -1 is a perfect negative correlation. The larger the magnitude " \
                     "of a correlation, the stronger the linear association."
        month_index = list.index(self.months, self.month_var.get())
        country = self.country_var.get().split("(")[1].split(")")[0]
        data = dict_of_countries[country][month_index]
        _, analysis = get_correlations(data, country, month_index)
        corr_label = tk.Label(self.analyze_window, text="Pearson's Correlation Coefficient")
        corr_label.pack()
        definition_label = tk.Label(self.analyze_window, text=definition, wraplength=480)
        definition_label.pack(fill="both", expand=True)
        written_analysis = tk.Label(self.analyze_window, text=analysis, wraplength=480)
        written_analysis.pack(fill="both", expand=True)


set_of_countries = {"Belarus", "Great Britain", "Greenland", "Malaysia", "Saudi Arabia"}
# Let the user know that the program is running as intended
print("Loading Data...")
# Create a dictionary mapping all countries to corresponding pd.DataFrame values
dict_of_countries = {country: get_country_data(country) for country in set_of_countries}
print("Data Loaded Successfully!")

if __name__ == "__main__":
    # Run the MainMenu class
    root = tk.Tk()
    gui = MainMenu(root)
    root.mainloop()
