from kafka3 import KafkaConsumer as kc

consumer = kc('pessoas')

for msg in consumer:
    print(msg.value)
