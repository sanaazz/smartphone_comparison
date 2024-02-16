# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, ForeignKey, text,Null
# from sqlalchemy.orm import relationship
# from database_eng import *
# import pandas as pd


# Base = declarative_base()
# # session = Session(bind=engine)

# class CreateTable:
#     def __init__(self, database_name, username, password):
#         engine = create_schema(username, password)
#         with engine.connect() as conn:
#             conn.execute(text(f"DROP DATABASE IF EXISTS {database_name}"))
#             conn.execute(text(f"CREATE DATABASE {database_name}"))
#         engine = create_table(username, password, database_name)
#         with engine.connect() as conn:
#             conn.execute(text(f"USE {database_name}"))
#             Base.metadata.create_all(bind=conn)
 
# ###part 3
# class device_name(Base):
#     __tablename__ = 'device_name'
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     brand = Column(String(255))
#     model = Column(String(255))
    
# class internal(Base):
#     __tablename__ = 'internal'
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     Storage = Column(String(6))
#     RAM = Column(String(6))

# class chipset(Base):
#     __tablename__ = 'chipset'
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     Chipset_Manufacturer = Column(String(510))

# class card(Base):
#     __tablename__ = 'card'
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     Card_Slot_Type = Column(String(7))

# # class wlan(Base):
# #     __tablename__ = 'wlan'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     Comms_WLAN = Column(String(510))

# # class bluetooth(Base):
# #     __tablename__ = 'bluetooth'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     Comms_Bluetooth = Column(String(125))

# # class usb(Base):
# #     __tablename__ = 'usb'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     Comms_USB = Column(String(255))

# # class battery_capactiy(Base):
# #     __tablename__ = 'battery_capactiy'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     capactiy = Column(float)

# # class charge(Base):
# #     __tablename__ = 'charge'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     name = Column(String(255))

# # class color(Base):
# #     __tablename__ = 'color'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     name = Column(String(255))

# class technology(Base):
#     __tablename__ = 'technology'
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     Network_Technology = Column(String(255))

# # class n2g(Base):
# #     __tablename__ = 'n2g'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     name = Column(String(255))

# # class n3g(Base):
# #     __tablename__ = 'n3g'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     name = Column(String(255))

# # class n4g(Base):
# #     __tablename__ = 'n4g'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     name = Column(String(255))

# # class n5g(Base):
# #     __tablename__ = 'n5g'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     name = Column(String(255))

# # class speed(Base):
# #     __tablename__ = 'speed'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     name = Column(String(255))

# class sim(Base):
#     __tablename__ = 'sim'
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     Body_SIM = Column(String(255))

# # class protection(Base):
# #     __tablename__ = 'protection'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     name = Column(String(255))

# class os(Base):
#     __tablename__ = 'os'
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     Base_os = Column(String(255))

# # class charg(Base):
# #     __tablename__ = 'charg'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     name = Column(String(255))

# # ##part 2

# class network_technology(Base):
#     __tablename__ = 'network_technology'
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     tech_id = Column(Integer, ForeignKey('technology.id'))
#     technology = relationship('technology', back_populates='network_technology')
    
# # class network_2g(Base):
# #     __tablename__ = 'network_2g'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     n2g_id = Column(Integer, ForeignKey('n2g.id'), nullable=False)
# #     n2g = relationship('n2g', back_populates='network_2g')
    
# # class network_3g(Base):
# #     __tablename__ = 'network_3g'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     n3g_id = Column(Integer, ForeignKey('n3g.id'), nullable=False)
# #     n3g = relationship('n3g', back_populates='network_3g')
    
# # class network_4g(Base):
# #     __tablename__ = 'network_4g'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     n4g_id = Column(Integer, ForeignKey('n4g.id'), nullable=False)
# #     n4g = relationship('n4g', back_populates='network_4g')
    
# # class network_5g(Base):
# #     __tablename__ = 'network_5g'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     n5g_id = Column(Integer, ForeignKey('n5g.id'), nullable=False)
# #     n5g = relationship('n5g', back_populates='network_5g')
     
# # class network_speed(Base):
# #     __tablename__ = 'network_speed'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     speed_id = Column(Integer, ForeignKey('speed.id'), nullable=False)
# #     speed = relationship('speed', back_populates='network_speed')
     
# class body_sim(Base):
#     __tablename__ = 'body_sim'
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     sim_id = Column(Integer, ForeignKey('sim.id'))
#     sim = relationship('sim', back_populates='body_sim')
    
