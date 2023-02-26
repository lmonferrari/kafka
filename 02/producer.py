import glob
import json
import os
import time

from kafka3 import KafkaProducer as kp

producer = kp(bootstrap_servers='localhost:9092')

basedir = os.path.dirname(os.path.realpath(__file__))
filepath = 'arquivos'

while True:
    files = glob.glob(os.path.join(basedir, filepath, '*.json'))
    for file in files:
        with open(file, 'r') as f:
            file_content = json.load(f)
            print(file_content)
            producer.send('pessoas', value=json.dumps(
                file_content).encode('utf-8'))
        os.remove(file)

    time.sleep(30)
