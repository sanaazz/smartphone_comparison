import numpy as np
import pandas as pd
import re


class DataPreProcess:
    def __init__(self, data_input):
        # If data_input is a string, assume it's a filename. Otherwise, assume it's a DataFrame.
        if isinstance(data_input, str):
            self.df = pd.read_csv(data_input, )
        else:
            self.df = data_input

      # Convert to string and remove leading "~"
    
    def process_main_camera_columns(self):
        camera_types = {
            'Main Camera_Single': 1,
            'Main Camera_Dual': 2,
            'Main Camera_Triple': 3,
            'Main Camera_Quad': 4,
            'Main Camera_Dual or Triple': 3,
            'Main Camera_Penta': 5,
            'Main Camera_Five': 5
        }
        for col, num in camera_types.items():
            self.df.loc[self.df[col].notnull(), 'Number of main cameras'] = num

    def process_selfie_camera_columns(self):
        camera_types = {
            'Selfie camera_Single': 1,
            'Selfie camera_Dual': 2,
            'Selfie camera_Triple': 3
        }
        for col, num in camera_types.items():
            self.df.loc[self.df[col].notnull(), 'Number of selfie cameras'] = num

    def get_highest_res(self, cell):
        cell = str(cell)
        if 'MP' in cell:
            cell = cell.split('MP')[0].strip()
        return cell

    def get_video_res(self, cell):
        cell = str(cell)
        if '@' in cell:
            cell = cell.split('@')[0].strip()
        return cell

    def get_features_list(self, cell):
        cell = str(cell)
        if ',' in cell:
            cell = cell.split(',')
        return cell

    def process_camera_resolutions(self):
        self.df['Highest_maincam_res'] = self.df['Main Camera_Single'].combine_first(
            self.df['Main Camera_Dual']).combine_first(self.df['Main Camera_Triple']).combine_first(
            self.df['Main Camera_Quad']).combine_first(self.df['Main Camera_Dual or Triple']).combine_first(
            self.df['Main Camera_Penta']).combine_first(self.df['Main Camera_Five'])
        self.df['Highest_maincam_res'] = self.df['Highest_maincam_res'].apply(self.get_highest_res)
        self.df['Highest_selfiecam_res'] = self.df['Selfie camera_Single'].combine_first(
            self.df['Selfie camera_Dual']).combine_first(self.df['Selfie camera_Triple'])
        self.df['Highest_selfiecam_res'] = self.df['Highest_selfiecam_res'].apply(self.get_highest_res)

    def process_video_resolution(self):
        self.df['Main Camera_Video'] = self.df['Main Camera_Video'].apply(self.get_video_res)
        self.df['Selfie camera_Video'] = self.df['Selfie camera_Video'].apply(self.get_video_res)

    def camera_features_listing(self):
        self.df['Main Camera_Features'] = self.df['Main Camera_Features'].apply(self.get_features_list)
        self.df['Selfie camera_Features'] = self.df['Selfie camera_Features'].apply(self.get_features_list)

    def demintions_process(self):
        length = []
        width = []
        height = []
        volume = []
        for x in list(self.df['Body_Dimensions']):
            try:
                m = re.findall('(\d+(?:\.\d+)?)', x)
                length.append(float(m[0]))
            except:
                length.append(np.nan)
            try:
                m = re.findall('(\d+(?:\.\d+)?)', x)
                width.append(float(m[1]))
            except:
                width.append(np.nan)
            try:
                m = re.findall('(\d+(?:\.\d+)?)', x)
                height.append(float(m[2]))
            except:
                height.append(np.nan)
            try:
                m = re.findall('(\d+(?:\.\d+)?)', x)
                volume.append(float(m[0]) * float(m[1]) * float(m[2]))
            except:
                volume.append(np.nan)
        self.df['length'] = length
        self.df['width'] = width
        self.df['height'] = height
        self.df['volume'] = volume

    def weight_process(self):
        weight = []
        for x in list(self.df['Body_Weight']):
            try:
                m = re.findall('(\d+(?:\.\d+)?)', x)
                weight.append(float(m[0]))
            except:
                m = np.nan
                weight.append(m)
        self.df['weight'] = weight

    def network_tech_process(self):
        self.df['Network_2G bands'].fillna(0, inplace=True)
        self.df['Network_3G bands'].fillna(0, inplace=True)
        self.df['Network_4G bands'].fillna(0, inplace=True)
        self.df['Network_5G bands'].fillna(0, inplace=True)
        net_2g = []
        for x in list(self.df['Network_2G bands']):
            if x == 0:
                net_2g.append(0)
            else:
                net_2g.append(1)
        self.df['2G'] = net_2g
        net_3g = []
        for x in list(self.df['Network_3G bands']):
            if x == 0:
                net_3g.append(0)
            else:
                net_3g.append(1)
        self.df['3G'] = net_3g
        net_4g = []
        for x in list(self.df['Network_4G bands']):
            if x == 0:
                net_4g.append(0)
            else:
                net_4g.append(1)
        self.df['4G'] = net_4g
        net_5g = []
        for x in list(self.df['Network_5G bands']):
            if x == 0:
                net_5g.append(0)
            else:
                net_5g.append(1)
        self.df['5G'] = net_5g

    def battery_capacity_process(self):
        battery_capacity = []
        for x in list(self.df['Battery_Type']):
            try:
                m = re.findall('(\d+)', x)
                battery_capacity.append(int(m[0]))
            except:
                m = np.nan
                battery_capacity.append(m)
        self.df['Battery_capactiy'] = battery_capacity

    def sensors_process(self):
        sensors = []
        for x in list(self.df['Features_Sensors']):
            try:
                m = x.split(',')
                sensors.append(m)
            except:
                sensors.append(np.nan)
        self.df['Sensors'] = sensors

    def extract_display_characteristics(self):
        self.df['Display_Size_Inch'] = self.df['Display_Size'].apply(
            lambda x: self._extract_with_regex(x, r'(\d+\.?\d*) inches')
        )
        self.df['Display_Size_Cm'] = self.df['Display_Size'].apply(
            lambda x: self._extract_with_regex(x, r'(\d+\.?\d*) cm2')
        )
        self.df['Screen_To_Body_Ratio'] = self.df['Display_Size'].apply(
            lambda x: self._extract_with_regex(x, r'(~\d+\.?\d*%)')
        )
        def remove_tilde_percent(value):
            try:
                return float(str(value).replace("~", "").replace("%", ""))
            except:
                return (str(value).replace("~", "").replace("%", ""))
        self.df['Screen_To_Body_Ratio']= self.df['Screen_To_Body_Ratio'].apply(remove_tilde_percent)
        self.df['Screen_To_Body_Ratio'].value_counts()
    def SIM_process(self):
        type_sim = []
        count = []
        for x in list(self.df['Body_SIM']):
            try:
                x_lower = x.lower()
                nano = x_lower.find('nano')
                mini = x_lower.find('mini')
                micro = x_lower.find('micro')
                if nano > -1 :
                    type_sim.append('nano')
                elif micro > -1 :
                    type_sim.append('micro')
                elif mini > -1 :
                    type_sim.append('mini')
                else:
                    type_sim.append('unknown')
                dual = x_lower.find('dual')
                single = x_lower.find('single')
                if (single > -1) & (dual > -1):
                    count.append('both')
                elif dual > -1:
                    count.append('dual')
                else:
                    count.append('single')
            except:
                type_sim.append(np.nan)
                count.append(np.nan)
        self.df['SIM_type'] = type_sim
        self.df['SIM_count'] = count
    
    def extract_resolution_details(self):
        self.df['Resolution_Pixels'] = self.df['Display_Resolution'].apply(
            lambda x: self._extract_with_regex(x, r'(\d+ x \d+) pixels')
        )
        self.df['Resolution_Ratio'] = self.df['Display_Resolution'].apply(
            lambda x: self._extract_with_regex(x, r'(\d+:\d+) ratio')
        )
        self.df['PPI_Density'] = self.df['Display_Resolution'].apply(
            lambda x: self._extract_with_regex(x, r'(~?\d+) ppi')
        )
        def remove_tilde(value):
            return str(value).lstrip("~")
        self.df['PPI_Density'] = self.df['PPI_Density'].apply(remove_tilde)
        self.df['PPI_Density'].value_counts()

    def extract_base_os(self):

        self.df['base_os'] = self.df['Platform_OS'].apply(
            lambda x: self._extract_os_from_first_space(x)
        )

    def _extract_os_from_first_space(self, os_string):

        return os_string.split(' ', 1)[0] if isinstance(os_string, str) else os_string

    def extract_os_version(self):

        self.df['OS_Version'] = self.df['Platform_OS'].apply(
            lambda x: self._extract_version_number(x)
        )

    def _extract_version_number(self, os_string):

        if isinstance(os_string, str):
            # Adjusted regex pattern to capture only the numeric part before any spaces or additional text
            match = re.search(r'\b(?:Android|iOS|Windows)\b\s([\d]+)', os_string)
            if match:
                return match.group(1)  # Return only the numeric part of the version
        return "Unknown"

    def extract_chipset_manufacturer(self):
        manufacturers = ["Qualcomm", "Mediatek", "Apple", "Samsung", "Exynos", "Intel Atom"]
        self.df['Chipset_Manufacturer'] = self.df['Platform_Chipset'].apply(
            lambda x: next((manufacturer for manufacturer in manufacturers if manufacturer in str(x)), "Other")
        )

    def extract_cpu_core_count(self):
        self.df['CPU_Core_Count'] = self.df['Platform_CPU'].apply(
            lambda x: self._extract_with_regex(x, r'(Dual|Quad|Hexa|Octa|Deca)-core')
        )

    def preprocess_memory_card_slot(self):

        self.df['Card_Slot_Type'] = self.df['Memory_Card slot'].apply(self._preprocess_memory_card_slot_value)

    def _preprocess_memory_card_slot_value(self, value):

        if pd.isna(value):
            return None  # Handle missing or null values
        value_str = str(value).lower()  # Standardize the string for comparison

        # Define keywords that imply card slot support
        keywords = ['microsd', 'sd', 'mmc', 'minisd', 'nanomemory']

        # Check for explicit "no" mention
        if 'no' in value_str:
            return 'No'

        # Check and return the specific keyword found in the value
        for keyword in keywords:
            if keyword in value_str:
                return keyword.capitalize()  # Return the keyword with the first letter capitalized for consistency

        # If "yes" is mentioned but no specific type is identified
        if 'yes' in value_str:
            return 'Yes'

        # Return 'Unknown' if none of the conditions are met
        return 'Unknown'

    """def expand_memory_configurations(self, column_name='Memory_Internal'):
        # Temporary container for the new rows
        temp_df_list = []

        for _, row in self.df.iterrows():
            configs = str(row[column_name]).split(', ') if pd.notnull(row[column_name]) else [None]
            for config in configs:
                new_row = row.copy()
                new_row[column_name] = config
                temp_df_list.append(new_row)

        self.df = pd.DataFrame(temp_df_list).reset_index(drop=True)

    def convert_storage_ram(self):
        # Convert storage and RAM sizes
        self.df['Internal_Storage_GB'] = self.df['Memory_Internal'].str.extract(r'(\d+)\s*GB',
                                                                                expand=False).astype(
            float)
        storage_in_mb = self.df['Memory_Internal'].str.extract(r'(\d+)\s*MB', expand=False).astype(float) / 1024
        self.df['Internal_Storage_GB'].fillna(storage_in_mb, inplace=True)

        self.df['RAM_GB'] = self.df['Memory_Internal'].str.extract(r'(\d+)\s*GB RAM',
                                                                   expand=False).astype(float)
        ram_in_mb = self.df['Memory_Internal'].str.extract(r'(\d+)\s*MB RAM', expand=False).astype(float) / 1024
        self.df['RAM_GB'].fillna(ram_in_mb, inplace=True)
"""

    def process_memory_data(self):
        # Example of calling the function with a memory data string
        self.df['Possible_Storages_Split'], self.df['Possible_RAMs_Split'] = \
            zip(*self.df['Memory_Internal'].apply(lambda x: self.extract_storage_and_ram_split_values(x)))

    def extract_storage_and_ram_split_values(self, memory_str):
        if pd.isna(memory_str):
            return [], []  # Return empty lists if the value is NaN

        unique_storages = set()
        unique_rams = set()

        # Split the string to handle multiple configurations
        split_memory_str = re.split(r'/|,| or ', memory_str)

        for part in split_memory_str:
            # Look for storage size patterns, ignoring details in parentheses
            storage_match = re.search(r'(\d+GB|\d+MB)(?=\s|\(|$)', part)
            ram_match = re.findall(r'(\d+GB|\d+MB) RAM', part)

            if storage_match:
                unique_storages.add(storage_match.group(1))
            if ram_match:
                unique_rams.update([ram.replace(' RAM', '') for ram in ram_match])

        return list(unique_storages), list(unique_rams)
    # Apply the adjusted function to each row in the DataFrame
        #self.df['Possible_Storages_Split'], self.df['Possible_RAMs_Split'] = zip(*self.df['Memory_Internal'].apply(extract_storage_and_ram_split_values))

    def clean_and_extract_price(self):
        def clean_price(price):
            if pd.isna(price):
                return None, None, None, None, None  # Return None for all currencies if the price string is NaN

                # Define regular expressions for EUR, USD, GBP, and INR prices, including optional prefixes like "About"
            regex_patterns = {
                'EUR': r'(?:About\s)?\€\s*(\d{1,3}(?:,\d{3})*\.?\d*)|(?:About\s)?(\d{1,3}(?:,\d{3})*\.?\d*)\s*EUR',
                'USD': r'(?:About\s)?\$\s*(\d{1,3}(?:,\d{3})*\.?\d*)',
                'GBP': r'(?:About\s)?£\s*(\d{1,3}(?:,\d{3})*\.?\d*)',
                'INR': r'(?:About\s)?₹\s*(\d{1,3}(?:,\d{3})*\.?\d*)|(?:About\s)?(\d{1,3}(?:,\d{3})*\.?\d*)\s*INR'
            }

            # Initialize variables to store extracted prices
            price_eur, price_usd, price_gbp, price_inr, price_other = None, None, None, None, None

            # Attempt to extract EUR, USD, GBP, and INR prices
            for currency, pattern in regex_patterns.items():
                match = re.search(pattern, price)
                if match:
                    # Remove commas from the matched price and convert to float
                    price = match.group(1) or match.group(2)  # Group 2 is for EUR pattern with "About"
                    if price:
                        price = price.replace(',', '')
                        if currency == 'EUR':
                            price_eur = float(price)
                        elif currency == 'USD':
                            price_usd = float(price)
                        elif currency == 'GBP':
                            price_gbp = float(price)
                        elif currency == 'INR':
                            price_inr = float(price)

            # If none of the specific currencies were found, attempt to extract any numeric value as 'other'
            if not any([price_eur, price_usd, price_gbp, price_inr]):
                match = re.search(r'(\d{1,3}(?:,\d{3})*\.?\d*)', price)
                if match:
                    price_other = float(match.group(1).replace(',', ''))

            return price_eur, price_usd, price_gbp, price_inr, price_other
            # matches = pattern.findall(str(price))
            # if matches:
            #    currency_symbols = {'$': 'USD', '€': 'EUR', '£': 'GBP', '₹': 'INR'}
            #    currency, amount = matches[0]
            #    amount = float(amount)
            #    return amount
            #return None


        #self.df['Cleaned_Price'] = pd.DataFrame(
        #    self.df['Misc_Price'].apply(clean_price).tolist(), index=self.df.index
        #)
        # Apply the updated function to extract prices
        extracted_prices = self.df['Misc_Price'].apply(lambda x: clean_price(x))
        # Create separate columns for each currency's price
        self.df['Price_EUR'], self.df['Price_USD'], self.df['Price_GBP'], self.df['Price_INR'], self.df['Price_Other'] = zip(*extracted_prices)
        usd_to_eur_rate = 0.93
        inr_to_eur_rate = 0.011
        gbp_to_eur_rate = 1.17
        for index, row in self.df.iterrows():
            if pd.isna(row['Price_EUR']):  # Check if Price_EUR is NaN
                if not pd.isna(row['Price_USD']):
                    # Convert USD to EUR and update
                    self.df.at[index, 'Price_EUR'] = row['Price_USD'] * usd_to_eur_rate
                elif not pd.isna(row['Price_GBP']):
                # Convert INR to EUR and update
                     self.df.at[index, 'Price_EUR'] = row['Price_INR'] * gbp_to_eur_rate
                elif not pd.isna(row['Price_INR']):
                    # Convert INR to EUR and update
                    self.df.at[index, 'Price_EUR'] = row['Price_INR'] * inr_to_eur_rate

    def _extract_with_regex(self, text, pattern):
        if pd.isna(text):
            return None
        match = re.findall(pattern, str(text))
        return match[0] if match else None

    def drop_old_columns(self):
        self.df = self.df.drop(
            columns=[
                    'Network_','Network_Speed','Display_Type','Memory_','Main Camera_Features', 
                    'Main Camera_Video', 'Selfie camera_Video',
                    'Sound_Loudspeaker', 'Sound_3.5mm jack', 'Comms_WLAN',
                    'Comms_Bluetooth', 'Comms_Positioning', 'Comms_NFC', 'Comms_Radio',
                    'Comms_USB', 'Misc_Colors',
                    "Main Camera_Single", "Main Camera_Dual", "Main Camera_Triple", "Main Camera_Quad",
                     "Main Camera_Dual or Triple", "Main Camera_Penta", "Main Camera_Five", "Selfie camera_Single",
                     "Selfie camera_Dual", "Selfie camera_Triple", "Selfie camera_", "Main Camera", "Selfie camera",
                     "Main Camera_",
                     'Display_Size', 'Display_Resolution', 'Platform_OS', 'Platform_Chipset', 'Platform_CPU',
                     'Platform_GPU',
                     'Memory_Internal', 'Memory_Card slot', 'Misc_Models', 'Misc_Price',
                     'Body_Dimensions', 'Body_Weight', 'Network_2G bands', 'Network_3G bands', 'Network_4G bands',
                     'Network_5G bands', 'Battery_Type', 'Features_Sensors',
                     'Body_Build', 'Selfie camera_Features', 'Display_Protection',
                     'Battery_Charging', 'Display_', 'Misc_SAR', 'Network_GPRS',
                     'Network_EDGE', 'Body_', 'Comms_Infrared port',
                     'Battery_Stand-by', 'Battery_Talk time', 'Features_', 'Sound_',
                     'Battery_Music play', 'Platform', 'Memory_Phonebook', 'Memory_Call records',
                     'Features_Messaging', 'Features_Games', 'Features_Java', 'Misc_SAR EU', 'Body_Keyboard',
                     'Features_Browser', 'Sound_Alert types', 'Features_Clock', 'Features_Alarm', 'Features_Languages','Price_USD',
                     'Price_GBP', 'Price_INR', 'Price_Other'])

    def drop_columns(self, columns_to_drop):

        self.df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

    def save_processed_data(self, file_name='processed_data.csv'):
        # Save the processed DataFrame to a CSV file
        self.df.to_csv(file_name, index=False)
    def final_adjustments(self):
        self.df['Launch_Announced'] = self.df['Launch_Announced'].replace('Not announced yet', np.nan)
        self.df['year'] = self.df['Launch_Announced'].str.extract(r'(\d{4})')
        self.df = self.df[self.df['year'].astype(float) > 2010]
        self.df['Resolution_Pixels'] = self.df['Resolution_Pixels'].fillna('0 x 0')
        self.df['Resolution_Pixels'] = self.df['Resolution_Pixels'].astype(str)
        self.df['Resolution_Pixels'] = self.df['Resolution_Pixels'].apply(lambda x: int(x.split(' x ')[0]) * int(x.split(' x ')[1]) if x != 'nan' else np.nan)
        self.df['Screen_To_Body_Ratio'] = pd.to_numeric(self.df['Screen_To_Body_Ratio'], errors='coerce')
        self.df['PPI_Density']=pd.to_numeric(self.df['PPI_Density'], errors='coerce')
        
    def year_to_int(self):
        int_year = []
        for x in list(self.df['year']):
            m = int(x)
            int_year.append(m)
        self.df['year'] = int_year

    def process(self):
        self.process_main_camera_columns()
        self.process_selfie_camera_columns()
        self.process_camera_resolutions()
        self.process_video_resolution()
        self.camera_features_listing()
        self.weight_process()
        self.demintions_process()
        self.network_tech_process()
        self.battery_capacity_process()
        self.sensors_process()
        self.SIM_process()
        self.extract_display_characteristics()
        self.extract_resolution_details()
        self.extract_base_os()
        self.extract_os_version()
        self.extract_chipset_manufacturer()
        self.extract_cpu_core_count()
        self.preprocess_memory_card_slot()
        """self.expand_memory_configurations()
        self.convert_storage_ram()"""
        self.process_memory_data()
        self.clean_and_extract_price()
        self.drop_old_columns()
        self.final_adjustments()
        self.year_to_int()
        return self.df


data_processor = DataPreProcess('flattened_data.csv')
data_processor.process()
data_processor.save_processed_data('processed_data.csv')
