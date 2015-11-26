import requests
r = requests.post('https://garpun.amocrm.ru/private/api/auth.php?type=json',
                  data = {"USER_LOGIN":"meta@realweb.ru", "USER_HASH":"f6fc87708b2ab944f069977de0e4a6c4"}
                  ,headers={"accept", "application/json"})
print(r.status_code)
print(r.headers['content-type'])
print(r.text)
print(r.json())

	# var accountsResponse = getData(Unirest.get('https://garpun.amocrm.ru/private/api/v2/json/accounts/current')
	# 	.asString()
	# 	.getBody());
