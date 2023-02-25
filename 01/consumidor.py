from kafka3 import KafkaConsumer

consumer = KafkaConsumer('mensagens')
for msg in consumer:
    print(msg.topic)
    print(msg.value)
