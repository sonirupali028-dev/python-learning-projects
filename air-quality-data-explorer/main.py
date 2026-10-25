"""
main.py
Runs the complete Air Quality Data Explorer program in the correct sequence:
1. Load CSV data
2. Clean data (handle missing values)
3. Calculate summary statistics
4. Print terminal summary
5. Generate and save high-quality visualizations
"""

from analysis import calculate_summary_statistics, print_summary
from data import clean_data, load_air_quality_data
from visualizations import create_city_bar_chart, create_trend_line_chart


def main():
    print("Starting Air Quality Data Explorer...")

    # Step 1 & 2: Load and clean dataset
    raw_df = load_air_quality_data("air_quality.csv")
    cleaned_df = clean_data(raw_df)

    # Step 3: Calculate summary statistics
    stats = calculate_summary_statistics(cleaned_df)

    # Step 4: Print terminal summary
    print_summary(stats)

    # Step 5: Generate and save visualizations
    print("Generating charts...")
    create_city_bar_chart(cleaned_df, output_dir="output")
    create_trend_line_chart(cleaned_df, selected_city="Tokyo", output_dir="output")

    print("\nProgram completed successfully! All charts saved in the 'output' folder.")


if __name__ == "__main__":
    main()