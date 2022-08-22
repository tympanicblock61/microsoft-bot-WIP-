import requests
import datetime

now = datetime.datetime.now()
global cookie, urls
urls = []
session = requests.session()
cookies = session.get('https://rewards.bing.com/api')
cookies = cookies.cookies
for item in cookies:
    if '<Cookie MSPRequ=id=N&lt=' in str(item):
        cookie = str(item).replace("<Cookie MSPRequ=id=N&lt=", '').replace("&co=1 for .login.live.com/>", '')

cookies = 'put your cookies here'
query = {'type': '1', 'X-Requested-With': 'XMLHttpRequest', '_': cookie}

info = requests.get(f'https://rewards.bing.com/api/getuserinfo?type=1&X-Requested-With=XMLHttpRequest&_={cookie}',
                    headers={'cookie': cookies}, params=query).json()

if now.month < 10:
    month = '0' + str(now.month)
else:
    month = now.month
if now.day < 10:
    day = '0' + str(now.day)
else:
    day = now.day
for item in info['dashboard']['dailySetPromotions'][f"{month}/{day}/{now.year}"]:
    urls.append(item['destinationUrl'])

for item in info['dashboard']['morePromotions']:
    urls.append(item['destinationUrl'])
