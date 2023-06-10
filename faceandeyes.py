import cv2 as cv
def detectAndDisplay(frame):
 frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 frame_gray = cv.equalizeHist(frame_gray)
 #-- Detect faces
 faces = face_cascade.detectMultiScale(frame_gray)
 for (x,y,w,h) in faces:
     frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
     faceROI = frame_gray[y:y+h,x:x+w]
     #-- In each face, detect eyes
     eyes = eyes_cascade.detectMultiScale(faceROI)
     for (x2,y2,w2,h2) in eyes:
         eye_center = (x + x2 + w2//2, y + y2 + h2//2)
         radius = int(round((w2 + h2)*0.25))
         frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
 cv.imshow('Capture - Face detection', frame)
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
#-- 1. Load the cascades
face_cascade.load(cv.samples.findFile('data\\haar\\haarcascade_frontalface_alt.xml'))
eyes_cascade.load(cv.samples.findFile('data\\haar\\haarcascade_eye_tree_eyeglasses.xml'))
#-- 2. Read the video stream
cap = cv.VideoCapture(0) #device webcam no.0
while cap.isOpened():
 ret, frame = cap.read()
 if not ret:
    print("webcam tidak ditemukan ...")
    break
 detectAndDisplay(frame)
 if cv.waitKey(1) == ord('q'): #tekan q untuk quit
    break
cap.release()
cv.destroyAllWindows()