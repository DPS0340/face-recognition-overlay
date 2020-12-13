import time
import cv2
import math
import face_detection
from threading import Thread

detector = face_detection.build_detector(
  "DSFDDetector", confidence_threshold=.5, nms_iou_threshold=.3)

resize_factor = 0.1
green = (0, 255, 0)
face_locations = []

def get_faces(img):
    detections = detector.detect(img)
    return detections


def find_faces(image):
    global face_locations
    resized_img = cv2.resize(img, (0, 0), fx=resize_factor, fy=resize_factor)
    face_locations = get_faces(resized_img)
    for pos in face_locations:
        for i in range(4):
            pos[i] *= 1/resize_factor
    print(face_locations)

def show_face(image):
    for pos in face_locations:
        image = process_face(image, pos)
    return image

def process_face(image, pos):
    left, bottom, right, top, _ = pos
    image = cv2.line(image, (left, bottom), (right, bottom), green, 2)
    image = cv2.line(image, (left, top), (right, top), green, 2)
    image = cv2.line(image, (left, bottom), (left, top), green, 2)
    image = cv2.line(image, (right, bottom), (right, top), green, 2)
    return image

cnt = 0

if __name__ == '__main__':
    cap = cv2.VideoCapture(0) #open camera
    ret,frame = cap.read() #start streaming

    while cap.isOpened():
        cnt += 1
        ret, img = cap.read()
        if ret:
            if cnt >= 50:
                t = Thread(target=find_faces, args=(img))
                t.start()
                face_wrap(img)
                cnt = 0
            img = show_face(img)
            cv2.imshow("RPI 얼굴인식", img)
            if cv2.waitKey(1) & 0xFF == 27: #esc
                break
        else:
            print('no camera!')
            break
    cap.release()
    cv2.destroyAllWindows()
