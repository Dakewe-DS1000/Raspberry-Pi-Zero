from picamera import PiCamera
from time import sleep

camera = PiCamera()

for i in range(0, 100):
    save_file_name = "../Pictures/captureImage_" + str(i) + ".jpg"
    camera.capture(save_file_name)
    sleep(2)
    print("Captured Image {0}".format(i))

