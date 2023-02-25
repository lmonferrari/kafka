import random

from kafka import KafkaProducer as kp

producer = kp(bootstrap_servers="127.0.0.1:9092")

for x in range(10):
    n = random.random()
    producer.send("mensagens", key=b"Chave %d" % x, value=b"Mensagem %f " % n)
