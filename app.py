from flask import Flask, render_template, request, redirect, url_for
import your_prediction_module  # Import your module for disease prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    image_file = request.files['image']
    if image_file:
        # Call your function for image prediction
        predicted_disease = your_prediction_module.predict(image_file)
        return predicted_disease
    return 'Error: No image provided.'

@app.route('/result')
def result():
    disease_name = request.args.get('disease')
    return render_template('result.html', disease_name=disease_name)

if __name__ == '__main__':
    app.run(debug=True)
