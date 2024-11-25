import cv2
import os

def capture_images(name):
    if not os.path.exists('dataset'):
        os.makedirs('dataset')
    
    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    print(f"Collecting images for {name}...")
    count = 0
    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            count += 1
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face = frame[y:y+h, x:x+w]
            cv2.imwrite(f"dataset/{name}_{count}.jpg", face)

        cv2.imshow('Collecting Faces', frame)

        if count >= 100:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    print("Dataset collection complete.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    capture_images(name)
import cv2
import os

def capture_images(name):
    if not os.path.exists('dataset'):
        os.makedirs('dataset')
    
    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    print(f"Collecting images for {name}...")
    count = 0
    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            count += 1
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face = frame[y:y+h, x:x+w]
            cv2.imwrite(f"dataset/{name}_{count}.jpg", face)

        cv2.imshow('Collecting Faces', frame)

        if count >= 100:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    print("Dataset collection complete.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    capture_images(name)
