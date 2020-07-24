import cv2
import time
from tf_lite import Model
import numpy as np


class VideoCamera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        time.sleep(2)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        _, frame = self.cap.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def get_object(self, classifier):
        _, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        objects = classifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the objects
        for (x, y, w, h) in objects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 140, 125), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def get_mask(self):
        _, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_cls = cv2.CascadeClassifier('models/facial_recognition_model.xml')
        faces = face_cls.detectMultiScale(gray, 1.3, 5)

        model = Model()
        interpreter = model.load_interpreter()
        input_details = model.input_details()
        output_details = model.output_details()
        input_shape = input_details[0]['shape']
        img_size = 100

        label_dict = {0: 'MASK', 1: "NO MASK"}
        color_dict = {0: (0, 255, 0), 1: (0, 0, 255)}

        for x, y, w, h in faces:
            face_img = gray[y:y + h, x:x + w]
            resized = cv2.resize(face_img, (img_size, img_size))
            normalized = resized / 255.0
            reshaped = np.reshape(normalized, input_shape)
            reshaped = np.float32(reshaped)
            interpreter.set_tensor(input_details[0]['index'], reshaped)
            interpreter.invoke()
            result = interpreter.get_tensor(output_details[0]['index'])

            label = np.argmax(result, axis=1)[0]

            cv2.rectangle(frame, (x, y), (x + w, y + h), color_dict[label], 2)
            cv2.rectangle(frame, (x, y - 4), (x + w, y), color_dict[label], -1)
            cv2.putText(frame, label_dict[label], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (250, 240, 255), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

