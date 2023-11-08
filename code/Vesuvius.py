import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
import glob
import random
import cv2
import os
from skimage.util import random_noise

def ProcessFrame(frame):
    frame = np.asarray(frame)
    gaussian_var = np.random.poisson(1, 1)[0] / 20
    frame = random_noise(frame, mode='gaussian', var=gaussian_var)
    frame_final = (255*frame).astype(np.uint8)
    return(frame_final)

def ProcessVideo(video_name):
    # create VideoCapture object: adapted from https://debuggercafe.com/image-and-video-blurring-using-opencv-and-python/
    cap = cv2.VideoCapture(video_name)
    if (cap.isOpened() == False):
        print('Error while trying to open video. Plese check again...')
    # get the frame width and height

    # define codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter(video_name.replace('.MOV', '_processed.MOV'), fourcc, 30, (1920, 1080))

    # read until end of video
    while(cap.isOpened()):
        # capture each frame of the video
        ret, frame = cap.read()
        if ret == True:
            # add gaussian blurring to frame
            processed_frame = ProcessFrame(frame)
            # save video frame
            out.write(processed_frame)
            # press `q` to exit
            if cv2.waitKey(27) & 0xFF == ord('q'):
                break
        # if no frame found
        else:
            break
    out.release()
    cv2.destroyAllWindows()

def Main():
    files = glob.glob('data/vesuvius/*.MOV')
    for file in files:
        print(file)
        ProcessVideo(file)

Main()
