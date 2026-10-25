import re
from html import unescape

import requests


def get_astronomy_picture():
    url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()

        # Handle dict and list responses
        if isinstance(data, list):
            if len(data) == 0:
                print("No astronomy pictures found.")
                return

            data = data[0]

        print("\n--- NASA Astronomy Picture ---")
        print("Title:", data.get("title", "Not available"))
        print("Date:", data.get("date", "Not available"))
        explanation = data.get("explanation", "Not available")

        # for clean up text
        explanation = re.sub(r"<[^>]+>", " ", explanation)
        explanation = unescape(explanation)
        explanation = " ".join(explanation.split())

        print("\nExplanation:")
        print(explanation[:500] + "..." if len(explanation) > 500 else explanation)
        print("Image URL:", data.get("hdurl", "Not available"))

    except requests.RequestException as error:
        print("\nCould not retrieve NASA data.")
        print("Error:", error)

    except (ValueError, AttributeError, TypeError) as error:
        print("\nCould not process NASA data.")
        print("Error:", error)


if __name__ == "__main__":
    get_astronomy_picture()