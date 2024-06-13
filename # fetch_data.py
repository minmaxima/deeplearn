# fetch_data.py

import requests
import json
import datetime

def fetch_data():
    url = "https://api.example.com/endpoint"  # Replace with the actual API endpoint
    headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',  # Replace with your access token
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        # Save the response to a file
        filename = f"data_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Data fetched and saved to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_data()

""" Setting Up the Cron Job
Make the Script Executable:
Ensure your script is executable. You can do this by running:

sh
chmod +x /path/to/fetch_data.py
Edit Crontab:
Open the crontab file for editing:

sh
crontab -e
Add the Cron Job:
Add a new line to schedule the script. For example, to run the script every day at 3 AM, add:

sh
0 3 * * * /usr/bin/python3 /path/to/fetch_data.py >> /path/to/fetch_data.log 2>&1
Replace /usr/bin/python3 with the path to your Python interpreter.
Replace /path/to/fetch_data.py with the full path to your script.
The >> /path/to/fetch_data.log 2>&1 part redirects the script’s output (including errors) to a log file.
Save and Exit:
Save the changes and exit the text editor.

Notes
Environment Variables: If your script depends on specific environment variables, make sure they are set correctly within the cron job or sourced in the script itself.
Permissions: Ensure that the user running the cron job has the necessary permissions to execute the script and write to the log file.
Dependencies: If your script relies on external Python packages, ensure they are installed in the environment where the cron job runs. """