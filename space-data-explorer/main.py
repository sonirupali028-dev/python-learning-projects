from src.data_loader import load_planet_data
from src.analysis import analyze_planets
from src.visualization import create_planet_graph
from src.nasa_api import get_astronomy_picture


def main():
    print("SPACE DATA EXPLORER")
    print("=" * 30)

    # Load planetary data
    planets = load_planet_data()

    print("\nPlanetary Dataset:")
    print(planets.to_string(index=False))

    # Analyze the data
    results = analyze_planets(planets)

    print("\n--- Analysis Results ---")
    print("Average Diameter:", results["average_diameter"], "km")
    print("Largest Planet:", results["largest_planet"])
    print("Smallest Planet:", results["smallest_planet"])

    # Create a graph
    create_planet_graph(planets)

    # Fetch astronomy information
    get_astronomy_picture()


if __name__ == "__main__":
    main()