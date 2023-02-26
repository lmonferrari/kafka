import json
import os
import time
from datetime import datetime

import requests

basedir = os.path.dirname(os.path.realpath(__file__))
filepath = 'arquivos'

url = 'https://randomuser.me/api/'
format = '?format=json'

while True:
    response = requests.get(url + format)
    jsoncontent = response.json()
    print(jsoncontent)

    filename = datetime.now().strftime("%Y%m%d-%H%M%S")

    with open(os.path.join(basedir, filepath, f'{filename}.json'), 'w') as f:
        f.write(json.dumps(jsoncontent))

    time.sleep(60)
