import requests
r = requests.get('https://api.github.com', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.text)
print(r.json())

r = requests.get('http://gun.io')
print (r.content)