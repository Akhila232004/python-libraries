# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Read Avro File
#  Author       : Team Tinitiate
# ==============================================================================



from avro.datafile import DataFileReader
from avro.io import DatumReader

file_path = "C:/tinitiate/users.avro"
with open(file_path, "rb") as f:
    reader = DataFileReader(f, DatumReader())
    for user in reader:
        print(user)   # Each record is a Python dict
    reader.close()
