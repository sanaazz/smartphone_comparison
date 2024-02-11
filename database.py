from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, text, Date, Float
from sqlalchemy.orm import relationship
from database_eng import *
import pandas as pd
import numpy as np
import os

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
 
###part 3
class device_name(Base):
    __tablename__ = 'device_name'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    
class internal(Base):
    __tablename__ = 'internal'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class chipset(Base):
    __tablename__ = 'chipset'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class wlan(Base):
    __tablename__ = 'wlan'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class bluetooth(Base):
    __tablename__ = 'bluetooth'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class usb(Base):
    __tablename__ = 'usb'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class type(Base):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class charge(Base):
    __tablename__ = 'charge'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class color(Base):
    __tablename__ = 'color'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class technology(Base):
    __tablename__ = 'technology'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class n2g(Base):
    __tablename__ = 'n2g'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class n3g(Base):
    __tablename__ = 'n3g'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class n4g(Base):
    __tablename__ = 'n4g'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class n5g(Base):
    __tablename__ = 'n5g'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class speed(Base):
    __tablename__ = 'speed'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class sim(Base):
    __tablename__ = 'sim'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class protection(Base):
    __tablename__ = 'protection'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class os(Base):
    __tablename__ = 'os'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class charg(Base):
    __tablename__ = 'charg'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

##part 2
class network_technology(Base):
    __tablename__ = 'network_technology'
    id = Column(Integer, primary_key=True)
    tech_id = Column(Integer, ForeignKey('technology.id'), nullable=False)
    
class network_2g(Base):
    __tablename__ = 'network_2g'
    id = Column(Integer, primary_key=True)
    n2g_id = Column(Integer, ForeignKey('n2g.id'), nullable=False)
    
class network_3g(Base):
    __tablename__ = 'network_3g'
    id = Column(Integer, primary_key=True)
    n3g_id = Column(Integer, ForeignKey('n3g.id'), nullable=False)
    
class network_4g(Base):
    __tablename__ = 'network_4g'
    id = Column(Integer, primary_key=True)
    n4g_id = Column(Integer, ForeignKey('n4g.id'), nullable=False)
    
class network_5g(Base):
    __tablename__ = 'network_5g'
    id = Column(Integer, primary_key=True)
    n5g_id = Column(Integer, ForeignKey('n5g.id'), nullable=False)
    
class network_speed(Base):
    __tablename__ = 'network_speed'
    id = Column(Integer, primary_key=True)
    speed_id = Column(Integer, ForeignKey('speed.id'), nullable=False)
    
class body_sim(Base):
    __tablename__ = 'body_sim'
    id = Column(Integer, primary_key=True)
    sim_id = Column(Integer, ForeignKey('sim.id'), nullable=False)
    
class display_protection(Base):
    __tablename__ = 'display_protection'
    id = Column(Integer, primary_key=True)
    protection_id = Column(Integer, ForeignKey('protection.id'), nullable=False)
    
class platform_os(Base):
    __tablename__ = 'platform_os'
    id = Column(Integer, primary_key=True)
    os_id = Column(Integer, ForeignKey('os.id'), nullable=False)
    
class platform_chipset(Base):
    __tablename__ = 'platform_chipset'
    id = Column(Integer, primary_key=True)
    chipset_id = Column(Integer, ForeignKey('chipset.id'), nullable=False)
    
class memory_card(Base):
    __tablename__ = 'memory_card'
    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey('card.id'), nullable=False)
    
class memory_internal(Base):
    __tablename__ = 'memory_internal'
    id = Column(Integer, primary_key=True)
    internal_id = Column(Integer, ForeignKey('internal.id'), nullable=False)
    
class comms_wlan(Base):
    __tablename__ = 'comms_wlan'
    id = Column(Integer, primary_key=True)
    wlan_id = Column(Integer, ForeignKey('wlan.id'), nullable=False)
    
class comms_blue(Base):
    __tablename__ = 'comms_blue'
    id = Column(Integer, primary_key=True)
    wlan_id = Column(Integer, ForeignKey('wlan.id'), nullable=False)
    
class comms_usb(Base):
    __tablename__ = 'comms_usb'
    id = Column(Integer, primary_key=True)
    usb_id = Column(Integer, ForeignKey('usb.id'), nullable=False)
    
class feature_sensors(Base):
    __tablename__ = 'feature_sensors'
    id = Column(Integer, primary_key=True)
    sensors = Column(String(255))
    
class battery_type(Base):
    __tablename__ = 'battery_type'
    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, ForeignKey('type.id'), nullable=False)
    
class battery_charg(Base):
    __tablename__ = 'battery_charg'
    id = Column(Integer, primary_key=True)
    charg_id = Column(Integer, ForeignKey('charg.id'), nullable=False)
    
