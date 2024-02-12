import json
import pandas as pd
from bs4 import BeautifulSoup
from crawl import HttpRequestManager

# Load JSON file
json_file_path = 'phone_models.json'
with open(json_file_path, 'r') as f:
    phone_links = json.load(f)

# Load CSV file
csv_file_path = 'flattened_data.csv'
data = pd.read_csv(csv_file_path)

# Check for multiple configurations
data['Config_Count'] = data['Memory_Internal'].apply(lambda x: len(str(x).split(',')) if pd.notna(x) else 0)
devices_with_multiple_configs = data[data['Config_Count'] > 1]


def scrape_pricing(rsp):

    # Parse the HTML content of the page
    soup = BeautifulSoup(rsp, 'html.parser')
    # save the parsed content to a file

    table = soup.find('table', class_='pricing inline widget')

    # Initialize a dictionary to hold configuration and its first price
    if table:
        config_prices = {}

        for tr in table.find_all('tr'):
            # Extracting configuration and the first price link
            config = tr.find('td').text.strip()
            price_link = tr.find('a')
            if price_link:
                price = price_link.text.strip()
                config_prices[config] = price

        return config_prices
    else:
        return None

# Example usage
final_dic={}
html = HttpRequestManager()

for index, row in devices_with_multiple_configs.iterrows():
    model_url = None

    for brand, models in phone_links.items():
        # Adjust the key access if your CSV uses different naming
        if row['model'] in models.keys():
            model_url = models[row['model']]
            break  # Found the URL, no need to continue searching
    if model_url:
        final_dic[row['model']] = scrape_pricing(html.fetch(model_url))
        print(f"Scraped {final_dic[row['model']]}")
    else:
        print(f"No URL found for {row['model']}")

# Save the dictionary to a JSON file
with open('pricing.json', 'w') as f:
    json.dump(final_dic, f, indent=4)
