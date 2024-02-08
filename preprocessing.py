import pandas as pd
import re

data = pd.read_csv('flattened_data.csv')


class DataFrameProcessor:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def apply_transformations(self):
        self.extract_display_characteristics()
        self.extract_resolution_details()
        self.extract_base_os()
        self.extract_os_version()
        self.extract_chipset_manufacturer()
        self.extract_cpu_core_count()
        self.preprocess_memory_card_slot()
        self.expand_memory_configurations()
        self.convert_storage_ram()
        self.clean_and_extract_price()

    def extract_display_characteristics(self):
        self.dataframe['Display_Size_Inch'] = self.dataframe['Display_Size'].apply(
            lambda x: self._extract_with_regex(x, r'(\d+\.?\d*) inches')
        )
        self.dataframe['Display_Size_Cm'] = self.dataframe['Display_Size'].apply(
            lambda x: self._extract_with_regex(x, r'(\d+\.?\d*) cm2')
        )
        self.dataframe['Screen_To_Body_Ratio'] = self.dataframe['Display_Size'].apply(
            lambda x: self._extract_with_regex(x, r'(~\d+\.?\d*%)')
        )

    def extract_resolution_details(self):
        self.dataframe['Resolution_Pixels'] = self.dataframe['Display_Resolution'].apply(
            lambda x: self._extract_with_regex(x, r'(\d+ x \d+) pixels')
        )
        self.dataframe['Resolution_Ratio'] = self.dataframe['Display_Resolution'].apply(
            lambda x: self._extract_with_regex(x, r'(\d+:\d+) ratio')
        )
        self.dataframe['PPI_Density'] = self.dataframe['Display_Resolution'].apply(
            lambda x: self._extract_with_regex(x, r'(~?\d+) ppi')
        )

    def extract_base_os(self):

        self.dataframe['base_os'] = self.dataframe['Platform_OS'].apply(
            lambda x: self._extract_os_from_first_space(x)
        )

    def _extract_os_from_first_space(self, os_string):

        return os_string.split(' ', 1)[0] if isinstance(os_string, str) else os_string

    def extract_os_version(self):

        self.dataframe['OS_Version'] = self.dataframe['Platform_OS'].apply(
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
        self.dataframe['Chipset_Manufacturer'] = self.dataframe['Platform_Chipset'].apply(
            lambda x: next((manufacturer for manufacturer in manufacturers if manufacturer in str(x)), "Other")
        )

    def extract_cpu_core_count(self):
        self.dataframe['CPU_Core_Count'] = self.dataframe['Platform_CPU'].apply(
            lambda x: self._extract_with_regex(x, r'(Dual|Quad|Hexa|Octa|Deca)-core')
        )

    def preprocess_memory_card_slot(self):

        self.dataframe['Card_Slot_Type'] = self.dataframe['Memory_Card slot'].apply(self._preprocess_memory_card_slot_value)

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

    def expand_memory_configurations(self, column_name='Memory_Internal'):
        # Temporary container for the new rows
        temp_df_list = []

        for _, row in self.dataframe.iterrows():
            configs = str(row[column_name]).split(', ') if pd.notnull(row[column_name]) else [None]
            for config in configs:
                new_row = row.copy()
                new_row[column_name] = config
                temp_df_list.append(new_row)

        self.dataframe = pd.DataFrame(temp_df_list).reset_index(drop=True)

    def convert_storage_ram(self):
        # Convert storage and RAM sizes
        self.dataframe['Internal_Storage_GB'] = self.dataframe['Memory_Internal'].str.extract(r'(\d+)\s*GB',
                                                                                              expand=False).astype(
            float)
        storage_in_mb = self.dataframe['Memory_Internal'].str.extract(r'(\d+)\s*MB', expand=False).astype(float) / 1024
        self.dataframe['Internal_Storage_GB'].fillna(storage_in_mb, inplace=True)

        self.dataframe['RAM_GB'] = self.dataframe['Memory_Internal'].str.extract(r'(\d+)\s*GB RAM',
                                                                                 expand=False).astype(float)
        ram_in_mb = self.dataframe['Memory_Internal'].str.extract(r'(\d+)\s*MB RAM', expand=False).astype(float) / 1024
        self.dataframe['RAM_GB'].fillna(ram_in_mb, inplace=True)

    def clean_and_extract_price(self):
        def clean_price(price):
            pattern = re.compile(r'([\$\€\£])?\s*(\d+(?:\.\d+)?)')
            matches = pattern.findall(str(price))
            if matches:
                currency_symbols = {'$': 'USD', '€': 'EUR', '£': 'GBP'}
                currency, amount = matches[0]
                currency = currency_symbols.get(currency, 'Unknown')
                amount = float(amount)
                return amount
            return 'Unknown', None
        self.dataframe['Cleaned_Price'] = pd.DataFrame(
            self.dataframe['Misc_Price'].apply(clean_price).tolist(), index=self.dataframe.index
        )

    def _extract_with_regex(self, text, pattern):
        if pd.isna(text):
            return None
        match = re.findall(pattern, str(text))
        return match[0] if match else None

    def drop_columns(self, columns_to_drop):

        self.dataframe.drop(columns=columns_to_drop, inplace=True, errors='ignore')


# Assuming data is your DataFrame loaded from 'flattened_data.csv'
processor = DataFrameProcessor(data)
processor.apply_transformations()
columns_to_drop = ['Display_Size', 'Display_Resolution', 'Platform_OS', 'Platform_Chipset', 'Platform_CPU','Platform_GPU', 'Memory_Internal', 'Memory_Card slot','Misc_Models','Misc_Price']
processor.drop_columns(columns_to_drop)
# To save the processed DataFrame:
processor.dataframe.to_csv('processed_data.csv', index=False)

