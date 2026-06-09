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


def write_log_to_file(api_data):
    """Processes the data and appends it to a timestamped log file."""
    log_entries = [
        "User logged in",
        f"API Request Success - Fetched Title: '{api_data.get('title', 'No Title')}'",
        "Report exported successfully"
    ]
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            for entry in log_entries:
                file.write(f"[{datetime.now().strftime('%H:%M:%S')}] {entry}\n")
        print(f"Success! Log written to {filename}")
    except IOError as e:
        print(f"File I/O Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    print("Initializing automation tool...")    
    post_data = fetch_data()
    write_log_to_file(post_data)
    print("Automation execution finished.")