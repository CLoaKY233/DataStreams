# Kafka-based Real-time Image Classifier

This project demonstrates a real-time cat/dog image classification system using Kafka and a pre-trained CNN model.

## Prerequisites

- Python 3.7+
- Apache Kafka
- Git

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/kafka-image-classifier.git
   cd kafka-image-classifier
   ```

2. Set up Kafka:
   Follow the instructions in [KafkaSetup.md](KafkaSetup.md) to install and configure Kafka.

3. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Ensure `dogcatclassifier.h5` (the pre-trained model) is in the project root directory.

## Components

The system consists of three main components:

1. **Receiver-Predictor**: Processes images and makes predictions.
2. **Sender**: Allows you to send images for classification.
3. **Result Consumer**: (Optional) Displays classification results in real-time.

## Usage

### 1. Start the Receiver-Predictor

In a terminal, run:
```
python receiver_predictor.py
```

This will continuously wait for images on the Kafka topic.

### 2. Run the Sender

In another terminal, run:
```
python sender.py
```

- You'll be prompted to enter paths to image files.
- Enter the full path to an image when prompted.
- Type 'quit' to exit the sender program.

### 3. (Optional) Run the Result Consumer

To see predictions in real-time, open a third terminal and run:
```
python result_consumer.py
```

## Example Workflow

1. Ensure Kafka is running (refer to KafkaSetup.md).

2. Open three terminal windows and navigate to the project directory in each.

3. In Terminal 1, start the receiver-predictor:
   ```
   python receiver_predictor.py
   ```

4. In Terminal 2, start the sender:
   ```
   python sender.py
   ```

5. (Optional) In Terminal 3, start the result consumer:
   ```
   python result_consumer.py
   ```

6. In the sender terminal (Terminal 2), enter an image path when prompted:
   ```
   Enter the path to the image (or 'quit' to exit): /path/to/your/cat_image.jpg
   ```

7. View the results in Terminal 1 (receiver-predictor) or Terminal 3 (result consumer).

8. Repeat step 6 with different images as desired.

9. Type 'quit' in Terminal 2 (sender) to exit.

## Troubleshooting

- Verify Kafka is running correctly (check KafkaSetup.md).
- Ensure `dogcatclassifier.h5` is present in the project root.
- Verify all dependencies are installed (`pip list`).
- Check that the image paths you enter exist and are accessible.

## Customization

- To use a different model, replace `dogcatclassifier.h5` and update `receiver_predictor.py` if needed.
- Kafka topics and server addresses can be modified in the scripts if required.
