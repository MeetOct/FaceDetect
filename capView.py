

from time import sleep
from picamera import PiCamera

with PiCamera() as camera:
	camera.resolution = (320, 240)
	camera.start_preview()
	sleep(10)

camera.close()
