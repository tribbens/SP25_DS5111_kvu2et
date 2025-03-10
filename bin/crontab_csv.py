import os
from datetime import datetime
from zoneinfo import ZoneInfo
# use ZoneInfo to set time zone to EST
now = datetime.now(ZoneInfo("America/New_York"))
date = str(now.date())
time = str(now.time()).replace(':', '-')

filename = 'ygainers_' + date + '_at_' + time[:-10] + '.csv'
print(filename)
# rename file and move it to proper folder
os.rename('ygainers.csv', 'collected_data/' +  filename)
