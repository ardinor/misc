import re
import gzip
import os
import time
import json
import urllib, urllib2
from datetime import timedelta, datetime
from jinja2 import Environment, FileSystemLoader

from settings import API_URL, API_KEY, LOG_DIR, SEARCH_STRING, FAIL2BAN_SEARCH_STRING

DIR = os.path.dirname(os.path.realpath(__file__))

env = Environment(loader=FileSystemLoader(DIR))
template = env.get_template('template.html')

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

def check_ip_location(ip):

    params = {'format': 'json', 'key': API_KEY, 'ip': ip, 'timezone': 'false'}
    print 'Checking IP - {}'.format(ip)
    url_params = urllib.urlencode(params)
    url = API_URL + '?' + url_params
    url_obj = urllib2.urlopen(url)
    response = url_obj.read()
    url_obj.close()
    response_dict = json.loads(response)

    return_dict = {}

    if 'cityName' in response_dict:
        return_dict['region'] = response_dict['cityName'] + ', ' + response_dict['regionName']
    else:
        return_dict['region'] = response_dict['regionName']

    return_dict['county'] = response_dict['countryName']

    return return_dict

def parse_content(content, breakin_attempt, banned_ip, last_month, auth_log):

    for j in content:
        if auth_log:
            m = re.search(SEARCH_STRING, j)
            if m:
                if m.group('log_date')[:3] == last_month.strftime('%b'):
                    log_date = datetime.strptime(m.group('log_date'), '%b %d %H:%M:%S')
                    log_date = log_date.replace(year=last_month.year)
                    #sometimes there's multiple entries per second, since we're
                    #not that concerned about to the second accuracy just increment
                    #the seconds until we find a unique log date to put in
                    if log_date in breakin_attempt:
                        while log_date in breakin_attempt:
                            ns = log_date.second+1
                            if ns >= 60:
                                ns = 0
                            log_date = log_date.replace(second=ns)
                    breakin_attempt[log_date] = (m.group('ip_add'), m.group('user'))

        else:
            m = re.search(FAIL2BAN_SEARCH_STRING, j)
            if m:
                    b_time = datetime.strptime(m.group('log_date'),
                                '%Y-%m-%d %H:%M:%S,%f')
                    banned_ip[b_time] = m.group('ip_add')


    return breakin_attempt, banned_ip

def read_logs(log_dir):

    banned_ip = {}
    breakin_attempt = {}

    last_month = datetime.now().replace(day=1) - timedelta(days=1) #.strftime('%b')
    two_month_ago = last_month.replace(day=1) - timedelta(days=1)

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
                    breakin_attempt, banned_ip = parse_content(split_text,
                                                               breakin_attempt,
                                                               banned_ip,
                                                               last_month,
                                                               auth_log)

                else:
                    with open(os.path.join(log_dir, i), 'r') as f:
                        breakin_attempt, banned_ip = parse_content(f,
                                                                   breakin_attempt,
                                                                   banned_ip,
                                                                   last_month,
                                                                   auth_log)

    return breakin_attempt, banned_ip


if __name__ == '__main__':

    print 'Begin.'
    last_month = datetime.now().replace(day=1) - timedelta(days=1)
    print 'Timezone setup...'
    displayed_time, time_offset = tz_setup()
    print 'Reading logs...'
    breakin_attempt, banned_ip = read_logs(LOG_DIR)
    unique_ips = set()
    for i in breakin_attempt.values():
        unique_ips.add(i[0])
    ip_and_location = {}
    print 'Checking IP locations...'
    for i in unique_ips:
        ip_and_location[i] = check_ip_location(i)
        # be a good citizen and only hit the site every two seconds
        time.sleep(2)

    print 'Building output...'
    output_parsed_template = template.render(displayed_time=displayed_time,
                                             time_offset=time_offset,
                                             last_month=last_month,
                                             breakin_attempts=breakin_attempt,
                                             bans=banned_ip,
                                             ips=ip_and_location)

    with open(os.path.join(DIR, 'index.html'), 'wb') as f:
        f.write(output_parsed_template)

    print 'Finished!'
