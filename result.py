from kafka import KafkaConsumer

# Kafka configuration
bootstrap_servers = ['localhost:9092']
output_topic = 'prediction_output'

def receive_results():
    consumer = KafkaConsumer(output_topic, bootstrap_servers=bootstrap_servers)
    print("Result consumer is running. Waiting for predictions...")

    for message in consumer:
        print(f"Received prediction: {message.value.decode('utf-8')}")

if __name__ == "__main__":
    receive_results()
