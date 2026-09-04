# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : JSON Schema Validation
#  Author       : Team Tinitiate
# ==============================================================================



import json
import jsonschema

# Read the JSON data from file
try:
    with open('C:/tinitiate/product.json', 'r') as f:
        data = json.load(f)
except ValueError as e:
    print("Malformed JSON data:", e)
    exit()

# Read the JSON schema from file
try:
    with open('C:/tinitiate/schema.json', 'r') as f:
        schema = json.load(f)
except ValueError as e:
    print("Malformed JSON schema:", e)
    exit()

# Validate the JSON data against the schema
try:
    jsonschema.validate(data, schema)
    print("JSON data is valid!")
    
except jsonschema.exceptions.ValidationError as e:
    print("JSON validation error:", e)
