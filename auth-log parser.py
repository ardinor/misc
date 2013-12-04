import re
import gzip
import os
import time
from datetime import date, timedelta, datetime

search_string = '(?P<log_date>^.*) defestri sshd.*Invalid user (?P<user>.*) from (?P<ip_add>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
#log_dir = 'C:/Temp/log'
log_dir = '/var/log/'

fail2ban_search_string = '(?P<log_date>^.*) fail2ban.actions: WARNING \[ssh] Ban (?P<ip_add>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

last_month = date.today().replace(day=1) - timedelta(days=1) #.strftime('%b')
two_month_ago = last_month.replace(day=1) - timedelta(days=1)

seen_ip = []
seen_user = []
banned_ip = {}

def tz_setup():
    if time.localtime().tm_isdst:
        displayed_time = time.tzname[time.daylight]
        time_offset = (time.altzone * -1) / 3600
    else:
        displayed_time = time.tzname[0]
        time_offset = (time.timezone * -1) / 3600

    if time_offset > 0:
        time_offset = '+{}'.format(time_offset)

    return displayed_time, time_offset

for i in os.listdir(log_dir):
    if 'auth.log' in i or 'fail2ban.log' in i:
        modified_date = datetime.strptime(time.ctime(os.path.getmtime(
                        os.path.join(log_dir, i))), "%a %b %d %H:%M:%S %Y")
        if  modified_date > two_month_ago:
            if 'auth.log' in i:
                auth_log = True
            else:
                auth_log = False
            if os.path.splitext(i)[1] == '.gz':
                f = gzip.open(os.path.join(log_dir, i), 'r')
                file_content = f.read()
                split_text = file_content.split('\n')
                for j in split_text:
                    if auth_log:
                        m = re.search(search_string, j)
                        if m:
                            if m.group('log_date')[:3] == last_month.strftime('%b'):
                                seen_ip.append(m.group('ip_add'))
                                seen_user.append(m.group('user'))
                    else:
                        m = re.search(fail2ban_search_string, j)
                        if m:
                                b_time = datetime.strptime(m.group('log_date'),
                                            '%Y-%m-%d %H:%M:%S,%f')
                                banned_ip[b_time] = m.group('ip_add')
            else:
                with open(os.path.join(log_dir, i), 'r') as f:
                    for line in f:
                        if auth_log:
                            m = re.search(search_string, line)
                            if m:
                                if m.group('log_date')[:3] == last_month.strftime('%b'):
                                    seen_ip.append(m.group('ip_add'))
                                    seen_user.append(m.group('user'))
                        else:
                            m = re.search(fail2ban_search_string, line)
                            if m:
                                b_time = datetime.strptime(m.group('log_date'),
                                            '%Y-%m-%d %H:%M:%S,%f')
                                banned_ip[b_time] = m.group('ip_add')

if __name__ == '__main__':

    displayed_time, time_offset = tz_setup()
