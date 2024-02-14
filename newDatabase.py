from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, text,Null
from sqlalchemy.orm import relationship
from database_eng import *
import pandas as pd



Base = declarative_base()

class CreateTable:
    def __init__(self, database_name, username, password):
        engine = create_schema(username, password)
        with engine.connect() as conn:
            conn.execute(text(f"DROP DATABASE IF EXISTS {database_name}"))
            conn.execute(text(f"CREATE DATABASE {database_name}"))
        engine = create_table(username, password, database_name)
        with engine.connect() as conn:
            conn.execute(text(f"USE {database_name}"))
            Base.metadata.create_all(bind=conn)
 

#MAIN
class device_name(Base):
    __tablename__ = 'device_name'
    id = Column(Integer, primary_key=True,autoincrement=True)
    brand = Column(String(255))
    model = Column(String(255))
    
class g(Base):
    __tablename__ = 'g'
    id = Column(Integer, primary_key=True,autoincrement=True)
    n2g = Column(Integer)
    n3g = Column(Integer)
    n4g = Column(Integer)
    n5g = Column(Integer)
    
class technology(Base):
    __tablename__ = 'technology'
    id = Column(Integer, primary_key=True,autoincrement=True)
    technology = Column(String(255))
    
#MAIN
class Network_Technology(Base):
    __tablename__ = 'Network_Technology'
    id = Column(Integer, primary_key=True,autoincrement=True)
    technology_id = Column(Integer, ForeignKey('technology.id'))
    g_id = Column(Integer, ForeignKey('g.id'))
    
    

class Launch_Announced(Base):
    __tablename__ = 'Launch_Announced'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Launch_Announced = Column(String(255))
    
class Launch_Status(Base):
    __tablename__ = 'Launch_Status'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Launch_Status = Column(String(255))
    
#MAIN
class launch(Base):
    __tablename__ = 'launch'
    id = Column(Integer, primary_key=True,autoincrement=True)
    announced_id = Column(Integer, ForeignKey('Launch_Announced.id'))
    status_id = Column(Integer, ForeignKey('Launch_Status.id'))
    
    
class SIM_type(Base):
    __tablename__ = 'SIM_type'
    id = Column(Integer, primary_key=True,autoincrement=True)
    SIM_type = Column(String(10))
    
class SIM_count(Base):
    __tablename__ = 'SIM_count'
    id = Column(Integer, primary_key=True,autoincrement=True)
    SIM_count = Column(String(10))
    
#MAIN
class sim(Base):
    __tablename__ = 'sim'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Body_SIM = Column(String(255))
    count_id = Column(Integer, ForeignKey('SIM_count.id'))
    type_id = Column(Integer, ForeignKey('SIM_type.id'))


#MAIN
class camera(Base):
    __tablename__ = 'camera'
    id = Column(Integer, primary_key=True,autoincrement=True)
    main_cameras_num = Column(Integer)
    selfie_cameras_num = Column(Integer)
    Highest_maincam_res = Column(Integer)
    Highest_selfiecam_res = Column(Integer)
    
 
#MAIN   
# class body(Base):
#     __tablename__ = 'body'
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     weight = Column(Integer)
#     length = Column(Integer)
#     width = Column(Integer)
#     volume = Column(Integer)
    
#MAIN   
class battery(Base):
    __tablename__ = 'body'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Battery_capactiy = Column(Integer)

 
class Sensors(Base):
    __tablename__ = 'Sensors'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Sensors = Column(String(510))  

