# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Avro Schema Generator
#  Author       : Team Tinitiate
# ==============================================================================



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
