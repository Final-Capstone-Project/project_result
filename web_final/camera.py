from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np


fire_cascade = cv2.CascadeClassifier('fire_xml3.xml')   # opencv 학습 xml
classifier = load_model('fire_mobilNet.h5') # 학습된 가중치
class_labels = ['Fire', 'Neutral']

class VideoCamera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture('http://192.168.0.14:8090/?action=stream')
        self.cap.set(3, 960) # 영상 가로길이 설정 
        self.cap.set(4, 480) # 영상 세로길이 설정

    def __del__(self):
        self.cap.release()

    def frame(self):
        label = 'Neutral'
        ret, frame = self.cap.read()
        fire = fire_cascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in fire:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = frame[y:y + h, x:x + w]
            roi_color = cv2.resize(roi_color, (224, 224), interpolation=cv2.INTER_AREA)
            if np.sum([roi_color]) != 0:
                roi_c = roi_color.astype('float') / 255.0
                roi_c = img_to_array(roi_c)
                roi_c = np.expand_dims(roi_c, axis=0)

                preds = classifier.predict(roi_c)[0]
                label = class_labels[preds.argmax()]
                label_position = (x, y)
            if label == 'Fire':
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2)
        out.write(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def save(self):
        ret, frame = self.cap.read()
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        out = cv2.VideoWriter('save.avi', fourcc, 25.0, (640, 480))