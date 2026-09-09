# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Create Date At A Timezone
#  Author       : Team Tinitiate
# ==============================================================================



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
