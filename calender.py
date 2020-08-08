# #current time
# from datetime import datetime as dt 
# import pytz
# import calendar
# print(len(pytz.all_timezones))
# tz=pytz.timezone('America/New_York')
# print(dt.now(tz))
# print(calendar.weekday(2019,10,21))
import calendar
from datetime import datetime as dt
import pytz
# def check_leap(y):
# 	if y%100==0:
# 		if y%400==0:
# 			return True
# 		else:
# 			return False
# 	else:
# 		if y%4==0:
# 			return True
# 		else:
# 			return False
# def check(dt,m,n):
# 	if m%2==n:
# 		if dt<32:
# 			return True
# 		else:
# 			return False
# 	else:
# 		if dt<31:
# 			return True
# 		else:
# 			return False
# def valied(dt,m,x):
# 	if m ==2:
# 		if dt<x:
# 			return True
# 		else:
# 			return False
# 	else:
# 		if m<8:
# 			return check(dt,m,1)
				
# 		else:
# 			return check(dt,m,0)
				
# def check_valid_date(dt,m,y,l):
# 	if l:
# 		return valied(dt,m,30)
# 	else:
# 		return valied(dt,m,29)

# def get_day(day_index):
# 	list_of_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# 	return list_of_day[day_index]
# while(1):
# 	year=int(raw_input('Enter yearfrom 1970: '))
# 	if year<1970:
# 		print('Enter a year from 1970 ')
# 	else:
# 		break
# while(1):
# 	month=int(raw_input('Enter month(1-12): '))
# 	if month<=12 and month>0:
# 		break
# 	else:
# 		print('Enter a month in the range (1-12) ')
# leap=check_leap(year)

# while(1):
# 	date=int(raw_input('Enter day: '))
# 	if date>0 and check_valid_date(date,month,year,leap):
# 		break
# 	else:
# 		print('Enter a valid date')

# day_index=calendar.weekday(year,month,date)
# day=get_day(day_index)
# print date,"/",month,"/",year,": ",day
timezones=pytz.all_timezones
for i in range(len(timezones)):
	zone=timezones[i]
	tz=pytz.timezone(zone)
	print 'Current time at zone ',zone,' is ',dt.now(tz)