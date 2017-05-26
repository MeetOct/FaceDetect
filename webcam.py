import cv2
import sys
import skvideo.io
import time

cascPath = sys.argv[2]
#videoPath =sys.argv[1]
imagePath=sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

#video_capture = skvideo.io.VideoCapture(videoPath)
video_capture = cv2.VideoCapture(0)	
#video_capture.open()
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
   
    if not ret:
	print 'capture failed'
	break
    frame=cv2.flip(frame,0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(20, 20),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces

    if len(faces)<=0:
	continue
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
    # Display the resulting frame
    cv2.imshow('Video', frame)
    cv2.imwrite(imagePath+time.strftime("%Y%m%d%H%M%S", time.localtime())+'.jpg',frame)
    break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
