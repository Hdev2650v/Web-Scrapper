import requests
from bs4 import BeautifulSoup
import json
import os

BASE_URL = "http://rcdelhi2.ignou.ac.in"
# --- 1. Configuration ---
# We grab the webhook from an environment variable for security
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

if not WEBHOOK_URL:
    raise ValueError("WEBHOOK_URL is not configured")
IGNOU_URL = "http://rcdelhi2.ignou.ac.in/news/1"
STATE_FILE = "seen_links.json"

# --- 2. Load Memory (State) ---
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        seen_links = json.load(f)
else:
    seen_links = []

# --- 3. Fetch Data (HTTP GET) ---
print("Fetching IGNOU website...")
response = requests.get(IGNOU_URL)
soup = BeautifulSoup(response.text, "html.parser")

new_announcements = []

# --- 4. Parse HTML ---
# This looks for all hyperlink tags <a>. You may need to inspect the
# IGNOU website's HTML and change 'a' to a specific div class if they update it.
for link in soup.find_all("a"):
    href = link.get("href")
    text = link.get_text(strip=True)

    # Check if href exists AND if it's an actual announcement link
    if href and "/news/detail/" in href:
        # Fix the broken link by appending the base URL
        if not href.startswith("http"):
            full_url = BASE_URL + href
        else:
            full_url = href

        # Check our memory to see if we've sent this full URL before
        if full_url not in seen_links and len(text) > 5:
            new_announcements.append({"title": text, "url": full_url})
            seen_links.append(full_url)

# --- 5. Send to Discord (HTTP POST) ---
for item in new_announcements:
    # Discord expects a JSON payload with a "content" key
    message = {"content": f"🚨 **New IGNOU Update:** {item['title']}\n🔗 {item['url']}"}
    requests.post(WEBHOOK_URL, json=message)
    print(f"Sent: {item['title']}")

# --- 6. Save Memory ---
with open(STATE_FILE, "w") as f:
    json.dump(seen_links, f)
