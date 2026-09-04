![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# ConfigParser
* Configuration files are usually plain text files that store settings and parameters for a program. 
* These settings can include things like database connection strings, API keys, and other configuration parameters that are specific to a particular application or environment.
* `configparser` is a built-in module in Python that provides a way to work with configuration files.
* `configparser` allows you to read and write these configuration files using a simple API, making it easy to manage settings for your Python applications.
* `configparser` supports several different formats for configuration files, including the popular **.ini** file format, which consists of sections and key-value pairs.
* The `configparser` module provides a `ConfigParser()` class that you can use to read and write configuration files. You create an instance of the `ConfigParser()` class, and then use its methods to read and write settings to the configuration file.
* `ConfigParser()` allows you to define sections in your configuration file, which can group related settings together. You can then access settings within a section using their keys.
* `configparser` supports interpolation, which allows you to use variables in your configuration files. You can define variables in the `[DEFAULT]` section of your configuration file, and then reference them in other sections using the `${variable}` syntax.
* `configparser` also provides support for parsing command-line arguments and environment variables, which allows you to override settings in your configuration file at runtime.
* Below is the sample config file data, that will be used in the demo.
* Save the file as `test-data.ini` in `C:/your-path` folder.
```ini
[DEFAULT]
debug = False

[web_server]
host = 127.0.0.1
port = 80

[database]
host = 127.0.0.1
port = 5432
```

## Read Config File
```python
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
```

## Write Config File
```python
import configparser
  
config = configparser.ConfigParser()
data_dir = 'C:/tinitiate/test-data.ini'

# Add sections and options to the config object
config['web_server'] = {'host': '127.0.0.1', 'port': '80'}
config['database'] = {'host': '127.0.0.1', 'port': '5432'}

# Write the config object to a file
with open(data_dir+'config.ini', 'w') as configfile:
    config.write(configfile)
```

## Interpolation
* `ConfigParser()` (the default) enables basic interpolation.
* Below is the sample config file data, that will be used in the demo.
* Save the file as `test-data1.ini` in `C:/your-path` folder.
```ini
[Settings]
data_dir = /path/to/data
file_name = myfile.txt
file_path = %(data_dir)s/%(file_name)s
```
```python
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
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|