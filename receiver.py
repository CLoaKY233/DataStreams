import base64
import numpy as np
import cv2
from kafka import KafkaConsumer, KafkaProducer
from keras.models import load_model

# Kafka configuration
bootstrap_servers = ['localhost:9092']
input_topic = 'image_input'
output_topic = 'prediction_output'

# Load the model
model = load_model('Models/dogcatclassifier.h5')

def preprocess_image(img_array):
    img_array = img_array.astype('float32') / 255.0
    img_array = np.reshape(img_array, (1, 256, 256, 1))
    return img_array

def predict_image(img_array):
    preprocessed_img = preprocess_image(img_array)
    prediction = model.predict(preprocessed_img)
    predicted_class = "Cat" if prediction[0][0] > 0.5 else "Dog"
    confidence = prediction[0][0] if predicted_class == "Cat" else 1 - prediction[0][0]
    return predicted_class, confidence

def process_images():
    consumer = KafkaConsumer(input_topic, bootstrap_servers=bootstrap_servers)
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    print("Receiver-Predictor is running. Waiting for images...")

    for message in consumer:
        try:
            # Decode the image
            img_base64 = message.value
            img_bytes = base64.b64decode(img_base64)
            img_array = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_GRAYSCALE)

            # Make prediction
            predicted_class, confidence = predict_image(img_array)

            # Send result back
            result = f"Predicted: {predicted_class}, Confidence: {confidence:.2f}"
            producer.send(output_topic, result.encode('utf-8'))
            producer.flush()
            print(f"Processed image. {result}")
        except Exception as e:
            error_msg = f"Error processing image: {str(e)}"
            producer.send(output_topic, error_msg.encode('utf-8'))
            producer.flush()
            print(error_msg)

if __name__ == "__main__":
    process_images()
