from kafka3 import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

print("Gerando info...")
for _ in range(100):
    print()
    producer.send(topic='mensagens', value=b'some_message_bytes')
