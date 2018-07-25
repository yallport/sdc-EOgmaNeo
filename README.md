# EOgmaNeo Self-Driving Car
## Powered by Raspberry Pi 3B+ and Arduino 

(Code not yet updated for the new version of EOgmaNeo, stay tuned for updates!)


![Front side](https://github.com/ylustina/sdc-EOgmaNeo/blob/master/docs/front.jpg)



## Table of Contents

[EOgmaNeo Self-Driving Car](#sdc)

[OgmaNeo](#ogma)

- [Feynman Machine](#fm)

- [EOgmaNeo](#eogmaneo) 

[Materials](#materials)

[Installation Instructions](#install)

- [Docker Image for Pi](#docker) 🐋

[Assembly Instructions](#assembly)

[Train and Test](#run) 




---------------


<a name="sdc"/>

## EOgmaNeo Self-Driving Car ##


The program runs on the Pi, and performs all the online machine learning on the Pi's CPU. With the OgmaNeo library, there is no pre-training and no offloading to a more powerful machine. The network learns to predict the next command as you drive it. The car takes video from the camera and the steering angles as input, and uses a predictive hierarchy to predict the next desired steering angle. This greatly lowers the computational cost, as well as saves the time and work necessary for collecting data for other kinds of neural networks. 




<a name="ogma"/>

## OgmaNeo ##

OgmaNeo is online (real-time) learning software. The OgmaNeo library contains implementations of Online Predictive Hierarchies based on the Feynman Machine. 

If you have a machine learning problem that has to do with data changing over time, and the traditional approaches to machine learning don't work, check out OgmaNeo! 




<a name="fm"/>

### Feynman Machine ### 

The Feynman Machine is a brain-inspired sequence prediction algorithm AI architecture for machine learning. It is a network of intercommunicating nonlinear dynamical systems, and each system can adapt to predict its future inputs. While the Feynman Machine is not for beginners due to the combination of hard math, neuroscience, and machine learning, Ogma has done an extraordinary job in packaging their software in a way that is approachable.


If you are interested in the inner workings of the Feynman Machine, read the paper "Feynman Machine: The Universal Dynamical Systems Computer" [here!](https://arxiv.org/abs/1609.03971)





<a name="eogmaneo"/>

### EOgmaNeo ###

[EOgmaNeo](https://github.com/ogmacorp/EOgmaNeo) is Ogma Corp's embedded version of OgmaNeo. For some tasks it is also much faster than OgmaNeo. 

While OgmaNeo can run on large networks and parallel architectures like GPUs, EOgmaNeo runs on the CPU and is optimized for low-powered hardware. 

EOgmaNeo is used for this SDC.




<a name="materials"/>

## Materials ##

- [Raspberry Pi 3B+](https://www.amazon.com/CanaKit-Raspberry-Power-Supply-Listed/dp/B07BC6WH7V/ref=sr_1_3?s=electronics&ie=UTF8&qid=1527881534&sr=1-3&keywords=pi+3B%2B) and [case w/ fan](https://www.amazon.com/gp/product/B01E8YBSDG/ref=oh_aui_detailpage_o07_s03?ie=UTF8&psc=1)

- [Traxxas Rustler Truck](https://www.amazon.com/gp/product/B01EA6QXWS/ref=oh_aui_detailpage_o07_s00?ie=UTF8&psc=1)

- [Traxxas Rustler camera mount](https://www.thingiverse.com/thing:1476904/apps/customize/) .stl file included in this repository.

- [60A Brushed ESC](https://www.amazon.com/gp/product/B00M1SB35U/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)

- [Pi camera](https://www.amazon.com/gp/product/B01ER2SKFS/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1) and [case](https://www.amazon.com/gp/product/B00IJZK66G/ref=oh_aui_detailpage_o07_s01?ie=UTF8&psc=1)

- [Arduino Uno R3](https://www.amazon.com/gp/product/B008GRTSV6/ref=oh_aui_detailpage_o07_s02?ie=UTF8&psc=1) and [case](https://www.amazon.com/gp/product/B00UBT87XM/ref=oh_aui_detailpage_o07_s01?ie=UTF8&psc=1)

- [A to B USB Cable](https://www.amazon.com/gp/product/B00K86MVE4/ref=oh_aui_detailpage_o07_s01?ie=UTF8&psc=1)

- [Anker Power Bank](https://www.amazon.com/gp/product/B0194WDVHI/ref=oh_aui_detailpage_o07_s02?ie=UTF8&psc=1)

- [32GB Memory Card](https://www.amazon.com/gp/product/B06XWN9Q99/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1)

- [Steam Controller w/ Dongle](https://store.steampowered.com/app/353370/Steam_Controller/)



#### Misc: #### 

- [Mounting Tape](https://www.amazon.com/gp/product/B003W0R4PE/ref=oh_aui_detailpage_o07_s01?ie=UTF8&psc=1)

- [Breadboard with Jumper Cables](https://www.amazon.com/gp/product/B073X7GZ1P/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1)

- [Solid Hookup Wire](https://www.amazon.com/gp/product/B008L3QJAS/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1)







<a name="install"/>

## Installation Instructions ##



Walkthrough for the installation process in my Docker container repository [here](https://github.com/ylustina/sdc-docker). 

- Install the Steam controller on the Pi

- Install Docker on the Pi

- Ino build + upload in the Docker container






<a name="docker"/>

### Docker Image for Pi ###

[Docker image repository](https://github.com/ylustina/sdc-docker) for setting up a Raspberry Pi 3 Stretch environment for the EOgmaDrive self-driving car.

[DockerHub link](https://hub.docker.com/r/ylustina/sdc-docker/).







<a name="assembly"/>

## Assembly Instructions ## 

![Top](https://github.com/ylustina/sdc-EOgmaNeo/blob/master/docs/top.jpg)



### Arduino and Breadboard ###



The breadboard is used to multiplex the power and ground pins. There should be 3 in each + and -. The power and the ground cables connected at the breadboard are:

- Arduino

- Steering servo

- Driving servo (back motor)



On the Arduino, here are the corresponding digital connections: 

- Digital 2: Driving Servo

- Digital 3: Steering Servo

If you want, you can change the assignment in the [.ino file](https://github.com/ylustina/sdc-EOgmaNeo/blob/master/self-driving%20car/drive/src/SDC_controller_norf.ino).

The 2 remaining cables:

- Red goes into 5V on the Arduino

- Black goes into ground on the Arduino



![Wiring](https://github.com/ylustina/sdc-EOgmaNeo/blob/master/docs/wires.jpg)

![Arduino side](https://github.com/ylustina/sdc-EOgmaNeo/blob/master/docs/arduino-side.jpg)



### Steam Controller ### 

The Steam controller dongle is directly plugged into the Pi. Steam controller installation instructions [here](https://github.com/ylustina/sdc-docker#controller) in my Docker repository, or [here](https://github.com/ynsta/steamcontroller), from the driver repo. 


#### Important! #### 

Push a button on the controller on reboot and after starting the daemon!



### Traxxas Truck ### 

I replaced the stock ESC with the [Dynamite Brushed ESC](https://www.amazon.com/gp/product/B00M1SB35U/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1) because the one that comes with the car makes the car stutter randomly.

I couldn't get all the materials to fit under the truck case, so I ended up with a cable monster. You try it! Good luck!



### Camera ### 

The camera is mounted to the front of the truck.


To test if the camera works:

    from picamera import PiCamera
    camera = PiCamera()
    camera.capture('image.jpg') 
    

I used [this mount](https://github.com/ylustina/sdc-EOgmaNeo/blob/master/rustler_mount.stl) to mount the camera for the Raspberry Pi to the truck. It doesn't perfectly slide onto the truck, and is made for the GoPro, but with some epoxy, it got the job done. Please let me know if you find something better!




<a name="run"/>


## Train and Test

If you are using my Docker container, here are the instructions:

- Connect all wires

- Wait for the Pi to start

- Pi will be looking for the controller, press a button for them to connect. After the controller is connected, you should be good to go!


To train the SDC, just drive it around for a bit. The button A switches between training and self-driving mode. 








----------------


## Ogma License and Copyright ##

[OgmaCorp](https://github.com/ogmacorp)

The work in this repository is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. See the EOGMADRIVE_LICENSE.md and LICENSE.md file for further information. Contact Ogma via licenses@ogmacorp.com to discuss commercial use and licensing options.

EOgmaDrive Copyright (c) 2017 Ogma Intelligent Systems Corp. All rights reserved.



