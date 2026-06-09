import sys
from datetime import datetime
import requests


def fetch_data():
    """Fetches placeholder data from a public API."""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}", file=sys.stderr)
        return {}


def generate_log(log_data):
    """Writes a list of log entries to a dated file and returns the filename."""
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list of entries")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    return filename


def write_log_to_file(api_data):
    """Processes API data and writes a summary log file."""
    log_entries = [
        "User logged in",
        f"Fetched API Title: {api_data.get('title', 'No title found')}",
        "Report exported successfully"
    ]
    return generate_log(log_entries)


if __name__ == "__main__":
    print("Initializing automation tool...")
    post_data = fetch_data()
    filename = write_log_to_file(post_data)
    print(f"Success! Log written to {filename}")
