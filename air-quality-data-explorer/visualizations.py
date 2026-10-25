"""
visualizations.py
Creates and saves high-quality Matplotlib charts into an automatically created output folder.
"""

import os
import matplotlib.pyplot as plt


def ensure_output_directory(output_dir="output"):
    """Ensures the output directory exists, creating it automatically if needed."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def create_city_bar_chart(df, output_dir="output"):
    """Creates a bar chart comparing average PM2.5 concentrations across cities."""
    ensure_output_directory(output_dir)

    # Calculate city averages
    city_avg = df.groupby("City")["PM2.5"].mean()

    # Set up figure size and style
    plt.figure(figsize=(8, 5))
    colors = ["#2b5c8f", "#d95f02", "#7570b3"]
    bars = plt.bar(
        city_avg.index, city_avg.values, color=colors, width=0.5, edgecolor="black"
    )

    # Add labels, title, and styling
    plt.title(
        "Average PM2.5 Concentration by City", fontsize=14, fontweight="bold", pad=15
    )
    plt.xlabel("City", fontsize=12, labelpad=10)
    plt.ylabel("Average PM2.5 (µg/m³)", fontsize=12, labelpad=10)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Add data value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 1,
            f"{height:.1f}",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.tight_layout()

    # Save figure
    file_path = os.path.join(output_dir, "city_pm25_bar_chart.png")
    plt.savefig(file_path, dpi=300)
    plt.close()
    print(f"[Saved] City bar chart successfully saved to: {file_path}")


def create_trend_line_chart(df, selected_city="Tokyo", output_dir="output"):
    """Creates a line chart showing how PM2.5 changes over time for one selected city."""
    ensure_output_directory(output_dir)

    # Filter data for the chosen city
    city_data = df[df["City"] == selected_city].copy()
    city_data["Date"] = pd.to_datetime(city_data["Date"])
    city_data = city_data.sort_values("Date")

    plt.figure(figsize=(9, 5))
    plt.plot(
        city_data["Date"],
        city_data["PM2.5"],
        marker="o",
        linestyle="-",
        color="#2b5c8f",
        linewidth=2,
        markersize=6,
        label=f"{selected_city} PM2.5",
    )

    # Add titles, labels, and legend
    plt.title(
        f"PM2.5 Trend Over Time in {selected_city}",
        fontsize=14,
        fontweight="bold",
        pad=15,
    )
    plt.xlabel("Date", fontsize=12, labelpad=10)
    plt.ylabel("PM2.5 Concentration (µg/m³)", fontsize=12, labelpad=10)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(loc="upper right")

    # Format date ticks nicely
    plt.gcf().autofmt_xdate()
    plt.tight_layout()

    # Save figure
    file_path = os.path.join(output_dir, f"{selected_city.lower()}_pm25_trend.png")
    plt.savefig(file_path, dpi=300)
    plt.close()
    print(f"[Saved] Trend line chart successfully saved to: {file_path}")