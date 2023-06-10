import numpy as np
import cv2 as cv

im_w = 720; im_h = 480
img = np.ones((im_h, im_w, 3), dtype = np.uint8)*252
#
color = (255, 0, 0) # Blue color in BGR
thickness = 1; isClosed = False; font = cv2.FONT_HERSHEY_SIMPLEX; fontScale = 0.5
#
upleft = (int(1/8*im_w), int(5/8*im_h))
btmright = (int(7/8*im_w), int(7/8*im_h))
cv2.rectangle(img, upleft, btmright, color, thickness)
#
p1 = [int(2/8*im_w), int(6/8*im_h)]
p2 = [int(3/8*im_w), int(6/8*im_h)]
p3 = [int(5/8*im_w), int(6/8*im_h)]
p4 = [int(6/8*im_w), int(6/8*im_h)]
points = np.array([p1,p2,p3,p4])
points = points.reshape((-1, 1, 2))
cv2.polylines(img, [points], isClosed, color, thickness)
#
cv2.putText(img, 'Left/Right', (int(3.5/8*im_w),int(6/8*im_h)), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow('white image', img)
cv2.waitKey(0)
