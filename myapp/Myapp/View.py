
import pytz 
from datetime import datetime, timedelta 
from django.shortcuts import render 
#Using pytz library 
def current_datetime(request): 
# Get the standard UTC time 
utc = pytz.utc 
# Get the time zone of the specified location (IST - Indian Standard Time) 
ist = pytz.timezone('Asia/Kolkata') 
# Get the current time in UTC and IST 
datetime_utc = datetime.now(utc) 
datetime_ist = datetime.now(ist) 
# Format the date and time 
formatted_utc = datetime_utc.strftime('%Y-%m-%d %H:%M:%S %Z %z') 
formatted_ist = datetime_ist.strftime('%Y-%m-%d %H:%M:%S %Z %z') 
# Pass the formatted date and time to the template 
context = { 
'utc_time': formatted_utc, 
'ist_time': formatted_ist 
} 
# Render the template with the context 
return render(request, 'myapp/current_datetime.html', context)
#Using pytz library 
def date_time_offset(request): 
# Get the current date and time on the server 
current_datetime = datetime.now() 
# Calculate the date and time four hours ahead and four hours before 
datetime_ahead = current_datetime + timedelta(hours=4) 
datetime_before = current_datetime - timedelta(hours=4) 
# Format the date and time strings 
formatted_current_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S') 
formatted_datetime_ahead = datetime_ahead.strftime('%Y-%m-%d %H:%M:%S') 
formatted_datetime_before = datetime_before.strftime('%Y-%m-%d %H:%M:%S')
# Pass the formatted date and time strings to the template 
context = { 
'current_datetime': formatted_current_datetime, 
'datetime_ahead': formatted_datetime_ahead, 
'datetime_before': formatted_datetime_before 
} 
# Render the template with the context 
return render(request, 'myapp/date_time_offset.html', context)