#MAIN   
class features(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Sensors_id = Column(Integer, ForeignKey('Sensors.id'))
    
    
    
#MAIN   
class display(Base):
    __tablename__ = 'display'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Display_Size_Inch = Column(Integer)
    Display_Size_Cm = Column(Integer)
    Screen_To_Body_Ratio = Column(Integer)
    Resolution_Pixels = Column(Integer)
    Resolution_Ratio = Column(Integer)
    PPI_Density = Column(Integer)
    
    
    
class version(Base):
    __tablename__ = 'version'
    id = Column(Integer, primary_key=True,autoincrement=True)
    OS_Version = Column(String(255)) 
    
class os_name(Base):
    __tablename__ = 'os_name'
    id = Column(Integer, primary_key=True,autoincrement=True)
    os_name = Column(String(255))  

#MAIN  
class os(Base):
    __tablename__ = 'os'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name_id = Column(Integer, ForeignKey('os_name.id'))
    version_id = Column(Integer, ForeignKey('SIM_type.id'))
    
class chipset(Base):
    __tablename__ = 'chipset'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Chipset_Manufacturer = Column(String(255))  
    
class cpu(Base):
    __tablename__ = 'cpu'
    id = Column(Integer, primary_key=True,autoincrement=True)
    CPU_Core_Count = Column(String(255))  
    
class ram(Base):
    __tablename__ = 'ram'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Storage = Column(String(255))  
    RAM = Column(String(255))  
    
#MAIN  
class platform(Base):
    __tablename__ = 'platform'
    id = Column(Integer, primary_key=True,autoincrement=True)
    chipset_id = Column(Integer, ForeignKey('os_name.id'))
    CPU_id = Column(Integer, ForeignKey('cpu.id'))
    Ram_id = Column(Integer, ForeignKey('ram.id'))
    
    
class Device(Base):
    __tablename__ = 'Device'
    id = Column(Integer, primary_key=True,autoincrement=True)
    device_name_id = Column(Integer, ForeignKey('device_name.id'))
    Network_Technology_id = Column(Integer, ForeignKey('Network_Technology.id'))
    launch_id = Column(Integer, ForeignKey('launch.id'))
    camera_id = Column(Integer, ForeignKey('camera.id'))
    body_id = Column(Integer, ForeignKey('body.id'))
    battery_id = Column(Integer, ForeignKey('battery.id'))
    features_id = Column(Integer, ForeignKey('features.id'))
    display_id = Column(Integer, ForeignKey('display.id'))
    os_id = Column(Integer, ForeignKey('os.id'))
    platform_id = Column(Integer, ForeignKey('platform.id'))
    sim_id = Column(Integer, ForeignKey('sim.id'))
    price = Column(String(255))  
    year = Column(String(255))  
    
    
    
    
    

    
    
    



    
class AddToTable:
    def __init__(self):
        self.connection = create_table('root', '361375Ff@', 'GSM')


        
    def addDeviceName(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        device_name = csvDevice[['brand','model']]
        device_name = pd.DataFrame(device_name.drop_duplicates().to_records(index=False))
        device_name.to_sql('device_name', con=self.connection, if_exists='append', index=False)
        
    def addg(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        g = csvDevice[['2G','3G','4G','5G']]
        g = g.rename(columns={'2G': 'n2g', '3G': 'n3g','4G': 'n4g', '5G': 'n5g'})
        g = pd.DataFrame(g.drop_duplicates().to_records(index=False))
        g.to_sql('g', con=self.connection, if_exists='append', index=False)
        
    def addTechnology(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        Network_Technology = csvDevice[['Network_Technology']]
        Network_Technology = Network_Technology.rename(columns={'Network_Technology': 'technology'})
        Network_Technology = pd.DataFrame(Network_Technology.drop_duplicates().to_records(index=False))
        Network_Technology.to_sql('technology', con=self.connection, if_exists='append', index=False)
        
        
        
    # def addNetwork_Technology(self):
    #     csvDevice = pd.read_csv('./processed_data.csv')
    #     csvg = csvDevice[['2G','3G','4G','5G']]
    #     csvg = csvg.rename(columns={'2G': 'n2g','3G': 'n3g','4G': 'n4g','5G': 'n5g',})
    #     csvtechnology = csvDevice[['Network_Technology']]
        
    #     g_data = pd.DataFrame(columns=['g_id'])
    #     technology_data = pd.DataFrame(columns=['Network_Technology'])
        
    #     g_mapping = pd.read_sql('SELECT * FROM g', con=self.connection)
    #     g_mapping['data'] = g_mapping.apply(lambda row: list(map(str, row[['n2g', 'n3g', 'n4g', 'n5g']])), axis=1)
    #     technology_mapping = pd.read_sql('SELECT * FROM technology', con=self.connection)
    #     for index, row in csvg.iterrows():
    #         g_name = row.values[0]
    #         g_id = g_mapping[g_mapping['data'] == g_name]['id'] 
    #         g_data.loc[len(g_data)] = g_id
                    
    #     for index, row in csvtechnology.iterrows():
    #         technology_name = row.values[0]
    #         technology_id = technology_mapping[technology_mapping['technology'] == technology_name]['id'].values[0]       
    #         technology_data.loc[len(technology_data)] = technology_id


    #     print(g_data)
    #     # print(technology_data)
    #     # new_data.to_sql('body_sim', con=self.connection, if_exists='append', index=False)
    
    
    def addLaunch_Announced(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        Launch_Announced = csvDevice[['Launch_Announced']]
        Launch_Announced = pd.DataFrame(Launch_Announced.drop_duplicates().to_records(index=False))
        Launch_Announced.to_sql('Launch_Announced', con=self.connection, if_exists='append', index=False)
     
    def addLaunch_Status(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        Launch_Status = csvDevice[['Launch_Status']]
        Launch_Status = pd.DataFrame(Launch_Status.drop_duplicates().to_records(index=False))
        Launch_Status.to_sql('Launch_Status', con=self.connection, if_exists='append', index=False)
        
    def addSIM_type(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        SIM_type = csvDevice[['SIM_type']]
        SIM_type = pd.DataFrame(SIM_type.drop_duplicates().to_records(index=False))
        SIM_type.to_sql('SIM_type', con=self.connection, if_exists='append', index=False)
        
    def addSIM_count(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        SIM_count = csvDevice[['SIM_count']]
        SIM_count = pd.DataFrame(SIM_count.drop_duplicates().to_records(index=False))
        SIM_count.to_sql('SIM_count', con=self.connection, if_exists='append', index=False)
        
    def addSensors(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        Sensors = csvDevice[['Sensors']]
        Sensors = pd.DataFrame(Sensors.drop_duplicates().to_records(index=False))
        Sensors.to_sql('Sensors', con=self.connection, if_exists='append', index=False)

    def addVersion(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        OS_Version = csvDevice[['OS_Version']]
        OS_Version = pd.DataFrame(OS_Version.drop_duplicates().to_records(index=False))
        OS_Version.to_sql('version', con=self.connection, if_exists='append', index=False)
        
    def addos_name(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        os_name = csvDevice[['base_os']]
        os_name = os_name.rename(columns={'base_os': 'os_name'})
        os_name = os_name[['os_name']]
        os_name = pd.DataFrame(os_name.drop_duplicates().to_records(index=False))
        os_name.to_sql('os_name', con=self.connection, if_exists='append', index=False)
        
    def addChipset(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        Chipset_Manufacturer = csvDevice[['Chipset_Manufacturer']]
        Chipset_Manufacturer = pd.DataFrame(Chipset_Manufacturer.drop_duplicates().to_records(index=False))
        Chipset_Manufacturer.to_sql('chipset', con=self.connection, if_exists='append', index=False)
        
    def addCpu(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        CPU_Core_Count = csvDevice[['CPU_Core_Count']]
        CPU_Core_Count = pd.DataFrame(CPU_Core_Count.drop_duplicates().to_records(index=False))
        CPU_Core_Count.to_sql('cpu', con=self.connection, if_exists='append', index=False)
        
    def addRam(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        ram = csvDevice[['Storage','RAM']]
        ram = pd.DataFrame(ram.drop_duplicates().to_records(index=False))
        ram.to_sql('ram', con=self.connection, if_exists='append', index=False)
        
    # def addBody_sim(self):
    #     csvDevice = pd.read_csv('./processed_data.csv')
    #     csvDevice = csvDevice[['Body_SIM']]
    #     new_data = pd.DataFrame(columns=['sim_id'])

    #     sim_mapping = pd.read_sql('SELECT * FROM sim', con=self.connection)

    #     for index, row in csvDevice.iterrows():
    #         sim_name = row['Body_SIM']
    #         try:
    #             sim_id = sim_mapping[sim_mapping['Body_SIM'] == sim_name]['id'].values[0]        
    #             new_data.loc[len(new_data)] = sim_id
    #         except:
    #             new_data.loc[len(new_data)] = Null

    #     new_data.to_sql('body_sim', con=self.connection, if_exists='append', index=False)
        


        
    def addAll(self):
        self.addDeviceName()
        self.addg()
        self.addTechnology()
        # self.addNetwork_Technology()
        self.addLaunch_Announced()
        self.addLaunch_Status()
        # self.addLaunch()
        self.addSIM_type()
        self.addSIM_count()
        # self.addsim()
        # self.addcamera()
        # self.addbody()
        # self.addbattery()
        self.addSensors()
        # self.addFeatures()
        # self.addDisplay()
        self.addVersion()
        self.addos_name()
        # self.addOs()
        self.addChipset()
        self.addCpu()
        self.addRam()
        # self.addPlatform()
        # self.addDevice()




if __name__ == '__main__':
    creator = CreateTable('GSM', 'root', '############')
    add = AddToTable()
    add.addAll()


