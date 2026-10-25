import pandas as pd


def load_planet_data():
    file_path = "data/planets.csv"

    data = pd.read_csv(file_path)

    return data