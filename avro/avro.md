![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Avro
* Avro(Apache Avro) is a row-oriented data serialization format (like JSON, but designed for Hadoop ecosystem).
* It’s part of the Apache Hadoop ecosystem and widely used in Kafka, Spark, Hive, Flink, and other big data pipelines.
* Avro is language-neutral (works with Java, Python, C++, etc.).
* You define a schema (JSON string), and data is stored with this schema.
* Avro files stores both the its schema and data(Serialized data encoded with that schema), making it self-describing.
* Avro supports fast serialization, schema evolution, and is widely used with Kafka, Hadoop, Spark, etc.
```bash
# To install 'avro' run the following command
python -m pip install avro-python3
```

## Avro Schema Generator
```python
import avro.schema
import json

l_schema = {
    "namespace": "example.avro",
    "type": "record",
    "name": "User",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "favorite_number", "type": ["int", "null"]},
        {"name": "favorite_color", "type": ["string", "null"]}
    ]
}

schema_str = json.dumps(l_schema)
schema = avro.schema.Parse(schema_str)
```

## Write Avro File
```python
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
```

## Read Avro File
```python
from avro.datafile import DataFileReader
from avro.io import DatumReader

file_path = "C:/tinitiate/users.avro"
with open(file_path, "rb") as f:
    reader = DataFileReader(f, DatumReader())
    for user in reader:
        print(user)   # Each record is a Python dict
    reader.close()
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|