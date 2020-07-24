import cv2


def gen(camera, type='normal_camera'):
    while True:
        if type == 'normal_camera':
            frame = camera.get_frame()
        elif type == 'face_detection':
            frame = camera.get_object(classifier=cv2.CascadeClassifier('models/facial_recognition_model.xml'))
        elif type == 'full_body_detection':
            frame = camera.get_object(classifier=cv2.CascadeClassifier('models/fullbody_recognition_model.xml'))
        elif type == 'upper_body_detection':
            frame = camera.get_object(classifier=cv2.CascadeClassifier('models/upperbody_recognition_model.xml'))
        elif type == 'face_mask_detection':
            frame = camera.get_mask()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')