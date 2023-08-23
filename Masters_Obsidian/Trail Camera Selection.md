---
author: Kyle Nessen
created: August 20th, 2023
---
# Trail Camera Selection Rationale

## Background
During the overwintering season, I plan to use a combination of trail cameras and wind data loggers to make repeated and high frequency observations of the monarch clusters. The goal here is to correlate presence/absence data of the clusters with wind conditions.

The image below shows a basic diagram of my proposed setup. Essentially a long pole will lift a camera and wind data logger to the same height as the monarchs. I will then use a modified trail camera that takes photos in near-infrared (NIR) to take photos at some interval (e.g. every 10 mins). The purpose of using NIR imagery is based off the observation that monarch clusters have high contrast in this wavelength compared to the vegetation that they are found in (Hirstov et. al. 2019). 

- add in temperature and RH
![[camera_monitoring_setup.png]]

## Modifying Camera Traps to NIR
Camera traps are ideal for this application because of a few key characteristics:
1. They are purpose built to withstand environmental conditions for extended periods of time.
2. Many have data logger features built in (timelapse mode).
3. Can be purchased to transmit photos over cellular networks.
4. Easily convertible to NIR. 

I want to focus on the last point in this section. All modern digital camera sensors can detect NIR light, a feature camera traps exploit. Within the camera module of these systems is small mechanical switch, that can move an IR cut filter in front or away from the lens. This allows the system to take normal color photos during the day (removing any NIR light), while still being able to use NIR LEDs to illuminate the scene at night (with the cut filter moved out of the way).

This is a big advantage, because the IR cut filter can be removed fairly easily. unlike most cameras which have the filter glued directly to the sensor. It can then be replaced with an "IR Pass" filter that, as it sounds, allows IR light to pass but not visible. 

Without going into too much detail, I was able to modify one my existing Camera Traps for this purpose. I used a Roscolux filter ( #382 "Congo Blue") as a make shift IR Pass filter, because of it's low vis and high NIR transmission (image below).
![[roscolux_congo_blue.jpg]]

Below are some photos showing some of the modifications I did. 

This image is of the camera module within the unit. Adjusting focus is straightforward, simply turn the lens till the image is in focus. They glue the threads at the factory to keep the focus, but it is easy to breakthrough.

Readjusting the focus is necessary, as the removal of the ir filter causes the images to be blurry initially. 
![[IMG_5306.jpeg]]

Here I have taken the lens off the sensor. The rectangle in the center is where the IR filter was. I simply removed it by breaking the glass and taking out the fragments with tweezers. 
![[IMG_5307.jpeg]]

Here I'm showing the "congo blue" filter that I put in front of the lens so I can get the NIR light to predominately shine through. Obviously, some blue light also gets through, polluting the image. Proper IR cut filters exist that we can purchase for this purpose. 
![[IMG_5311.jpeg]]

### Testing modified camera in a monarch grove

On Francis' recommendation, I tested the modified trail camera in a eucalyptus grove. His concern was that foggy conditions might affect the how bright the leaves will appear in the image. 

Below are two images to find this out. I set the cameras out in a monarch grove (Site 3090) looking straight up. 

The first image taken under clear sunny conditions. The leaves are bright, as expected, while the sky is dark in the NIR band.
![[NIR_looking_up_sunny.jpg]]


The second image is taken around dawn the next day. The bright clouds affects the exposure value, causing the leaves and branches to be underexposed. This *could* potentially lower our ability to detect clusters, but might be easy to overcome with some exposure compensation. Hard to say until we have monarchs to photograph.
![[NIR_looking_up_cloudy.jpg]]

# Pole design
In my figure at the beginning of the document, I show a pole on a tripod, but after some research, I've opted for a guy line approach. 

Why I like this approach is that it allows for a secure pole design that is flexible in the field to setup. It can be used with any long poles, including some that we have on hand, or any long extending pole. 

I did a test with some string found that it worked well. It was important that it was anchored at the very top to minimize movement. While I didn't have strong winds, it seems pretty robust. 
![[IMG_5284.jpeg]]

# Potential Cameras
## Basic Cameras
### Meidase P200
https://amzn.to/3OGbvet
**Cost**: 90-130
![[Pasted image 20230821131205.png]]

#### Pros
- High quality camera
- Has built in wifi, allows for aiming while extended on pole
- No monthly costs
#### Cons
- No cellular connection
- No back 1/4 thread (only bottom)

## Cellular Cameras
### SPYPOINT Flex G-36
https://amzn.to/3KRiUGu
**Cost**: 100-120
![[Pasted image 20230821131911.png]]
#### Pros
- A free tier for cellular connection (100 pics/mon)
#### Cons
- Poor customer support.
- Hard to preview photos if no service is available (not designed to be so high)

### Moultrie Mobile Edge
https://amzn.to/3snF50Q
**Cost**: 70
**Cellular**: $650 for five months unlimited images

![[Pasted image 20230821132250.png]]

#### Pros
- Relatively cheap
- Well reviewed
- Can work on both Verzion and ATT
- Smart antennae design for transport
#### Cons
- No ability to use SD cards
