from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, text,Null , Float
from sqlalchemy.orm import relationship
from database_eng import *
import pandas as pd
import time


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
    n2g_n3g_n4g_n5g = Column(String(5))
    
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
    Highest_maincam_res = Column(String(255))
    Highest_selfiecam_res = Column(String(255))
    
    
#MAIN   
class battery(Base):
    __tablename__ = 'battery'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Battery_capactiy = Column(Integer)

class Sensors(Base):
    __tablename__ = 'Sensors'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Sensors = Column(String(510))  

#MAIN   
class display(Base):
    __tablename__ = 'display'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Display_Size_Inch = Column(String(255))
    Display_Size_Cm = Column(String(255))
    Screen_To_Body_Ratio = Column(String(255))
    Resolution_Pixels = Column(String(255))
    Resolution_Ratio = Column(String(255))
    PPI_Density = Column(String(255))
    
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
    version_id = Column(Integer, ForeignKey('version.id'))
    
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
    Internal_Storage_GB = Column(String(255))  
    
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
    Network_Technology_id = Column(Integer)
    launch_id = Column(Integer, ForeignKey('launch.id'))
    camera_id = Column(Integer, ForeignKey('camera.id'))
    weight = Column(Float)
    length = Column(Float)
    width = Column(Float)
    height = Column(Float)
    volume = Column(Float)
    Battery_capactiy = Column(Integer)
    Display_Size_Inch = Column(String(255))
    Display_Size_Cm = Column(String(255))
    Screen_To_Body_Ratio = Column(String(255))
    Resolution_Pixels = Column(String(255))
    Resolution_Ratio = Column(String(255))
    PPI_Density = Column(String(255))
    Sensor_id = Column(Integer)
    os_id = Column(Integer,nullable=True)
    platform_id = Column(Integer)
    sim_id = Column(Integer)
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
        g = pd.DataFrame({'n2g_n3g_n4g_n5g': g.astype(str).agg(''.join, axis=1)})
        g = pd.DataFrame(g.drop_duplicates().to_records(index=False))
        g.to_sql('g', con=self.connection, if_exists='append', index=False)
        
    def addTechnology(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        Network_Technology = csvDevice[['Network_Technology']]
        Network_Technology = Network_Technology.rename(columns={'Network_Technology': 'technology'})
        Network_Technology = pd.DataFrame(Network_Technology.drop_duplicates().to_records(index=False))
        Network_Technology.to_sql('technology', con=self.connection, if_exists='append', index=False)
            
    def addNetwork_Technology(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        csvg = csvDevice[['2G','3G','4G','5G']]
        csvg = csvg.rename(columns={'2G': 'n2g', '3G': 'n3g','4G': 'n4g', '5G': 'n5g'})
        csvg = pd.DataFrame({'n2g_n3g_n4g_n5g': csvg.astype(str).agg(''.join, axis=1)})
        csvg = csvg.rename(columns={'2G': 'n2g','3G': 'n3g','4G': 'n4g','5G': 'n5g',})
        
        csvtechnology = csvDevice[['Network_Technology']]
        
        g_data = pd.DataFrame(columns=['g_id'])
        technology_data = pd.DataFrame(columns=['Network_Technology'])
        
        g_mapping = pd.read_sql('SELECT * FROM g', con=self.connection)
        technology_mapping = pd.read_sql('SELECT * FROM technology', con=self.connection)
        for index, row in csvg.iterrows():
            g_name = row.values[0]
            g_id = g_mapping[g_mapping['n2g_n3g_n4g_n5g'] == g_name]['id'].values
            g_data.loc[len(g_data)] = g_id
                    
        for index, row in csvtechnology.iterrows():
            technology_name = row.values[0]
            technology_id = technology_mapping[technology_mapping['technology'] == technology_name]['id'].values[0]       
            technology_data.loc[len(technology_data)] = technology_id

        result_df = pd.concat([g_data , technology_data], axis=1)
        result_df = result_df.rename(columns={'Network_Technology': 'technology_id'})
        result_df.to_sql('Network_Technology', con=self.connection, if_exists='append', index=False)
         
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

    def addLaunch(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        csvStatus = csvDevice[['Launch_Status']]
        csvAnnounced = csvDevice[['Launch_Announced']]
        Status_data = pd.DataFrame(columns=['Launch_Status'])
        Announced_data = pd.DataFrame(columns=['Launch_Announced'])
        
        Status_mapping = pd.read_sql('SELECT * FROM Launch_Status', con=self.connection)
        Announced_mapping = pd.read_sql('SELECT * FROM Launch_Announced', con=self.connection)
        
        for index, row in csvStatus.iterrows():
            status_name = row['Launch_Status']
            Status_id = Status_mapping[Status_mapping['Launch_Status'] == status_name]['id'].values[0]        
            Status_data.loc[len(Status_data)] = Status_id

        for index, row in csvAnnounced.iterrows():
            Announced_name = row['Launch_Announced']
            Announced_id = Announced_mapping[Announced_mapping['Launch_Announced'] == Announced_name]['id'].values[0]        
            Announced_data.loc[len(Announced_data)] = Announced_id


        result_df = pd.concat([Announced_data, Status_data], axis=1)
        result_df = result_df.rename(columns={'Launch_Announced': 'announced_id', 'Launch_Status': 'status_id'})
        result_df.to_sql('launch', con=self.connection, if_exists='append', index=False)

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

    def addSim(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        csvDevice = csvDevice.fillna(0)
        csvtype = csvDevice[['SIM_type']]
        csvbody = csvDevice[['Body_SIM']]
        csvcount = csvDevice[['SIM_count']]
        type_data = pd.DataFrame(columns=['SIM_type'])
        count_data = pd.DataFrame(columns=['SIM_count'])
        
        type_mapping = pd.read_sql('SELECT * FROM SIM_type', con=self.connection)
        count_mapping = pd.read_sql('SELECT * FROM SIM_count', con=self.connection)
        
        for index, row in csvtype.iterrows():
            type_name = row['SIM_type']
            try : 
                Status_id = type_mapping[type_mapping['SIM_type'] == type_name]['id'].values[0]      
                type_data.loc[len(type_data)] = Status_id
            except:
                type_data.loc[len(type_data)] = 4

        for index, row in csvcount.iterrows():
            count_name = row['SIM_count']
            try : 
                count_id = count_mapping[count_mapping['SIM_count'] == count_name]['id'].values[0]        
                count_data.loc[len(count_data)] = count_id
            except:
                count_data.loc[len(count_data)] = 3


        result_df = pd.concat([csvbody , count_data, type_data], axis=1)
        result_df = result_df.rename(columns={'SIM_count': 'count_id', 'SIM_type': 'type_id'})
        result_df.to_sql('sim', con=self.connection, if_exists='append', index=False)
        
    def addSensors(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        Sensors = csvDevice[['Sensors']]
        Sensors = pd.DataFrame(Sensors.drop_duplicates().to_records(index=False))
        Sensors.to_sql('Sensors', con=self.connection, if_exists='append', index=False)
        
    def addVersion(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        csvDevice = csvDevice.fillna(0)
        OS_Version = csvDevice[['OS_Version']]
        OS_Version = pd.DataFrame(OS_Version.drop_duplicates().to_records(index=False))
        OS_Version.to_sql('version', con=self.connection, if_exists='append', index=False)
        
    def addos_name(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        csvDevice = csvDevice.fillna(0)
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
        csvDevice['Storage'] = csvDevice['Storage'].astype(str) + ',' + csvDevice['RAM'].astype(str)
        RAM_GB = csvDevice[['Storage']]
        RAM_GB = RAM_GB.rename(columns={'Storage': 'Internal_Storage_GB'})
        RAM_GB = pd.DataFrame( RAM_GB.drop_duplicates().to_records(index=False))
        RAM_GB.to_sql('ram', con=self.connection, if_exists='append', index=False)
    
    def addBattery(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        Battery_capactiy = csvDevice[['Battery_capactiy']]
        Battery_capactiy = pd.DataFrame( Battery_capactiy.drop_duplicates().to_records(index=False))
        Battery_capactiy.to_sql('battery', con=self.connection, if_exists='append', index=False)
    
    def addcamera(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        csvDevice = csvDevice.rename(columns={'Number of main cameras' :'main_cameras_num'  , 'Number of selfie cameras' : 'selfie_cameras_num'})
        camera = csvDevice[['main_cameras_num' , 'selfie_cameras_num' , 'Highest_maincam_res' , 'Highest_selfiecam_res']]
        camera = pd.DataFrame( camera.drop_duplicates().to_records(index=False))
        # print(camera)
        camera.to_sql('camera', con=self.connection, if_exists='append', index=False)
    
    def addDisplay(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        display = csvDevice[['Display_Size_Inch',
       'Display_Size_Cm', 'Screen_To_Body_Ratio', 'Resolution_Pixels',
       'Resolution_Ratio', 'PPI_Density']]
        display = pd.DataFrame( display.drop_duplicates().to_records(index=False))
        display.to_sql('display', con=self.connection, if_exists='append', index=False)
    
    def addOs(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        csvDevice = csvDevice.fillna(0)
        name_mapping = pd.DataFrame(pd.read_sql('SELECT * FROM os_name', con=self.connection))
        version_mapping = pd.DataFrame(pd.read_sql('SELECT * FROM version', con=self.connection))
        name = []
        version = []
        for row in list(csvDevice['base_os']):
            if (row == 0):
                    name.append(5)
            for j in range(len(list(name_mapping['os_name']))):
                if (row == list(name_mapping['os_name'])[j]):
                    name.append(j + 1)
                
        for row in list(csvDevice['OS_Version']):
            for j in range(len(list(version_mapping['OS_Version']))):
                if (row == list(version_mapping['OS_Version'])[j]):
                    version.append(j + 1)
        df2 = pd.DataFrame()
        df2['version_id'] = version
        df2['name_id'] = name
        df2 = df2.drop_duplicates(subset=['version_id' , 'name_id'])
        os_tab = df2
        os_tab = df2[['name_id' , 'version_id']]
        os_tab = pd.DataFrame( os_tab.drop_duplicates().to_records(index=False))
        os_tab.to_sql('os', con=self.connection, if_exists='append', index=False)
    
    def addPlatform(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        csvDevice['Chipset_Manufacturer'] = csvDevice['Chipset_Manufacturer'].fillna(0)
        csvDevice['CPU_Core_Count'] = csvDevice['CPU_Core_Count'].fillna(0)
        csvDevice['Storage'] = csvDevice['Storage'].astype(str) + ',' + csvDevice['RAM'].astype(str)
        csvDevice = csvDevice.rename(columns={'Storage': 'Internal_Storage_GB'})
        
        csvDevice = csvDevice.drop_duplicates(['Chipset_Manufacturer' , 'CPU_Core_Count' , 'Internal_Storage_GB'])
        chip_mapping = pd.DataFrame(pd.read_sql('SELECT * FROM chipset', con=self.connection))
        cpu_mapping = pd.DataFrame(pd.read_sql('SELECT * FROM cpu', con=self.connection))
        ram_mapping = pd.DataFrame(pd.read_sql('SELECT * FROM ram', con=self.connection))
        chip = []
        cpu = []
        ram = []
        for row in list(csvDevice['Chipset_Manufacturer']):
            for j in range(len(list(chip_mapping['Chipset_Manufacturer']))):
                if (row == list(chip_mapping['Chipset_Manufacturer'])[j]):
                    chip.append(j + 1)
                
        for row in list(csvDevice['CPU_Core_Count']):
            if (row == 0):
                    cpu.append(5)
            for j in range(len(list(cpu_mapping['CPU_Core_Count']))):
                
                if (row == list(cpu_mapping['CPU_Core_Count'])[j]):
                    cpu.append(j + 1)
        
        for row in list(csvDevice['Internal_Storage_GB']):
            for j in range(len(list(ram_mapping['Internal_Storage_GB']))):
                if (row == list(ram_mapping['Internal_Storage_GB'])[j]):
                    ram.append(j + 1)

       
        df2 = pd.DataFrame()
        df2['chipset_id'] = chip
        df2['CPU_id'] = cpu
        df2['Ram_id'] = ram
        
        df2 = df2.drop_duplicates(subset=['chipset_id' , 'CPU_id' , 'Ram_id'])
        plat_tab = df2
        plat_tab = df2[['chipset_id' , 'CPU_id' , 'Ram_id']]
        plat_tab = pd.DataFrame( plat_tab.drop_duplicates().to_records(index=False))
        plat_tab.to_sql('platform', con=self.connection, if_exists='append', index=False)

    def addDevice(self):
        csvDevice = pd.read_csv('./processed_data.csv')
        csvDevice = csvDevice.rename(columns={'Number of main cameras' :'main_cameras_num'  , 'Number of selfie cameras' : 'selfie_cameras_num'})
        data = csvDevice[['Body_SIM','SIM_type','SIM_count','Sensors','Launch_Announced','Launch_Status','Network_Technology','2G','3G','4G','5G','brand','model','CPU_Core_Count','Storage','RAM','Chipset_Manufacturer','base_os','OS_Version','PPI_Density','Resolution_Ratio','Resolution_Pixels','Display_Size_Inch','Display_Size_Cm','Screen_To_Body_Ratio','main_cameras_num' , 'selfie_cameras_num' , 'Highest_maincam_res' , 'Highest_selfiecam_res','Price_EUR','length' , 'width' ,'height','Battery_capactiy', 'volume','year','weight' ]]
        data['Internal_Storage_GB'] = data['Storage'].astype(str) + ',' + data['RAM'].astype(str)
        data['n2g_n3g_n4g_n5g'] = data['2G'].astype(str) + '' + data['3G'].astype(str) + ''+data['4G'].astype(str) + ''+data['5G'].astype(str)
        data = data.rename(columns={'Price_EUR': 'price','base_os':'os_name'})
        data = pd.DataFrame(data.drop_duplicates().to_records(index=False))
        camera_mapping = pd.read_sql('SELECT * FROM camera', con=self.connection)
        camera_mapping = pd.read_sql('SELECT * FROM camera', con=self.connection)
        name_mapping = pd.read_sql('SELECT * FROM device_name', con=self.connection)
        os_mapping = pd.read_sql('SELECT os.id ,os_name.os_name,version.OS_Version  FROM os join os_name on os.name_id = os_name.id join version on os.version_id = version.id', con=self.connection)
        platform_mapping = pd.read_sql('select platform.id , cpu.CPU_Core_Count , ram.Internal_Storage_GB , chipset.Chipset_Manufacturer from platform join cpu on platform.CPU_id = cpu.id join chipset on chipset.id = platform.chipset_id join ram on ram.id = platform.ram_id', con=self.connection)
        net_mapping = pd.read_sql('select a.id ,technology,n2g_n3g_n4g_n5g from Network_Technology a join technology b on a.technology_id = b.id join g on a.g_id = g.id', con=self.connection)
        launch_mapping = pd.read_sql('select launch.id , Launch_Announced , Launch_Status from launch join Launch_Announced a on launch.announced_id = a.id join Launch_Status c on launch.status_id = c.id', con=self.connection)
        Sensors_mapping = pd.read_sql('select * from sensors', con=self.connection)
        sim_mapping = pd.read_sql('select sim.id,Body_SIM,SIM_count,SIM_type from sim join SIM_count on SIM_count.id = sim.id join SIM_type on SIM_type.id = sim.id', con=self.connection)

        data['sim_id'] = data[['Body_SIM','SIM_count','SIM_type']].apply(
            lambda row: sim_mapping[
        (sim_mapping['Body_SIM'] == row['Body_SIM']) &
        (sim_mapping['SIM_count'] == row['SIM_count']) &
        (sim_mapping['SIM_type'] == row['SIM_type'])]['id'].values ,axis=1)
        
        for i in range(len(data['sim_id'])) :
            try :
                data['sim_id'][i] = int(data['sim_id'][i][0])
            except:
                data['sim_id'][i] = 0
        
        
        data['Sensor_id'] = data[['Sensors']].apply(
            lambda row: Sensors_mapping[
        (Sensors_mapping['Sensors'] == row['Sensors'])]['id'].values ,axis=1)

        for i in range(len(data['Sensor_id'])) :
            try :
                data['Sensor_id'][i] = int(data['Sensor_id'][i][0])
            except:
                data['Sensor_id'][i] = 0

        data['launch_id'] = data[['Launch_Announced','Launch_Status']].apply(
            lambda row: launch_mapping[
        (launch_mapping['Launch_Announced'] == row['Launch_Announced']) &
        (launch_mapping['Launch_Status'] == row['Launch_Status'])]['id'].values ,axis=1)

        for i in range(len(data['launch_id'])) :
            try :
                data['launch_id'][i] = int(data['launch_id'][i][0])
            except:
                data['launch_id'][i] = 0

        data['Network_Technology_id'] = data[['Network_Technology','n2g_n3g_n4g_n5g']].apply(
            lambda row: name_mapping[
        (net_mapping['technology'] == row['Network_Technology']) &
        (net_mapping['n2g_n3g_n4g_n5g'] == row['n2g_n3g_n4g_n5g'])]['id'].values ,axis=1)


        for i in range(len(data['Network_Technology_id'])) :
            try :
                data['Network_Technology_id'][i] = int(data['Network_Technology_id'][i][0])
            except:
                data['Network_Technology_id'][i] = 0
                
                
        data['device_name_id'] = data[['brand','model']].apply(
            lambda row: name_mapping[
        (name_mapping['brand'] == row['brand']) &
        (name_mapping['model'] == row['model'])]['id'].values ,axis=1)

        
        for i in range(len(data['device_name_id'])) :
            print(data['device_name_id'][i])
            if len(data['device_name_id'][i]) == 1:
                data['device_name_id'][i] = int(data['device_name_id'][i][0])

        data['platform_id'] = data[['Internal_Storage_GB','CPU_Core_Count','Chipset_Manufacturer']].apply(
            lambda row: platform_mapping[
        (platform_mapping['Internal_Storage_GB'] == row['Internal_Storage_GB']) &
        (platform_mapping['CPU_Core_Count'] == row['CPU_Core_Count']) &
        (platform_mapping['Chipset_Manufacturer'] == row['Chipset_Manufacturer'])]['id'].values ,axis=1)
        
        for i in range(len(data['platform_id'])) :
            print(data['platform_id'][i])
            if len(data['platform_id'][i]) == 1:
                data['platform_id'][i] = int(data['platform_id'][i][0])
            else:
                data['platform_id'][i] = -1
                
        # print(data['platform_id'].value_counts)
        data['os_id'] = data[['os_name','OS_Version']].apply(
            lambda row: os_mapping[
        (os_mapping['os_name'] == row['os_name']) &
        (os_mapping['OS_Version'] == row['OS_Version'])]['id'].values ,axis=1)
        print(data['os_id'].value_counts())
        
        for i in range(len(data['os_id'])) :
            print(data['os_id'][i])
            if len(data['os_id'][i]) == 1:
                data['os_id'][i] = int(data['os_id'][i][0])
            else:
                data['os_id'][i] = -1


        data['camera_id'] = data[['main_cameras_num', 'selfie_cameras_num', 'Highest_maincam_res', 'Highest_selfiecam_res']].apply(
            lambda row: camera_mapping[
        (camera_mapping['main_cameras_num'] == row['main_cameras_num']) &
        (camera_mapping['selfie_cameras_num'] == row['selfie_cameras_num']) &
        (camera_mapping['Highest_maincam_res'] == row['Highest_maincam_res']) &
        (camera_mapping['Highest_selfiecam_res'] == row['Highest_selfiecam_res'])]['id'].values ,axis=1)
        
        
        data = data[['sim_id','Sensor_id','launch_id','Network_Technology_id','device_name_id','platform_id','os_id','PPI_Density','Resolution_Ratio','Resolution_Pixels','Display_Size_Inch','Display_Size_Cm','Screen_To_Body_Ratio','camera_id','Battery_capactiy','length' ,'weight', 'width' ,'height', 'volume','price','year']]
        for i in range(len(data['camera_id'])) :
            try :
                data['camera_id'][i] = int(data['camera_id'][i][0])
            except:
                data['camera_id'][i] = 17

        
        data.to_sql('Device', con=self.connection, if_exists='append', index=False)
        
        
          
          
          


    def addAll(self):
        self.addDeviceName()
        self.addg()
        self.addTechnology()
        self.addNetwork_Technology()
        self.addLaunch_Announced()
        self.addLaunch_Status()
        self.addLaunch()
        self.addSIM_type()
        self.addSIM_count()
        self.addSim()
        self.addcamera()
        self.addSensors()
        self.addDisplay()
        self.addVersion()
        self.addos_name()
        self.addOs()
        self.addChipset()
        self.addCpu()
        self.addRam()
        self.addBattery()
        self.addPlatform()
        self.addDevice()
        # self.addBody_sim()



if __name__ == '__main__':
    creator = CreateTable('GSM', 'root', '361375Ff@')
    add = AddToTable()
    add.addAll()

