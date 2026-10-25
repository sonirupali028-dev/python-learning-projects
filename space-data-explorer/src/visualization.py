import matplotlib.pyplot as plt


def create_planet_graph(data):
    # Planet diameters
    plt.figure(figsize=(10, 6))

    plt.bar(data["Planet"], data["Diameter_km"])

    plt.title("Comparison of Planet Diameters")
    plt.xlabel("Planet")
    plt.ylabel("Diameter (km)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("outputs/planet_comparison.png")
    plt.show()

    # Graph 2: Distance from the Sun
    plt.figure(figsize=(10, 6))

    plt.bar(
        data["Planet"],
        data["Distance_from_Sun_million_km"]
    )

    plt.title("Distance of Planets from the Sun")
    plt.xlabel("Planet")
    plt.ylabel("Distance (million km)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("outputs/planet_distances.png")
    plt.show()