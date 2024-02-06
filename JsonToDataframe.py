import json
import pandas as pd

# Assuming `json_file_path` is the path to your JSON file
json_file_path = 'phone_info.json'

# Load the JSON data
with open(json_file_path) as file:
    data = json.load(file)


# Example flatten_json function
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], f'{name}{a}_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, f'{name}{i}_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# Function to process and flatten entire JSON file
def process_json(data):
    flattened_data = []

    for brand, models in data.items():
        for model, details in models.items():
            flat_details = flatten_json(details)
            flat_details['brand'] = brand
            flat_details['model'] = model
            flattened_data.append(flat_details)

    return pd.DataFrame(flattened_data)


# Using the function to process the JSON data
df = process_json(data)
df.to_csv('flattened_data.csv', index=False)

print(df.head())
