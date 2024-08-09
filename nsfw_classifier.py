import tensorflow as tf
from utils.image_processing import preprocess_image
from utils.config import NSFW_THRESHOLDS, NSFW_LABELS
model_path = 'app/nsfw_model/nsfw_mobilenet2.224x224.h5'

model = tf.keras.models.load_model(model_path)

def classify_image(image_path):
    processed_image = preprocess_image(image_path)
    predictions = model.predict(processed_image)
    return predictions

def classify_nsfw(predictions):
    scores = predictions[0]
    
    nsfw_detected = False
    for label, threshold in NSFW_THRESHOLDS.items():
        if label in NSFW_LABELS:
            index = NSFW_LABELS.index(label)
            if scores[index] >= threshold:
                nsfw_detected = True
                break
    
    return nsfw_detected
