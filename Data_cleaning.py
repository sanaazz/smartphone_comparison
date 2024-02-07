import numpy as np
import pandas as pd

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

    def process(self):
        self.process_main_camera_columns()
        self.process_selfie_camera_columns()
        self.process_camera_resolutions()
        self.process_video_resolution()
        self.camera_features_listing()
        self.drop_old_columns()
        return self.df

processor = CameraDataProcessor('flattened_data.csv')
df = processor.process()
