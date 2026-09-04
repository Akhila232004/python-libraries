![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Pytz
* The `pytz` module provides support for working with timezones in Python.
* The `pytz` module includes a database of timezone information that is based on the IANA(Internet Assigned Numbers Authority) Time Zone Database.
* We can use the `all_timezones` attribute to get a list of all the available timezone names.
* We can use the `country_timezones()` function to get a list of timezone names for a specified country code.
* The `datetime.astimezone()` method can be used to convert an aware datetime object to a different timezone.
* `pytz.timezone()`: Returns a timezone object for a specified timezone.
* `localize()`: Associates a timezone with a naive datetime object to create an aware datetime object.
* `normalize()`: Adjusts a datetime object to a specified timezone by handling daylight saving time transitions.
* `utc`: A timezone object for Coordinated Universal Time (UTC).
* `tzinfo`: A base class for implementing timezone information for datetime objects.

## Create Date At A Timezone
```python
# Creation of date at a timezone and associate a timezone with datetime object using `localize`
import datetime
import pytz

str_datetime = '2023-04-19 12:00:00'
l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

# Assign current Date to EST TimeZone
EST_TimeZone = pytz.timezone('America/New_York')
est_date = EST_TimeZone.localize(l_date_time)

print('est_date', est_date)
print('est_date timezone', est_date.tzinfo)
```

## Convert A Datetime At A Timezone To Another Timezone
```python
# Creation of date at a timezone and conversion of date to various timezones using `astimezone`
import datetime
import pytz

str_datetime = '2023-04-19 12:00:00'
l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

# Assign current Date to EST TimeZone
EST_TimeZone = pytz.timezone('America/New_York')
est_date = EST_TimeZone.localize(l_date_time)

print('est_date', est_date)
print('est_date timezone', est_date.tzinfo)

# Convert EST Date to GMT / UTC using "astimezone"
GMT_TimeZone = pytz.timezone('GMT')
gmt_date = est_date.astimezone(GMT_TimeZone)
print('gmt_date', gmt_date)
print('gmt_date timezone', gmt_date.tzinfo)

# Convert EST Date to INDIA TIMEZONE
IN_TimeZone = pytz.timezone('Asia/Kolkata')
india_date = est_date.astimezone(IN_TimeZone)
print('india_date', india_date)
print('india_date timezone', india_date.tzinfo)
```
>Here is a full list of TimeZone values that can be used 
>https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|