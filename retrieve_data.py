import requests
import json
import os
from dotenv import load_dotenv, dotenv_values

# URL for the ThingSpeak API
url = target_cane_id = os.getenv("url_retrieve")


load_dotenv()
target_cane_id = os.getenv("target_cane_id")
target_security_code = os.getenv("target_security_code")


response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    channel_data = data.get('channel', {})
    feeds = data.get('feeds', [])

    # Prepare the response in the requested format
    formatted_response = {
        "channel": {
            "id": channel_data.get("id", ""),
            "name": channel_data.get("name", ""),
            "description": channel_data.get("description", ""),
            "latitude": channel_data.get("latitude", "0.0"),
            "longitude": channel_data.get("longitude", "0.0"),
            "field1": "Location",
            "field2": "Security Key",
            "field3": "Smart Cane ID",
            "field4": "Emergency Status",
            "field5": "User Name",
            "field6": "GeoFencing",
            "field7": "Battery level",
            "created_at": channel_data.get("created_at", ""),
            "updated_at": channel_data.get("updated_at", ""),
            "last_entry_id": channel_data.get("last_entry_id", "")
        },
        "feeds": []
    }

    # Loop through the feeds and process each feed's field data
    for feed in feeds:
        try:
            cane_id = feed.get('field3')
            security_code = feed.get('field2')
            emergency_status = feed.get('field4')
            user_name = feed.get('field5')
            geo_fencing = feed.get('field6')
            battery_level = feed.get('field7')

            print(f"Processing feed: {feed}")

            # Check if the current feed matches the target CaneID and Security Code
            if cane_id == target_cane_id and security_code == target_security_code:
                feed_entry = {
                    "created_at": feed.get("created_at", ""),
                    "entry_id": feed.get("entry_id", ""),
                    "field1": feed.get("field1", "Lat: 0.00, Lon: 0.00"),
                    "field2": security_code,
                    "field3": cane_id,
                    "field4": emergency_status,
                    "field5": user_name,
                    "field6": geo_fencing,
                    "field7": battery_level
                }
                formatted_response["feeds"].append(feed_entry)

        except Exception as e:
            print(f"Error processing feed: {e}")


    if not formatted_response["feeds"]:
        print("No matching feeds found. Check your CaneID and Security Code.")
    else:
        print(f"Found {len(formatted_response['feeds'])} matching feeds.")

    print(json.dumps(formatted_response, indent=4))

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.text)
