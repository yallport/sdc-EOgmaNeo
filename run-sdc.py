import time
import os


while True:
    if 'js0' in os.listdir('/dev/input'):
        break
    else:
        time.sleep(1)

os.system('docker run -ti --privileged \
	-e DISPLAY=$DISPLAY \
	-v /tmp/.X11-unix:/tmp/.X11-unix:ro \
	-v /home/pi/shared-with-docker/:/root/ \
	-p 8888:8888 \
	ylustina/sdc-docker:latest python3 /root/sdc-EOgmaNeo/self-driving\ car/pi_sdc.py')