class misc_color(Base):
    __tablename__ = 'misc_color'
    id = Column(Integer, primary_key=True)
    color_id = Column(Integer, ForeignKey('color.id'), nullable=False)
    

    
###part 1

class network(Base):
    __tablename__ = 'network'
    id = Column(Integer, primary_key=True)
    technology_id = Column(Integer, primary_key=True)
    _2g_id = Column(Integer, ForeignKey('network_2g.id'), nullable=False)
    _3g_id = Column(Integer, ForeignKey('network_3g.id'), nullable=False)
    _4g_id = Column(Integer, ForeignKey('network_4g.id'), nullable=False)
    _5g_id = Column(Integer, ForeignKey('network_5g.id'), nullable=False)
    speed_id = Column(Integer, ForeignKey('network_speed.id'), nullable=False)

class launch_detail(Base):
    __tablename__ = 'launch_detail'
    id = Column(Integer, primary_key=True)
    announced = Column(String(255))
    status = Column(String(11))   
     
class body(Base):
    __tablename__ = 'body'
    id = Column(Integer, primary_key=True)
    dimensions = Column(String(255))
    weight = Column(Integer)
    sim_id = Column(Integer, ForeignKey('body_sim.id'), nullable=False)    
    
class display(Base):
    __tablename__ = 'display'
    id = Column(Integer, primary_key=True)
    type = Column(String(255))
    size = Column(String(11))
    resolution = Column(String(11))
    protection_id = Column(Integer, ForeignKey('display_protection.id'), nullable=False)    
    
class platform(Base):
    __tablename__ = 'platform'
    id = Column(Integer, primary_key=True)
    os_id = Column(Integer, ForeignKey('platform_os.id'), nullable=False)
    chipset_id = Column(Integer, ForeignKey('platform_chipset.id'), nullable=False)
    cpu = Column(String(255))
    gpu = Column(String(255))  
    
class memory(Base):
    __tablename__ = 'memory'
    id = Column(Integer, primary_key=True)
    card_slot = Column(Integer, ForeignKey('memory_card.id'), nullable=False)
    internal_id = Column(Integer, ForeignKey('memory_internal.id'), nullable=False)

class sound(Base):
    __tablename__ = 'sound'
    id = Column(Integer, primary_key=True)
    Loudspeaker = Column(String(11))
    jack = Column(String(11))

class comms(Base):
    __tablename__ = 'comms'
    id = Column(Integer, primary_key=True)
    wlan_id = Column(Integer, ForeignKey('comms_wlan.id'), nullable=False)
    bluetooth_id = Column(Integer, ForeignKey('comms_blue.id'), nullable=False)
    positioning = Column(String(255))
    nfc = Column(String(3))
    radio = Column(String(11))
    usb_id = Column(Integer, ForeignKey('comms_usb.id'), nullable=False)

class feature(Base):
    __tablename__ = 'feature'
    id = Column(Integer, primary_key=True)
    sensors_id = Column(Integer, ForeignKey('feature_sensors.id'), nullable=False)

class battery(Base):
    __tablename__ = 'battery'
    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, ForeignKey('battery_type.id'), nullable=False)
    charching_id = Column(Integer, ForeignKey('battery_charg.id'), nullable=False)

class misc(Base):
    __tablename__ = 'misc'
    id = Column(Integer, primary_key=True)
    colors_id = Column(Integer, ForeignKey('misc_color.id'), nullable=False)
    models = Column(String(255))
    sar = Column(String(11))
    sar_EU = Column(String(11))
    price = Column(Integer)


###part 0


class device(Base):
    __tablename__ = 'device'
    id = Column(Integer, primary_key=True)
    network_id = Column(Integer, ForeignKey('network.id'), nullable=False)
    launch_id = Column(Integer, ForeignKey('launch_detail.id'), nullable=False)
    body_id = Column(Integer, ForeignKey('body.id'), nullable=False)
    display_id = Column(Integer, ForeignKey('display.id'), nullable=False)
    platform_id = Column(Integer, ForeignKey('platform.id'), nullable=False)
    memory_id = Column(Integer, ForeignKey('memory.id'), nullable=False)
    # camera_id = Column(Integer, ForeignKey('camera.id'), nullable=False)
    sound_id = Column(Integer, ForeignKey('sound.id'), nullable=False)
    comms_id = Column(Integer, ForeignKey('comms.id'), nullable=False)
    feature_id = Column(Integer, ForeignKey('feature.id'), nullable=False)
    battery_id = Column(Integer, ForeignKey('battery.id'), nullable=False)
    misc_id = Column(Integer, ForeignKey('misc.id'), nullable=False)


class AddToTable:
    def __init__(self):
        self.connection = create_table('root', '', 'GSM')
        
        
    def addAll(self):
        self.addCountries()


if __name__ == '__main__':
    # clean = DataCleaning()
    creator = CreateTable('GSM', 'root', '#####')
    add = AddToTable()
    # add.addAll()


