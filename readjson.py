import json, requests, os 
from main import integrations_json_data
# Function to connect to the API and retrieve integration data

def connect_to_api(url, payload=None, headers=None):
    try:
        response = requests.get(
            url, params=payload,
            auth=(
                os.getenv('USER'),
                os.getenv('PASSWORD')
            ), 
            headers=headers
        )
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return None

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
                    print(item["version"]) 
            except KeyError:
                print('Invalid JSON structure')
                continue
            except TypeError:
                return 'No items found.'


# the code below is commented out because it is not used in the current context
# just a testing code to see if the function works
'''for item in integrations_json["items"]:
    processingJson(item["name"])'''
# processingJson()