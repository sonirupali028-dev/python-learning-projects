# Air Quality Data Explorer

A beginner-friendly data analysis program built with Python, NumPy, Pandas, and Matplotlib. Developed as a practice project while learning data science through GCI World (University of Tokyo online course).

---

## Project Overview

The **Air Quality Data Explorer** loads a synthetic air quality dataset, performs data inspection and cleaning, calculates vital statistics using NumPy and Pandas, and exports publication-quality visual charts into an automated output folder.

> **Disclaimer:** The dataset included in this project (`air_quality.csv`) is **synthetic sample data** created purely for educational practice. It does not represent actual real-world air pollution measurements and should not be used to draw scientific conclusions about air quality.

---

## Features

1. **CSV Loading & Inspection:** Reads tabular records into a Pandas DataFrame and checks for missing entries.
2. **Data Cleaning:** Safely handles missing values by imputing city-specific medians.
3. **Statistical Analysis:** Computes overall averages, minimums, maximums, and city-wise breakdowns using NumPy and Pandas.
4. **Automated Visualizations:** Generates and saves a city comparison bar chart and a temporal trend line chart as high-resolution PNG images.

---

## Technologies Used

- **Python 3.x** (Standard Library)
- **Pandas** (Data loading, cleaning, and grouping)
- **NumPy** (Numerical calculations and array operations)
- **Matplotlib** (Data visualization and plotting)

---

## Folder Structure

```text
air-quality-data-explorer/
│
├── main.py             # Orchestrates the entire program sequence
├── data.py             # Handles data loading and missing value imputation
├── analysis.py         # Computes statistical metrics and terminal summary
├── visualizations.py   # Generates and exports Matplotlib charts
├── air_quality.csv     # Synthetic sample dataset
├── requirements.txt    # External library dependencies
├── README.md           # Project documentation
└── .gitignore          # Git exclusion rules