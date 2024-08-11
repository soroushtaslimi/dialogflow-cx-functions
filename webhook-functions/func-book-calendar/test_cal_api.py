import requests

# Replace with your actual API key or token
api_key = 'your_api_key_here'
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# The endpoint for creating an event (replace with actual endpoint)
url = 'https://api.cal.com/v1/events'

# Replace with actual data required by the API to create an event
data = {
    "title": "Meeting with Bob",
    "start": "2024-08-10T15:00:00Z",
    "end": "2024-08-10T16:00:00Z",
    "location": "Online",
    "description": "Discuss the project details.",
    # Include other necessary fields
}

response = requests.post(url, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 201:
    print("Event created successfully")
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
