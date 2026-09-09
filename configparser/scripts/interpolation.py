# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Interpolation
#  Author       : Team Tinitiate
# ==============================================================================



import configparser

# By default interpolation is enabled
config = configparser.ConfigParser()
# Disable interpolation
# config = configparser.ConfigParser(interpolation=None)
config.read('C:/tinitiate/test-data1.ini')

data_dir = config.get('Settings', 'data_dir')
file_name = config.get('Settings', 'file_name')
file_path = config.get('Settings', 'file_path')

print(f"data_dir: {data_dir}")
print(f"file_name: {file_name}")
print(f"file_path: {file_path}")
