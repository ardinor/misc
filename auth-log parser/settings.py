
LOG_DIR = '/var/log/'

SEARCH_STRING = '(?P<log_date>^.*) defestri sshd.*Invalid user (?P<user>.*) from (?P<ip_add>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
FAIL2BAN_SEARCH_STRING = '(?P<log_date>^.*) fail2ban.actions: WARNING \[ssh] Ban (?P<ip_add>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

API_URL = 'http://api.ipinfodb.com/v3/ip-city/'
API_KEY = ''
