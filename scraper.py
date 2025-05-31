# scraper.py
import requests
import json
from datetime import datetime

def fetch_discourse_posts(base_url, start_date, end_date):
    headers = {
        "Api-Key": "<YOUR_DISCOURSE_API_KEY>",  # If needed
        "Api-Username": "system"
    }
    results = []
    for page in range(1, 20):  # Adjust range for more pages
        url = f"{base_url}/latest.json?page={page}"
        r = requests.get(url, headers=headers)
        data = r.json()

        for topic in data.get("topic_list", {}).get("topics", []):
            created = topic["created_at"]
            created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
            if start_date <= created_dt <= end_date:
                results.append(topic)

    with open("data/discourse_posts.json", "w") as f:
        json.dump(results, f, indent=2)

# Example usage
if __name__ == "__main__":
    fetch_discourse_posts("https://discourse.onlinedegree.iitm.ac.in", datetime(2025, 1, 1), datetime(2025, 4, 14))
