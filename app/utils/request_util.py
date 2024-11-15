import requests

def get(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during GET request: {e}")
        return None

# Function to make a POST request
def post(url, data=None, headers=None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request: {e}")
        return None

# Function to make a DELETE request
def delete(url, params=None, headers=None):
    try:
        response = requests.delete(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during DELETE request: {e}")
        return None