# # class display_protection(Base):
# #     __tablename__ = 'display_protection'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     protection_id = Column(Integer, ForeignKey('protection.id'), nullable=False)
# #     protection = relationship('protection', back_populates='display_protection')
    
# # class platform_os(Base):
# #     __tablename__ = 'platform_os'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     os_id = Column(Integer, ForeignKey('os.id'), nullable=False)
# #     os = relationship('os', back_populates='platform_os')
    
# # class platform_chipset(Base):
# #     __tablename__ = 'platform_chipset'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     chipset_id = Column(Integer, ForeignKey('chipset.id'), nullable=False)
# #     chipset = relationship('chipset', back_populates='platform_chipset')
       
# # class memory_card(Base):
# #     __tablename__ = 'memory_card'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     card_id = Column(Integer, ForeignKey('card.id'), nullable=False)
# #     card = relationship('card', back_populates='memory_card')
    
    
# # class memory_internal(Base):
# #     __tablename__ = 'memory_internal'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     internal_id = Column(Integer, ForeignKey('internal.id'), nullable=False)
# #     internal = relationship('internal', back_populates='memory_internal')
    
# # class comms_wlan(Base):
# #     __tablename__ = 'comms_wlan'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     wlan_id = Column(Integer, ForeignKey('wlan.id'), nullable=False)
# #     wlan = relationship('wlan', back_populates='comms_wlan')
      
# # class comms_blue(Base):
# #     __tablename__ = 'comms_blue'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     wlan_id = Column(Integer, ForeignKey('bluetooth.id'), nullable=False)
# #     bluetooth = relationship('bluetooth', back_populates='comms_blue')
       
# # class comms_usb(Base):
# #     __tablename__ = 'comms_usb'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     usb_id = Column(Integer, ForeignKey('usb.id'), nullable=False)
# #     bluetooth = relationship('bluetooth', back_populates='comms_usb')
    
# # class feature_sensors(Base):
# #     __tablename__ = 'feature_sensors'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     sensors = Column(String(255))
    
# # class battery_type(Base):
# #     __tablename__ = 'battery_type'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     type_id = Column(Integer, ForeignKey('type.id'), nullable=False)
# #     type = relationship('type', back_populates='battery_type')
    
    
# # class battery_charg(Base):
# #     __tablename__ = 'battery_charg'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     charg_id = Column(Integer, ForeignKey('charg.id'), nullable=False)
# #     charg = relationship('charg', back_populates='battery_charg')
    
    
# # class misc_color(Base):
# #     __tablename__ = 'misc_color'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     color_id = Column(Integer, ForeignKey('color.id'), nullable=False)
# #     color = relationship('color', back_populates='misc_color')
    
    

    
# # ###part 1

# # class network(Base):
# #     __tablename__ = 'network'
# #     id = Column(Integer, primary_key=True)
# #     technology_id = Column(Integer, primary_key=True,autoincrement=True)
# #     _2g_id = Column(Integer, ForeignKey('network_2g.id'), nullable=False)
# #     _3g_id = Column(Integer, ForeignKey('network_3g.id'), nullable=False)
# #     _4g_id = Column(Integer, ForeignKey('network_4g.id'), nullable=False)
# #     _5g_id = Column(Integer, ForeignKey('network_5g.id'), nullable=False)
# #     speed_id = Column(Integer, ForeignKey('network_speed.id'), nullable=False)
# #     network_2g = relationship('network_2g', back_populates='network')
# #     network_3g = relationship('network_3g', back_populates='network')
# #     network_4g = relationship('network_4g', back_populates='network')
# #     network_5g = relationship('network_5g', back_populates='network')
# #     network_speed = relationship('network_speed', back_populates='network')
    

# # class launch_detail(Base):
# #     __tablename__ = 'launch_detail'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     announced = Column(String(255))
# #     status = Column(String(11))   
     
# # class body(Base):
# #     __tablename__ = 'body'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     dimensions = Column(String(255))
# #     weight = Column(Integer)
# #     sim_id = Column(Integer, ForeignKey('body_sim.id'), nullable=False)  
# #     body_sim = relationship('body_sim', back_populates='body')
      
    
# # class display(Base):
# #     __tablename__ = 'display'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     type = Column(String(255))
# #     size = Column(String(11))
# #     resolution = Column(String(11))
# #     protection_id = Column(Integer, ForeignKey('display_protection.id'), nullable=False)    
# #     display_protection = relationship('display_protection', back_populates='display')
    
    
# # class platform(Base):
# #     __tablename__ = 'platform'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     os_id = Column(Integer, ForeignKey('platform_os.id'), nullable=False)
# #     chipset_id = Column(Integer, ForeignKey('platform_chipset.id'), nullable=False)
# #     cpu = Column(String(255))
# #     gpu = Column(String(255))  
# #     platform_chipset = relationship('platform_chipset', back_populates='platform')
# #     platform_os = relationship('platform_os', back_populates='platform')
    
    
# # class memory(Base):
# #     __tablename__ = 'memory'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     card_slot = Column(Integer, ForeignKey('memory_card.id'), nullable=False)
# #     internal_id = Column(Integer, ForeignKey('memory_internal.id'), nullable=False)
# #     memory_card = relationship('memory_card', back_populates='memory')
# #     memory_internal = relationship('memory_internal', back_populates='memory')
    

