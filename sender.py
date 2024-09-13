import base64
from kafka import KafkaProducer
import cv2

# Kafka configuration
bootstrap_servers = ['localhost:9092']
input_topic = 'image_input'

def send_image(image_path):
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    try:
        # Read and preprocess the image
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError("Image not found or unable to open.")
        img = cv2.resize(img, (256, 256))
        _, img_encoded = cv2.imencode('.jpg', img)

        # Encode the image as base64
        img_base64 = base64.b64encode(img_encoded.tobytes())

        # Send the image to Kafka
        producer.send(input_topic, img_base64)
        producer.flush()
        print(f"Sent image: {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

if __name__ == "__main__":
    while True:
        image_path = input("Enter the path to the image (or 'quit' to exit): ")
        if image_path.lower() == 'quit':
            break
        send_image(image_path)

    print("Sender terminated.")
