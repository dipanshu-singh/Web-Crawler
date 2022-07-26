import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data)
    info= json.loads(data.decode())
    print('Count:',len(info['comments']))
    sum=0
    for item in info['comments']:
        sum+=int(item['count'])
    print('Sum:',sum)