![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# CSVValidator
* `csvvalidator` is a Python library that allows you to define schemas and validate CSV files against them.
* It helps ensure that your CSV data is well-formed, consistent, and follows business rules.
* You can check:
    * Column headers
    * Record length
    * Data types (integer, float, date, etc.)
    * Custom rules (regex, ranges, boolean flags, etc.)
* `csvvalidator` is especially useful when importing CSV data from external sources into your applications, data pipelines, or databases.
```bash
# To install 'csvvalidator' run the following command
python -m pip install csvvalidator
```

## Schema
The csv schema includes:
* **field_names**: tuple of expected CSV column names in the exact order.
* **add_header_check**: ensures header row matches the expected schema.
* **add_record_length_check**: ensures each row has the correct number of columns.
* **add_value_cast** (optional): auto-casts fields (e.g., to int or float).
* **add_value_check**: attaches validation rules for specific fields.
* **datetime_string helper**: validates date/time format.
* **number_range_inclusive** helper: validates numeric ranges.
### Sample 'users' CSV
* Save as `users.csv`.
* Change any value as per your requirement.
```csv
id,first_name,last_name,gender,age,date,is_student,timestamp,email,score
12-1234567,John,Doe,Male,25,10/09/2025,True,2025-09-10 12:00:00,john.doe@example.com,87.5
15-9876543,Jane,Smith,Female,30,05/08/2025,False,2025-08-15 09:30:00,jane.smith@example.org,92.0
```

## CSV Schema Validation
* Validating the 'users' CSV data against the required CSV schema.
```python
import csv
import re
import logging
from datetime import datetime
from csvvalidator import CSVValidator, enumeration, number_range_inclusive, datetime_string

# ---------- logging ----------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('C:/tinitiate/validation.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# ---------- helpers ----------
def is_float(v: str) -> bool:
    try:
        float(v)
        return True
    except Exception:
        return False

def is_timestamp(v: str) -> bool:
    try:
        datetime.strptime(v, '%Y-%m-%d %H:%M:%S')
        return True
    except Exception:
        return False

# ---------- schema ----------
field_names = (
    'id', 'first_name', 'last_name', 'gender', 'age',
    'date', 'is_student', 'timestamp', 'email', 'score'
)
validator = CSVValidator(field_names)

# Header + record-length checks
validator.add_header_check('EX1', 'Invalid header')
validator.add_record_length_check('EX2', 'Invalid record length')

# Value checks — signature: (field, fn, ERR_CODE, ERR_MSG)
validator.add_value_check(
    'id',
    lambda v: re.match(r'^\d{2}-\d{7}$', v or '') is not None,
    'EX3',
    'ID must be in the format XX-XXXXXXX'
)
validator.add_value_check(
    'first_name',
    lambda v: isinstance(v, str) and 0 < len(v) <= 50,
    'EX4',
    'First name cannot be empty or more than 50 characters'
)
validator.add_value_check(
    'last_name',
    lambda v: isinstance(v, str) and 0 < len(v) <= 50,
    'EX5',
    'Last name cannot be empty or more than 50 characters'
)
validator.add_value_check(
    'gender',
    enumeration('Male', 'Female'),
    'EX6',
    'Gender must be either Male or Female'
)
validator.add_value_check(
    'age',
    number_range_inclusive(0, 120, int),
    'EX7',
    'Age must be a positive integer between 0 and 120'
)
validator.add_value_check(
    'date',
    datetime_string('%d/%m/%Y'),
    'EX8',
    'Date must be in the format dd/mm/yyyy'
)
validator.add_value_check(
    'is_student',
    lambda v: isinstance(v, str) and v.lower() in ('true', 'false'),
    'EX9',
    'is_student must be True or False'
)
validator.add_value_check(
    'timestamp',
    is_timestamp,
    'EX10',
    'Timestamp must be in the format YYYY-MM-DD HH:MM:SS'
)
validator.add_value_check(
    'email',
    lambda v: re.match(r'^[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}$', v or '') is not None,
    'EX11',
    'Email must be a valid email address'
)
validator.add_value_check(
    'score',
    is_float,
    'EX12',
    'Score must be a floating point number'
)

# ---------- validate ----------
csv_path = r'C:/tinitiate/users.csv'
with open(csv_path, 'r', newline='', encoding='utf-8') as f:
    data = csv.reader(f)
    problems = validator.validate(data)

if not problems:
    print('CSV is valid')
    logger.info('CSV is valid')
else:
    msg = f'CSV is invalid. Found {len(problems)} exceptions.'
    print(msg)
    logger.warning(msg)
    for p in problems:
        print(p)
        logger.warning(p)
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|