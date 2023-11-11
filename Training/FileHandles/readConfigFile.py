import os
from configparser import ConfigParser

filepath = os.path.dirname(__file__)
configfile = filepath+"\\..\\TestData\\Config.cfg"

# create obj of config parser class
config = ConfigParser()

# to read data from config file:
config.read(configfile)
print(config.get("Section1", "password"))
