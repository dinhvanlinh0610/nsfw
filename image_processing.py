import cv2
import numpy as np

def save_temp_image(file):
    file_path = 'temp.jpg'
    file.save(file_path)
    return file_path

def preprocess_image(image_path):
    # Đọc ảnh
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Tiền xử lý ảnh
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    return image
