import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv, dotenv_values

# URL for the ThingSpeak API
load_dotenv()
url_send = os.getenv("url_send ")

# API key
api_key = os.getenv("api_key")

# Data to be sent
data = {
    "channel": {
        "id": 2700771,
        "name": "Smart Cane",
        "description": "For storing smart cane details",
        "latitude": "0.0",
        "longitude": "0.0",
        "field1": "Location",
        "field2": "Security Key",
        "field3": "Smart Cane ID",
        "field4": "Emergency Status",
        "field5": "User Name",
        "field6": "GeoFencing",
        "field7": "Battery level",
        "created_at": "2024-10-17T08:15:31Z",
        "updated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "last_entry_id": 297
    },
    "feeds": [
        {
            "field1": "Lat: 0.00, Lon: 0.00",
            "field2": "Ombati986",
            "field3": "Ombati001",
            "field7": "98"
        }
    ]
}

# Headers for the POST request
headers = {
    "Content-Type": "application/json"
}

# Payload including the API key
payload = {
    "api_key": api_key,
    "field1": data["feeds"][0]["field1"],
    "field2": data["feeds"][0]["field2"],
    "field3": data["feeds"][0]["field3"],
    "field7": data["feeds"][0]["field7"]
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers)

# Check response
if response.status_code == 200:
    print("Data sent successfully!")
else:
    print(f"Failed to send data. Status code: {response.status_code}")
    print(response.text)
