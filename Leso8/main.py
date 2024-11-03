import cv2
import os 
haar_file = "C:/Users/proho/Desktop/Jetlearn/OpenCV/Leso8/haarcascade_frontalface_default.xml"
datasets = "C:/Users/proho/Desktop/Jetlearn/OpenCV/Leso8/datasets"
subdata = "prohor"

path = os.path.join(datasets, subdata)

if not os.path.isdir(path):
    os.mkdir(path)

#defining the size of images
(width, height) = (130,100)

face_cascade = cv2.CascadeClassifier(haar_file)

cam = cv2.VideoCapture(0)

count = 1

while count <= 30:
    (ret, img) = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #(image, scaleFactor, Min Neighbours)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x + w, y + h), (255,0,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('% s/% s.png' % (path,count), face_resize)
    count += 1

    cv2.imshow('OpenCV', img)
    key = cv2.waitKey(0)
    if key == 27:
        break