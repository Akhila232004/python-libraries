# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Write Config File
#  Author       : Team Tinitiate
# ==============================================================================



import configparser
  
config = configparser.ConfigParser()
data_dir = 'C:/tinitiate/'

# Add sections and options to the config object
config['web_server'] = {'host': '127.0.0.1', 'port': '80'}
config['database'] = {'host': '127.0.0.1', 'port': '5432'}

# Write the config object to a file
with open(data_dir+'config.ini', 'w') as configfile:
    config.write(configfile)
