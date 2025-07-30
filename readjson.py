import json, requests, os 
from main import integrations_json_data
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Function to connect to the API and retrieve integration data

def connect_to_api(url, payload=None, headers=None):
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    if not user or not password:
        raise ValueError("User and password must be set in environment variables.")
    else:
        try:
            response = requests.get(
                url, params=payload,
                auth=(
                    user,
                    password
                ), 
                headers=headers
            )
            response.raise_for_status()  # Raise an error for bad responses
            try:
                # Check if the response is JSON
                return response.json()
            except json.JSONDecodeError:
                raise ValueError("Response content is not valid JSON.")
        except requests.exceptions.RequestException as e: # Handle network-related errors
            raise ValueError(f"Error connecting to API: {e}")

# the code below is commented out because it is not used in the current context
# just a testing code to see if the function works

'''
def connect_to_api():
    with open('sampleIntegration.json', 'r') as file:
        data = json.load(file)
    return data
integrations_json = connect_to_api()
'''

# Function to process the JSON data and return the version of a specific integration
# This function is called in main.pystar

def processingJson(integration_excel_name):
    # integrations_json = connect_to_api()
    if integrations_json_data is not None:
        for item in integrations_json_data["items"]:
            try:   
                if item["name"] == integration_excel_name:
                    return item["version"]
            except KeyError:
                print('Operation failed due to invalid data or structure.')
                continue
            except TypeError:
                print(f'for {item['name']} no data found.')
                continue


# the code below is commented out because it is not used in the current context
# just a testing code to see if the function works
'''for item in integrations_json["items"]:
    processingJson(item["name"])'''
# processingJson()