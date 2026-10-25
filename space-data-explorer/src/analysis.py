import numpy as np


def analyze_planets(data):
    diameters = data["Diameter_km"]

    average_diameter = np.mean(diameters)

    largest_planet = data.loc[
        data["Diameter_km"].idxmax(), "Planet"
    ]

    smallest_planet = data.loc[
        data["Diameter_km"].idxmin(), "Planet"
    ]

    results = {
        "average_diameter": round(average_diameter, 2),
        "largest_planet": largest_planet,
        "smallest_planet": smallest_planet
    }

    return results