import numpy as np
import pandas as pd
import re

class CameraDataProcessor:
    def __init__(self, file_name):
        self.df = pd.read_csv(file_name)


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
        self.df['Highest_maincam_res'] = self.df['Main Camera_Single'].combine_first(self.df['Main Camera_Dual']).combine_first(self.df['Main Camera_Triple']).combine_first(self.df['Main Camera_Quad']).combine_first(self.df['Main Camera_Dual or Triple']).combine_first(self.df['Main Camera_Penta']).combine_first(self.df['Main Camera_Five'])
        self.df['Highest_maincam_res'] = self.df['Highest_maincam_res'].apply(self.get_highest_res)
        self.df['Highest_selfiecam_res'] = self.df['Selfie camera_Single'].combine_first(self.df['Selfie camera_Dual']).combine_first(self.df['Selfie camera_Triple'])
        self.df['Highest_selfiecam_res'] = self.df['Highest_selfiecam_res'].apply(self.get_highest_res)
        
    def process_video_resolution(self):
        self.df['Main Camera_Video'] = self.df['Main Camera_Video'].apply(self.get_video_res)
        self.df['Selfie camera_Video'] = self.df['Selfie camera_Video'].apply(self.get_video_res)
        
    def camera_features_listing(self):
        self.df['Main Camera_Features'] = self.df['Main Camera_Features'].apply(self.get_features_list)
        self.df['Selfie camera_Features'] = self.df['Selfie camera_Features'].apply(self.get_features_list)
        

    def drop_old_columns(self):
        self.df = self.df.drop(columns=["Main Camera_Single","Main Camera_Dual","Main Camera_Triple","Main Camera_Quad","Main Camera_Dual or Triple","Main Camera_Penta","Main Camera_Five", "Selfie camera_Single", "Selfie camera_Dual", "Selfie camera_Triple", "Selfie camera_", "Main Camera", "Selfie camera", "Main Camera_"])
    def demintions_process(self):    
        length = []
        width = []
        height = []
        volume = []
        for x in list(df['Body_Dimensions']):
            try:
                m = re.findall('(\d+(?:\.\d+)?)' , x)
                length.append(float(m[0]))
            except:
                length.append(np.nan)
            try:
                m = re.findall('(\d+(?:\.\d+)?)' , x)
                width.append(float(m[1]))
            except:
                width.append(np.nan)
            try:
                m = re.findall('(\d+(?:\.\d+)?)' , x)
                height.append(float(m[2]))
            except:
                height.append(np.nan)
            try:
                m = re.findall('(\d+(?:\.\d+)?)' , x)
                volume.append(float(m[0]) * float(m[1]) * float(m[2]))
            except:
                volume.append(np.nan)
        self.df['length'] = length
        self.df['width'] = width
        self.df['height'] = height
        self.df['volume'] = volume

    def weight_process(self):
        weight = []
        for x in list(df['Body_Weight']):
            try:
                m = re.findall('(\d+(?:\.\d+)?)' , x)
                weight.append(float(m[0]))
            except:
                m = np.nan
                weight.append(m)
        df['weight'] = weight
    
    def network_tech_process(self):
        df['Network_2G bands'].fillna(0 , inplace=True)
        df['Network_3G bands'].fillna(0 , inplace=True)
        df['Network_4G bands'].fillna(0 , inplace=True)
        df['Network_5G bands'].fillna(0 , inplace=True)
        net_2g = []
        for x in list(df['Network_2G bands']):
            if x == 0 :
                net_2g.append(0)
            else:
                net_2g.append(1)
        self.df['2G'] = net_2g
        net_3g = []
        for x in list(df['Network_3G bands']):
            if x == 0 :
                net_3g.append(0)
            else:
                net_3g.append(1)
        self.df['3G'] = net_3g
        net_4g = []
        for x in list(df['Network_4G bands']):
            if x == 0 :
                net_4g.append(0)
            else:
                net_4g.append(1)
        self.df['4G'] = net_4g
        net_5g = []
        for x in list(df['Network_5G bands']):
            if x == 0 :
                net_5g.append(0)
            else:
                net_5g.append(1)
        self.df['5G'] = net_5g

    def battery_capacity_process(self):
        battery_capacity = []
        for x in list(df['Battery_Type']):
            try:
                m = re.findall('(\d+)' , x)
                battery_capacity.append(int(m[0]))
            except:
                m = np.nan
                battery_capacity.append(m)
        self.df['Battery_capactiy'] = battery_capacity

    def sensors_process(self):
        sensors = []
        for x in list(df['Features_Sensors']):
            try:
                m = x.split(',')
                sensors.append(m)
            except:
                sensors.append(np.nan)
        self.df['Sensors'] = sensors

    def process(self):
        self.process_main_camera_columns()
        self.process_selfie_camera_columns()
        self.process_camera_resolutions()
        self.process_video_resolution()
        self.camera_features_listing()
        self.drop_old_columns()
        self.weight_process()
        self.demintions_process()
        self.network_tech_process()
        self.battery_capacity_process()
        self.sensors_process()
        return self.df
    
    
   
processor = CameraDataProcessor('flattened_data.csv')
df = processor.process()
