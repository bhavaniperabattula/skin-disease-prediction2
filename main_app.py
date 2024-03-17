from flask import Flask, render_template, request
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load your pre-trained deep learning model
model = tf.keras.models.load_model('your_model_path')

# Define class names for diseases (example)
class_names = [4: ('nv', 'Melanocytic nevi', ['Sensitivity to touch around the mole', 'Redness or inflammation around the mole'],['Avoid tight Clothing','Limit exposure to direct sunlight']),
    6: ('mel', 'Melanoma', ['Multiple colors within a mole', 'Bleeding or oozing from a mole'],['Eat a balanced diet rich in antioxidants and vitamins','Avoid smoking and limit alcohol consumption']),
    2: ('bkl', 'Benign keratosis-like lesions',  ['Itching or irritation in affected areas, Round or oval shaped growths', 'Very small growths clustered around the eyes or elsewhere on the face'],['Moisturize Regularly','Manage Stress by meditation or yoga']),
    1: ('bcc', 'Basal cell carcinoma', ['Surrounding skin becoming sunken or depressed','Formation of a flesh-coloured, pearl like bump'],['Avoid harmful chemicals','Wear Protective Clothing']),
    5: ('vasc', 'Pyogenic granulomas and hemorrhage', ['Prone to Ulceration', 'Moist or friable surface structure'],['Use sunscreen with a high SPF','Keep the affected arear covered with a sterile dressing']),
    0: ('akiec', 'Actinic keratoses and intraepithelial carcinomae', ['Swelling and burning in affected region', 'Thickening of the skin'],['Avoid tanning beds and sunlamps','Avoid hot shower and opt for lukewarm water']),
    3: ('df', 'Dermatofibroma', ['Dimpled appearance when pressed', 'Growing in size over time'],['Avoid using harsh chemicals or irritants','Drink plenty of water and maintain proper hydration']) ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image_file = request.files['image']
    if image_file:
        img = Image.open(Skin-Disease)
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
