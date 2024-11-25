import face_recognition
import cv2
import os
import numpy as np

def train_model():
    known_faces = []
    known_names = []
    
    image_paths = os.listdir('dataset')
    
    for image_name in image_paths:
        image_path = os.path.join('dataset', image_name)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        
        known_faces.append(encoding)
        known_names.append(image_name.split('_')[0])  # Extract the name part of the filename
    
    print("Model training complete.")
    return known_faces, known_names

if __name__ == "__main__":
    known_faces, known_names = train_model()
    np.save('known_faces.npy', known_faces)
    np.save('known_names.npy', known_names)
