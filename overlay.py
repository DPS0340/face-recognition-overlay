import time
import cv2
import math
import face_detection
detector = face_detection.build_detector(
  "DSFDDetector", confidence_threshold=.5, nms_iou_threshold=.3)

resize_factor = 0.25

def get_faces(img):
    detections = detector.detect(img)
    return detections

def face_wrap(image):
    resized_img = cv2.resize(img, (0, 0), fx=resize_factor, fy=resize_factor)
    face_locations = get_faces(resized_img)
    for pos in face_locations:
        for coord in pos:
            coord *= 1/resize_factor
    print(face_locations)
    for pos in face_locations:
        image = process_face(image, pos)
    return image

def process_face(image, pos):
    top, right, bottom, left, _ = pos
    image = cv2.line(image, (left, bottom), (right, bottom), green, thickness=2)
    image = cv2.line(image, (left, top), (right, top), green, thickness=2)
    image = cv2.line(image, (left, bottom), (left, top), green, thickness=2)
    image = cv2.line(image, (right, bottom), (right, top), green, thickness=2)
    return image


if __name__ == '__main__':
    cap = cv2.VideoCapture(0) #open camera
    ret,frame = cap.read() #start streaming
    green = (0, 255, 0)

    while cap.isOpened():
        ret, img = cap.read()
        if ret:
            img = face_wrap(img)
            cv2.imshow("RPI 얼굴인식", img)
            if cv2.waitKey(1) & 0xFF == 27: #esc
                break
        else:
            print('no camera!')
            break
    cap.release()
    cv2.destroyAllWindows()