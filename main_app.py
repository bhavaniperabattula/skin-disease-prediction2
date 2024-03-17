from flask import Flask, render_template, request
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load your pre-trained deep learning model
model = tf.keras.models.load_model('your_model_path')

# Define class names for diseases (example)
class_names = ['Disease A', 'Disease B', 'Disease C', 'Disease D', 'Disease E']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image_file = request.files['image']
    if image_file:
        img = Image.open(image_file)
        img = img.resize((224, 224))  # Resize image according to your model input size
        img_array = np.array(img) / 255.0  # Normalize image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        prediction = model.predict(img_array)
        predicted_class_index = np.argmax(prediction)
        disease_name = class_names[predicted_class_index]
        return disease_name
    return 'Error: No image provided.'

if __name__ == '__main__':
    app.run(debug=True)
