import requests
import json

# cookies = dict(session_id=r.cookies['session_id'])
#r = requests.get('http://logs.garpun.lan:9200/_stats')#, cookies=cookies)
# r = requests.get('http://logs.garpun.lan:9200/*/_search?pretty')
r = requests.get('http://logs.garpun.lan:9200/_count?pretty')

print(r.status_code)
print(r.headers)
#print(r.text)
print(r.json())
# print(r.cookies)
# for item in r.json()["hits"]["hits"]:
#         print (item)

