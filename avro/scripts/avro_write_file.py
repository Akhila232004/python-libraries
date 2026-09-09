# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Write Avro File
#  Author       : Team Tinitiate
# ==============================================================================



from avro.datafile import DataFileWriter
from avro.io import DatumWriter
from avro_schema_generator import schema

file_path = "C:/tinitiate/users.avro"

# Open file for writing
with open(file_path, "wb") as out:
    writer = DataFileWriter(out, DatumWriter(), schema)

    # Add records
    writer.append({"name": "Alice", "favorite_number": 7, "favorite_color": "red"})
    writer.append({"name": "Bob", "favorite_number": None, "favorite_color": "blue"})
    writer.append({"name": "Charlie", "favorite_number": 42, "favorite_color": None})

    writer.close()

print(f"✅ Avro file written to {file_path}")
