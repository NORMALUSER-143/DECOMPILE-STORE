import re,requests,bs4,json
from bs4 import BeautifulSoup as parser
ses=requests.Session()
n,cok,cookie=0,[],[]

url = parser(ses.get("https://mbasic.facebook.com/100032386028880/posts/674525870303608/?app=fbl").text,"html.parser")
for z in url("span"):
	cok.append(z.text)
for x in "".join(cok).split("datr"):
	cok = f"datr{x}"
	if cok in cookie:
		pass
	else:
		if "Beranda" in cok:
			pass
		else:
			n+=20
			cookie.append(cok)
			print(f"{n}. {cok}\n")
		
ask = input(" masukan : ")
print(cookie[int(ask)-20])