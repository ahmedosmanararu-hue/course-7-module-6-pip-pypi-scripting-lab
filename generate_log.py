from lib.generate_log import fetch_data, generate_log


if __name__ == "__main__":
    print("Starting log automation...")
    api_post = fetch_data()
    log_entries = [
        "User logged in",
        f"Fetched API Title: {api_post.get('title', 'No title found')}",
        "Report exported successfully"
    ]
    filename = generate_log(log_entries)
    print(f"Log written to {filename}")
