import json
import re
import ssl
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import random
from tqdm import tqdm
import csv
import os


class HttpRequestManager:
    def __init__(self, max_retries=5, backoff_factor=3, delay=2.5):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.delay = delay  # Delay in seconds between requests
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

    def fetch(self, url):
        retries = 0
        while retries < self.max_retries:
            time.sleep(self.delay)
            try:
                req = Request(
                    url=url,
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                        "Accept-Language": "en-US,en;q=0.9"}
                )
                response = urlopen(req, context=self.ctx).read().decode('utf-8')
                return response
            except HTTPError as e:
                if e.code in (429, 504):
                    retries += 1
                    sleep_time = self.backoff_factor * (2 ** retries) + random.uniform(0, 1)  # Add some randomness
                    print(f"Retrying in {sleep_time} seconds...")
                    time.sleep(sleep_time)
                else:
                    raise
            except URLError:
                retries += 1
                sleep_time = self.backoff_factor * (2 ** retries) + random.uniform(0, 1)
                time.sleep(sleep_time)
        raise Exception(f"Failed to fetch {url} after {self.max_retries} retries")


class DataExtractor:
    def __init__(self, main_url):
        self.main_url = main_url
        self.http_request_manager = HttpRequestManager()
        self.brand_links = {}
        self.phone_models_links = {}
        self.phone_info = {}
        print("DataExtractor object created")

    def extract_brand_data(self, brand_links_file='brand_links.json'):
        # Check if the file exists
        if os.path.exists(brand_links_file):
            print(f"Loading brand links from {brand_links_file}")
            with open(brand_links_file, 'r') as file:
                self.brand_links = json.load(file)
        else:
            print("Fetching brand links...")
            html = self.http_request_manager.fetch(self.main_url)
            soup = BeautifulSoup(html, "html.parser")

            table = soup.find('table')
            extracted_data = {}
            for row in tqdm(table.find_all('tr')):
                #  for row in table.find_all('tr'):
                cells = row.find_all('td')

                name = re.sub(r'\d+ devices', '', cells[0].text).strip()  # Extract text from the first column
                link = cells[0].find('a')['href']  # Extract the link from the second column
                extracted_data[name] = "https://www.gsmarena.com/" + link

                name = re.sub(r'\d+ devices', '', cells[1].text).strip()  # Extract text from the first column
                link = cells[1].find('a')['href']  # Extract the link from the second column
                extracted_data[name] = "https://www.gsmarena.com/" + link

            self.brand_links = extracted_data
            print("Brand links extracted")

    def extract_phone_models(self, models_list, models_file_path='phone_models.json'):
        # Check if the models file exists and load it if it does
        if os.path.exists(models_file_path):
            print(f"Loading phone models from {models_file_path}")
            with open(models_file_path, 'r') as file:
                self.phone_models_links = json.load(file)
        else:
            print("Phone models file not found, fetching new data...")

            for brand, link in self.brand_links.items():
                if brand in models_list:
                    phone_models = {}
                    while link:
                        html = self.http_request_manager.fetch(link)
                        soup = BeautifulSoup(html, "html.parser")

                        # Extract phone models
                        for item in soup.select('.makers ul li a'):
                            name = item.text.strip()
                            href = 'https://www.gsmarena.com/' + item.get('href')
                            phone_models[name] = href

                        # Check for the next page
                        next_page = soup.find('a', class_='prevnextbutton', title='Next page')
                        if next_page and 'href' in next_page.attrs:
                            link = 'https://www.gsmarena.com/' + next_page.get('href')
                        else:
                            link = None
                    self.phone_models_links[brand] = phone_models
                    self.write_json_each(f'{brand}_models.json', phone_models)
                print("Phone models extracted")

    """def extract_phone_info(self, interested_sections):
        for brands in self.phone_models_links.keys():
            self.phone_info[brands] = {}
        for brand, models in self.phone_models_links.items():
            for model, link in models.items():
                html = self.http_request_manager.fetch(link)
                soup = BeautifulSoup(html, "html.parser")
                extracted_info = {}
                for table in soup.find_all("table"):
                    section = table.find("th").text
                    if section in interested_sections:
                        extracted_info[section] = {}
                        for row in table.find_all("tr"):
                            info_type = row.find("td", class_="ttl").text.strip()
                            info_value = row.find("td", class_="nfo").text.strip()
                            extracted_info[section][info_type] = info_value
                self.phone_info[brand][model] = extracted_info

        print("Phone info extracted")"""


    """def extract_phone_info(self, interested_sections, json_file_path=None):
        if json_file_path:
            with open(json_file_path, 'r') as f:
                local_phone_models_links = json.load(f)

            with open('passed_link.csv', 'w', newline='') as f:
                writer = csv.writer(f)

                for brand, models in local_phone_models_links.keys():
                    self.phone_info[brand] = {}
                for brand, models in local_phone_models_links.items():
                    print(f"Extracting info for {brand}")
                    for model, link in models.items():
                        writer.writerow(link)
                        html = self.http_request_manager.fetch(link)
                        soup = BeautifulSoup(html, "html.parser")
                        extracted_info = {}
                        for section in interested_sections:
                            section_found = False
                            section_data = {}  # Initialize section dictionary to empty by default
                            # Attempt to find the table that contains the section
                            for table in soup.find_all("table"):
                                th = table.find("th")  # Find the <th> element
                                if th and th.text.strip() == section:  # Match the section
                                    section_found = True
                                    for row in table.find_all("tr"):
                                        info_type_cell = row.find("td", class_="ttl")
                                        info_value_cell = row.find("td", class_="nfo")
                                        if info_type_cell and info_value_cell:
                                            info_type = info_type_cell.text.strip()
                                            info_value = info_value_cell.text.strip()
                                            section_data[info_type] = info_value
                                    break  # Break after finding the section
                            if not section_found:
                                section_data = None
                            extracted_info[section] = section_data
                        self.phone_info[brand][model] = extracted_info

        else:
            for brand in self.phone_models_links.keys():
                self.phone_info[brand] = {}  # Initialize brand dictionary
            for brand, models in self.phone_models_links.items():
                print(f"Extracting info for {brand}")
                for model, link in tqdm(models.items()):
                    # for model, link in models.items():
                    html = self.http_request_manager.fetch(link)
                    soup = BeautifulSoup(html, "html.parser")
                    model_info = {}  # Initialize model dictionary
                    for section in interested_sections:
                        section_found = False
                        section_data = {}  # Initialize section dictionary to empty by default
                        # Attempt to find the table that contains the section
                        for table in soup.find_all("table"):
                            th = table.find("th")  # Find the <th> element
                            if th and th.text.strip() == section:  # Match the section
                                section_found = True
                                for row in table.find_all("tr"):
                                    info_type_cell = row.find("td", class_="ttl")
                                    info_value_cell = row.find("td", class_="nfo")
                                    if info_type_cell and info_value_cell:
                                        info_type = info_type_cell.text.strip()
                                        info_value = info_value_cell.text.strip()
                                        section_data[info_type] = info_value
                                break  # Break after finding the section
                        if not section_found:
                            section_data = None  # Or use {} if you prefer an empty dict instead of None
                        model_info[section] = section_data
                    self.phone_info[brand][model] = model_info
"""


    def load_existing_data(self, filepath):
        """Load existing data from a JSON file."""
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self, filepath, data):
        """Save data to a JSON file."""
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

    def extract_phone_info(self, interested_sections, json_file_path='phone_info.json'):
        phone_info = self.load_existing_data(json_file_path)  # Load existing data
        parsed_links = set()  # Set to store parsed links

        # Load previously parsed links
        try:
            with open('passed_link.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    parsed_links.add(row[0])
        except FileNotFoundError:
            print("passed_link.csv not found, creating a new one.")

        # Process models
        with open('passed_link.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            for brand, models in self.phone_models_links.items():
                if brand not in phone_info:
                    phone_info[brand] = {}
                for model, link in models.items():
                    if link in parsed_links:
                        continue  # Skip already parsed links
                    print(f"Extracting info for {model} from {brand}")
                    html = self.http_request_manager.fetch(link)
                    soup = BeautifulSoup(html, "html.parser")
                    extracted_info = self.parse_model_info(soup, interested_sections)
                    phone_info[brand][model] = extracted_info

                    # Add link to parsed links and update the file
                    parsed_links.add(link)
                    writer.writerow([link])

                    # Save updated phone info to JSON after each link
                    self.save_data(json_file_path, phone_info)

        print("Data extraction complete. Results saved.")

    def parse_model_info(self, soup, interested_sections):
        extracted_info = {}
        for section in interested_sections:
            section_data = {}  # Initialize section dictionary to empty by default
            for table in soup.find_all("table"):
                th = table.find("th")
                if th and th.text.strip() == section:  # Match the section
                    for row in table.find_all("tr"):
                        info_type_cell = row.find("td", class_="ttl")
                        info_value_cell = row.find("td", class_="nfo")
                        if info_type_cell and info_value_cell:
                            info_type = info_type_cell.text.strip()
                            info_value = info_value_cell.text.strip()
                            section_data[info_type] = info_value
                    extracted_info[section] = section_data
                    break
            if section not in extracted_info:  # If section was not found
                extracted_info[section] = None  # Or use {} for an empty dict instead
        return extracted_info

    def read_json(self, source_file, file_path):
        if source_file == 'brand links':
            with open(file_path, 'r') as f:
                self.brand_links = json.load(f)
            print("Brand links read")

        elif source_file == 'phone models':
            with open(file_path, 'r') as f:
                self.phone_models_links = json.load(f)
            print("Phone models read")

        elif source_file == 'phone info':
            with open(file_path, 'r') as f:
                self.phone_info = json.load(f)
            print("Phone info read")

        else:
            print("Invalid source file")

    def write_json(self, source_file, dest_file):
        if source_file == 'brand links':
            with open(dest_file, 'w') as f:
                json.dump(self.brand_links, f, ensure_ascii=False, indent=4)
            print("Brand links written")

        elif source_file == 'phone models':
            with open(dest_file, 'w') as f:
                json.dump(self.phone_models_links, f, ensure_ascii=False, indent=4)
            print("Phone models written")

        elif source_file == 'phone info':
            with open(dest_file, 'w') as f:
                json.dump(self.phone_info, f, ensure_ascii=False, indent=4)
            print("Phone info written")

        else:
            print("Invalid source file")

    def write_json_each(self, file, data):
        with open(file, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_brand_links(self):
        return self.brand_links

    def get_phone_models_links(self):
        return self.phone_models_links

    def get_phone_info(self):
        return self.phone_info


"""def res(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    while True:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            break
        else:
            time.sleep(3)
    return res"""

"""class Crawl():

    def __init__(self):
        self.phone_links = list()
        self.brands = ['alcatel', 'Apple', 'Asus', 'BLU', 'HTC', 'Huawei', 'Infinix', 'Lenovo', 'LG', 'Nokia', 'Sony',
                       'Xiaomi', 'ZTE', 'Samsung']
        self.brands_link = list()
        self.url = 'https://www.gsmarena.com/'
        self.crawl_brands()
        self.phone_crawl()

    def create_csv_file(self, name, listofeverything):
        with open('./{}.csv'.format(name), '+a') as f:
            for line in listofeverything:
                f.write(line + '\n')

    def crawl_brands(self):
        response = res(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        soup = soup.find_all('ul')[2]
        soup = soup.find_all('li')

        for i in soup:
            if i.text in self.brands:
                print(i.text, 'Link crawled')
                self.brands_link.append(self.url + i.find('a')['href'])

        self.create_csv_file('brands_link', self.brands_link)

    def phone_crawl(self):
        for brand in self.brands_link:
            response = res(brand)
            soup = BeautifulSoup(response.content, 'html.parser')
            soup = soup.find('div', class_='makers')
            soup = soup.find_all('li')
            for i in soup:
                self.phone_links.append(self.url + i.find('a')['href'])

        self.create_csv_file('phone_links', self.phone_links)"""


def main():
    brands_to_select = ['alcatel', 'Apple', 'Asus', 'BLU', 'HTC', 'Huawei', 'Infinix', 'Lenovo', 'LG', 'Nokia', 'Sony',
                        'Xiaomi', 'ZTE', 'Samsung']
    interested_sections = ['Network', 'Launch', 'Body', 'Display', 'Platform', 'Memory', 'Main Camera', 'Selfie camera',
                           'Sound', 'Comms', 'Features', 'Battery', 'Misc']

    main_links = "https://www.gsmarena.com/makers.php3"
    data_extractor = DataExtractor(main_links)
    data_extractor.extract_brand_data()
    # data_extractor.write_json('brand links', 'brand_links.json')
    data_extractor.extract_phone_models(brands_to_select)
    # data_extractor.write_json('phone models', 'phone_models.json')
    data_extractor.extract_phone_info(interested_sections)
    # data_extractor.write_json('phone info', 'phone_info.json')


if __name__ == '__main__':
    main()
    print("Done")