# # class sound(Base):
# #     __tablename__ = 'sound'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     Loudspeaker = Column(String(11))
# #     jack = Column(String(11))

# # class comms(Base):
# #     __tablename__ = 'comms'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     wlan_id = Column(Integer, ForeignKey('comms_wlan.id'), nullable=False)
# #     bluetooth_id = Column(Integer, ForeignKey('comms_blue.id'), nullable=False)
# #     positioning = Column(String(255))
# #     nfc = Column(String(3))
# #     radio = Column(String(11))
# #     usb_id = Column(Integer, ForeignKey('comms_usb.id'), nullable=False)
# #     wlan_id = relationship('wlan_id', back_populates='comms')
# #     bluetooth_id = relationship('bluetooth_id', back_populates='comms')
# #     usb_id = relationship('usb_id', back_populates='comms')
    

# # class feature(Base):
# #     __tablename__ = 'feature'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     sensors_id = Column(Integer, ForeignKey('feature_sensors.id'), nullable=False)
# #     feature_sensors = relationship('feature_sensors', back_populates='feature')
    

# # class battery(Base):
# #     __tablename__ = 'battery'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     type_id = Column(Integer, ForeignKey('battery_type.id'), nullable=False)
# #     charching_id = Column(Integer, ForeignKey('battery_charg.id'), nullable=False)
# #     battery_type = relationship('battery_type', back_populates='battery')
# #     battery_charg = relationship('battery_charg', back_populates='battery')
    

# # class misc(Base):
# #     __tablename__ = 'misc'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     colors_id = Column(Integer, ForeignKey('misc_color.id'), nullable=False)
# #     models = Column(String(255))
# #     sar = Column(String(11))
# #     sar_EU = Column(String(11))
# #     price = Column(Integer)
# #     misc_color = relationship('misc_color', back_populates='misc')
    
    


# # ###part 0


# # class device(Base):
# #     __tablename__ = 'device'
# #     id = Column(Integer, primary_key=True,autoincrement=True)
# #     network_id = Column(Integer, ForeignKey('network.id'), nullable=False)
# #     launch_id = Column(Integer, ForeignKey('launch_detail.id'), nullable=False)
# #     body_id = Column(Integer, ForeignKey('body.id'), nullable=False)
# #     display_id = Column(Integer, ForeignKey('display.id'), nullable=False)
# #     platform_id = Column(Integer, ForeignKey('platform.id'), nullable=False)
# #     memory_id = Column(Integer, ForeignKey('memory.id'), nullable=False)
# #     # camera_id = Column(Integer, ForeignKey('camera.id'), nullable=False)
# #     sound_id = Column(Integer, ForeignKey('sound.id'), nullable=False)
# #     comms_id = Column(Integer, ForeignKey('comms.id'), nullable=False)
# #     feature_id = Column(Integer, ForeignKey('feature.id'), nullable=False)
# #     battery_id = Column(Integer, ForeignKey('battery.id'), nullable=False)
# #     misc_id = Column(Integer, ForeignKey('misc.id'), nullable=False)
    
# #     network = relationship('network', back_populates='device')
# #     launch_detail = relationship('launch_detail', back_populates='device')
# #     body = relationship('body', back_populates='device')
# #     display = relationship('display', back_populates='device')
# #     platform = relationship('platform', back_populates='device')
# #     memory = relationship('memory', back_populates='device')
# #     sound = relationship('sound', back_populates='device')
# #     comms = relationship('comms', back_populates='device')
# #     feature = relationship('feature', back_populates='device')
# #     battery = relationship('battery', back_populates='device')
# #     misc = relationship('misc', back_populates='device')
# #     # camera = relationship('camera', back_populates='device')
    
