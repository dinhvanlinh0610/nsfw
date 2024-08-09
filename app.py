from flask import Flask, request, jsonify
from utils.image_processing import save_temp_image
from utils.nsfw_classifier import classify_image, classify_nsfw
import os

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Lưu ảnh tạm thời
    file_path = save_temp_image(file)
    
    # Phân loại ảnh
    predictions = classify_image(file_path)
    os.remove(file_path)
    
    # Xử lý dự đoán
    nsfw_detected = classify_nsfw(predictions)
    
    return jsonify({
        'predictions': predictions[0].tolist(),
        'nsfw_detected': nsfw_detected
    })

if __name__ == '__main__':
    app.run(debug=True)
