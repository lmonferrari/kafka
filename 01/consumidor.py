from kafka import KafkaConsumer as kc

consumer = kc("mensagens", bootstrap_servers="127.0.0.1:9092",
              consumer_timeout_ms=1000)

for message in consumer:
    print('a')
    print(message.topic)