# class AddToTable:
#     def __init__(self):
#         self.connection = create_table('root', '361375Ff@', 'GSM')


        
#     def addDeviceName(self):
#         csvDevice = pd.read_csv('./processed_data.csv')
#         device_name = csvDevice[['brand','model']]
#         device_name = pd.DataFrame(device_name.drop_duplicates().to_records(index=False))
#         device_name.to_sql('device_name', con=self.connection, if_exists='append', index=False)
        
#     def addPlatformChipset(self):
#         csvDevice = pd.read_csv('./processed_data.csv')
#         chipset = csvDevice[['Chipset_Manufacturer']]
#         chipset=pd.DataFrame(chipset.drop_duplicates().to_records(index=False))
#         chipset.to_sql('chipset', con=self.connection, if_exists='append', index=False)

#     def addInternal(self):
#         csvDevice = pd.read_csv('./processed_data.csv')
#         Internal = csvDevice[['Storage','RAM']]
#         Internal=pd.DataFrame(Internal.drop_duplicates().to_records(index=False))
#         Internal.to_sql('internal', con=self.connection, if_exists='append', index=False)
        
        
#     def addCard(self):
#         csvDevice = pd.read_csv('./processed_data.csv')
#         card = csvDevice[['Card_Slot_Type']]
#         card=pd.DataFrame(card.drop_duplicates().to_records(index=False))
#         card.to_sql('card', con=self.connection, if_exists='append', index=False)    
            
#     def addTechnology(self):
#         csvDevice = pd.read_csv('./processed_data.csv')
#         card = csvDevice[['Network_Technology']]
#         card=pd.DataFrame(card.drop_duplicates().to_records(index=False))
#         card.to_sql('technology', con=self.connection, if_exists='append', index=False)
        
#     def addSim(self):
#         csvDevice = pd.read_csv('./processed_data.csv')
#         Body_SIM = csvDevice[['Body_SIM']]
#         Body_SIM=pd.DataFrame(Body_SIM.drop_duplicates().to_records(index=False))
#         Body_SIM.to_sql('sim', con=self.connection, if_exists='append', index=False) 
       
#     def addOs(self):
#         csvDevice = pd.read_csv('./processed_data.csv')
#         base_os = csvDevice[['base_os']]
#         base_os=pd.DataFrame(base_os.drop_duplicates().to_records(index=False))
#         base_os.to_sql('os', con=self.connection, if_exists='append', index=False)
        
        
#     def addBody_sim(self):
#         csvDevice = pd.read_csv('./processed_data.csv')
#         csvDevice = csvDevice[['Body_SIM']]
#         new_data = pd.DataFrame(columns=['sim_id'])

#         sim_mapping = pd.read_sql('SELECT * FROM sim', con=self.connection)

#         for index, row in csvDevice.iterrows():
#             sim_name = row['Body_SIM']
#             try:
#                 sim_id = sim_mapping[sim_mapping['Body_SIM'] == sim_name]['id'].values[0]        
#                 new_data.loc[len(new_data)] = sim_id
#             except:
#                 new_data.loc[len(new_data)] = Null

#         new_data.to_sql('body_sim', con=self.connection, if_exists='append', index=False)
        
#     def addNetwork_technology(self):
#         csvDevice = pd.read_csv('./processed_data.csv')
#         csvDevice = csvDevice[['Network_Technology']]
#         new_data = pd.DataFrame(columns=['tech_id'])

#         tech_mapping = pd.read_sql('SELECT * FROM technology', con=self.connection)

#         for index, row in csvDevice.iterrows():
#             tech_name = row['Network_Technology']
#             tech_id = tech_mapping[tech_mapping['Network_Technology'] == tech_name]['id'].values[0]            
#             new_data.loc[len(new_data)] = tech_id
#         new_data.to_sql('network_technology', con=self.connection, if_exists='append', index=False)
        
           
#     # def addBattery_capactiy(self):
#     #     csvDevice = pd.read_csv('./processed_data.csv')
#     #     Battery_capactiy = csvDevice[['Battery_capactiy']]
#     #     Battery_capactiy=pd.DataFrame(Battery_capactiy.drop_duplicates().to_records(index=False))
#     #     Battery_capactiy.to_sql('Battery_capactiy', con=self.connection, if_exists='append', index=False)base_os
        
#     def addAll(self):
#         self.addDeviceName()
#         self.addPlatformChipset()
#         self.addInternal()
#         self.addCard()
#         # self.addBattery_capactiy()Network_Technology
#         self.addTechnology()
#         self.addSim()
#         self.addOs()
#         self.addNetwork_technology()
#         self.addBody_sim()



# if __name__ == '__main__':
#     creator = CreateTable('GSM', 'root', '361375Ff@')
#     add = AddToTable()
#     add.addAll()


