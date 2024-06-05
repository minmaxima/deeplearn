#--------------------
# Class Definition:
#     * ExternalUserInfoEndpoint class handles the configuration, data retrieval, and processing.
#     * The __init__ method initializes the base URL, endpoint, and bearer token.
#
# Methods:
#     * get_user_info: Sends a GET request to the endpoint with Bearer authentication and retrieves user information.
#     * process_user_info: Processes the retrieved user information (e.g., printing and saving it to a file).
#     * run: Combines the retrieval and processing steps, handling any request exceptions.
# 
# Scheduler:
#     * Uses apscheduler to schedule the task to run at regular intervals (e.g., every hour).
#     * Starts the scheduler and handles shutdown gracefully.
# Usage:
#   Replace "https://api.example.com", "external-user-info", and "your_bearer_token_here" with your actual API base URL, endpoint, and bearer token.
#   Adjust the scheduling interval in scheduler.add_job as needed.
# -------------------------------

import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler

class ExternalUserInfoEndpoint:
    def __init__(self, base_url, endpoint, token):
        self.base_url = base_url
        self.endpoint = endpoint
        self.token = token

    def get_user_info(self):
        url = f"{self.base_url}/{self.endpoint}"
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def process_user_info(self, user_info):
        # Process the user info as needed
        print("Processing user info:", user_info)
        # Example: Save user info to a file (or integrate into your system)
        with open('user_info.json', 'w') as f:
            json.dump(user_info, f, indent=4)

    def run(self):
        try:
            user_info = self.get_user_info()
            self.process_user_info(user_info)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

def main():
    # Configuration
    base_url = "https://api.example.com"
    endpoint = "external-user-info"
    token = "your_bearer_token_here"

    # Create an instance of ExternalUserInfoEndpoint
    user_info_endpoint = ExternalUserInfoEndpoint(base_url, endpoint, token)

    # Schedule the task
    scheduler = BlockingScheduler()
    scheduler.add_job(user_info_endpoint.run, 'interval', hours=1)  # Adjust interval as needed
    print("Scheduler started. Press Ctrl+C to exit.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")

if __name__ == "__main__":
    main()
