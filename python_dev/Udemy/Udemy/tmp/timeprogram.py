""" import time

print('The time that is: ', time.time())
print('the time that we can reed is: ', time.ctime())
later = time.time() + 15
print('15 seciond from now : ',time.ctime(later)) """

import os, sys
import time

#show stats of an existing file

stinfo = os.stat("modules.py")
print(stinfo)
print("access time of modules.py : %s" %stinfo.st_atime)
print("modified time of modules.py : %s" %stinfo.st_mtime)
os.utime('modules.py',(1591867097.2406194,1591867097.2406194))
print("Done!")

def show_zone_info():
    print('\ttzname : ',time.tzname)
    print('\tzone : ',time.timezone, time.timezone / 3600)
    print('tDST : ',time.daylight)
    print('\tTime : ', time.ctime())
print("Default : ")
show_zone_info()

print('gmtime : ', time.gmtime())
print('localtime : ', time.localtime())