

import cv2
import sys

imgPath=sys.argv[1]
cascPath=sys.argv[2]

face_cascade=cv2.CascadeClassifier(cascPath)
image=cv2.imread(imgPath)

gary=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(
gary,
scaleFactor=1.2,
minNeighbors=3,
minSize=(20,20),
flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "FOUND {0} faces".format(len(faces))

for (x,y,w,h) in faces:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)

cv2.imshow("faces found",image)
cv2.waitKey(0)
