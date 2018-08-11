from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera(resolution=(3280, 2464))
camera.start_preview()
sleep(2)

#camera.capture_sequence(["../Pictures/image%03d.jpg" % i for i in range(100)])

for i in range(13*60/5):
    now = datetime.datetime.now()
    str_date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    str_time = str(now.hour) + "-" + str(now.minute) + "-" + str(now.second)
    str_save_file_name = "../Pictures/image_" + str_date + "_" + str_time + ".jpg"
    camera.capture(str_save_file_name, resize=(320, 240))
    print("Captured @ {0} - {1}".format(str_date, str_time))
    sleep(5 * 60)
camera.close()
