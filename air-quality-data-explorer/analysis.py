"""
analysis.py
Performs statistical calculations using Pandas and NumPy on the cleaned DataFrame.
"""

import numpy as np


def calculate_summary_statistics(df):
    """Calculates summary metrics from the latest current readings."""
    current = df[df["Record type"] == "Current"]
    pm25_values = current["PM2.5"].dropna().to_numpy()
    pm10_values = current["PM10"].dropna().to_numpy()

    stats = {
        "avg_pm25": float(np.mean(pm25_values)),
        "avg_pm10": float(np.mean(pm10_values)),
        "min_pm25": float(np.min(pm25_values)),
        "max_pm25": float(np.max(pm25_values)),
        "city_pm25": current.set_index("City")["PM2.5"].to_dict(),
        "city_pm10": current.set_index("City")["PM10"].to_dict(),
        "current_time": current["Date"].max(),
    }
    return stats


def print_summary(stats):
    """Print the latest Indian city readings in a readable format."""
    print("\n" + "=" * 50)
    print("       INDIAN AIR QUALITY - CURRENT ESTIMATES")
    print("=" * 50)
    print(f"Data time (IST): {stats['current_time']}")
    print(f"Average PM2.5 across cities: {stats['avg_pm25']:.2f} µg/m³")
    print(f"Average PM10 across cities : {stats['avg_pm10']:.2f} µg/m³")
    print("\nCurrent city estimates:")
    for city, pm25 in stats["city_pm25"].items():
        pm10 = stats["city_pm10"].get(city)
        pm25_text = f"{pm25:.1f} µg/m³" if pm25 is not None else "unavailable"
        pm10_text = f"{pm10:.1f} µg/m³" if pm10 is not None else "unavailable"
        print(f"  - {city}: PM2.5 {pm25_text}; PM10 {pm10_text}")
    print("\nThese are model-based estimates, not official monitoring-station readings.")
    print("=" * 50 + "\n")