# IGNOU BCA Notice Scraper 🤖

An automated web scraper built with Python that monitors the IGNOU Regional Centre website for new practical schedules, assignment updates, and notices, sending real-time alerts directly to a Discord server via Webhooks.

## Features
* **Automated Polling:** Runs daily via GitHub Actions.
* **State Management:** Remembers previously sent notices using a local JSON memory file to prevent spam.
* **Smart Parsing:** Filters out irrelevant navigation links and only delivers absolute URLs for actual notices.

## Tech Stack
* Python 3.10
* `requests` & `beautifulsoup4` (Web Scraping)
* GitHub Actions (CI/CD & Automation)
* Discord Webhooks (Notifications)

## Setup for Local Development
1. Clone the repository.
2. Install requirements: `pip install requests beautifulsoup4`
3. Set your Discord webhook URL as an environment variable: `export DISCORD_WEBHOOK="your_url_here"`
4. Run the script: `python main.py`
