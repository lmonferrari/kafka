import json
import os
from datetime import datetime

import requests

basedir = os.path.dirname(os.path.realpath(__file__))
filepath = 'arquivos'

url = 'https://randomuser.me/api/'
format = '?format=json'


response = requests.get(url + format)
jsoncontent = response.json()
print(jsoncontent)

filename = datetime.now().strftime("%Y%m%d-%H%M%S")


with open(os.path.join(basedir, filepath, f'{filename}.json'), 'w') as f:
    f.write(json.dumps(jsoncontent))
