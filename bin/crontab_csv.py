import os
from datetime import datetime
from zoneinfo import ZoneInfo

# use ZoneInfo to set time zone to EST
now = datetime.now(ZoneInfo("America/New_York"))
date = str(now.date())
time = str(now.time()).replace(':', '-')

filename_ygain = 'ygainers_' + date + '_at_' + time[:-10] + '.csv'
filename_wsj = 'wsjgainers_' + date + '_at_' + time[:-10] + '.csv'
# rename files and move them to proper folders
os.rename('ygainers.csv', 'collected_data/' +  filename_ygain)
os.rename('wsjgainers.csv', 'collected_data/' + filename_wsj)


