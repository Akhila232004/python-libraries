# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Read Config File
#  Author       : Team Tinitiate
# ==============================================================================



import configparser

config = configparser.ConfigParser()
data_dir = 'C:/tinitiate/'
config.read(data_dir+'test-data.ini')

# Read values from DEFAULT section
debug = config.getboolean('DEFAULT', 'debug')
print(debug)

# Read values from web_server section
web_host = config.get('web_server', 'host')
web_port = config.getint('web_server', 'port')
print(web_host, web_port)

# Read values from database section
db_host = config.get('database', 'host')
db_port = config.getint('database', 'port')
print(db_host, db_port)
