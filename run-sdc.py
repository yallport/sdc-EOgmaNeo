import time
import os
import logging

logging.basicConfig(filename='/home/pi/run-sdc.log',level=logging.DEBUG)

logging.debug('checking for joystick')

while True:
    if 'js0' in os.listdir('/dev/input'):
        logging.debug('joystick found!')
        break
    else:
        logging.debug('no joystick found!')
        time.sleep(1)

logging.debug('running container...')
os.system('docker run -ti --privileged \
	-e DISPLAY=$DISPLAY \
	-v /tmp/.X11-unix:/tmp/.X11-unix:ro \
	-v /home/pi/shared-with-docker/:/root/ \
	-p 8888:8888 \
	ylustina/sdc-docker:latest python3 /root/sdc-EOgmaNeo/self-driving\ car/pi_sdc.py')

