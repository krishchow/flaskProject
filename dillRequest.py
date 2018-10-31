import requests
import dill
import base64

url = 'http://127.0.0.1:5000/pythonObj'
headers = {'codeName':'firstQueue','key':'123456'}
r = requests.get(url, headers=headers)
data = r.json()['pythonCode']
data = base64.b64decode(data)
data = dill.load(data)
print(data)
