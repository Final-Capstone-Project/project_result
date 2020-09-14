from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np


fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
classifier = load_model('fire_mobilNet.h5')

class_labels = ['Fire', 'Neutral']

cap = cv2.VideoCapture('./data/test1.mp4')
# cap = cv2.VideoCapture(0)

cnt = 0

label = 'Neutral'

while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)  # 48
        roi_color = frame[y:y + h, x:x + w]
        roi_color = cv2.resize(roi_color, (224, 224), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            roi_c = roi_color.astype('float') / 255.0
            roi_c = img_to_array(roi_c)
            roi_c = np.expand_dims(roi_c, axis=0)

            preds = classifier.predict(roi_c)[0]
            label = class_labels[preds.argmax()]
            label_position = (x, y)

    if label == 'Fire':
        cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2)
    else:
        cv2.putText(frame, label, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
