import cv2 as cv
cap = cv.VideoCapture(0)  # device webcam no.0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("webcam tidak ditemukan ...")
        break
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):  # tekan q untuk quit
        break
cap.release()
cv.destroyAllWindows()
