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

#######################################################
##### CRONTAB COMMANDS accessed with 'crontab -e' #####
######################################################

SHELL=/bin/bash
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task

# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').

31 13 * * 1-5 cd /home/ubuntu/SP25_DS5111_kvu2et; source env/bin/activate; make ygainers.csv; make wsjgainers.csv; python bin/crontab_csv.py
30 16 * * 1-5 cd /home/ubuntu/SP25_DS5111_kvu2et; source env/bin/activate; make ygainers.csv; make wsjgainers.csv; python bin/crontab_csv.py
1 20 * * 1-5 cd /home/ubuntu/SP25_DS5111_kvu2et; source env/bin/activate; make ygainers.csv; make wsjgainers.csv; python bin/crontab_csv.py
