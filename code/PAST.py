import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
import glob
import random
import cv2
import os
from skimage.util import random_noise

def ProcessPixel(pix, y, j):
    row = []
    for x in range(0,640):
        row.append(int(pix[x,y]))

    row_mean = np.mean(row)

    data_x = [i for i in range(0,640)]
    data_y = (-((row - row_mean) * j) / 20) + (640 - y)
    return({'x':data_x, 'y':data_y})

def ProcessImage(file_in, j, background_col, lines_col):
    plt.figure(figsize = (12.8,7.2))
    im = Image.open(file_in).convert('L')
    size = 640,360
    im_resized = im.resize(size, Image.LANCZOS)
    pix = im_resized.load()

    for y in range(0,360):
        row = ProcessPixel(pix, y, j)
        plt.plot(row['x'],row['y'],'-', c=lines_col,alpha=1, linewidth = 0.5)

    plt.axis('off')
    out_file = file_in.replace('.png', ''.join(['_',str(j),'_processed.png']))
    plt.savefig(out_file, facecolor=background_col, dpi = 800, bbox_inches='tight')
    plt.close()

def GetPhotos(img_cnt, sub_cnt):
    bckgrd = np.zeros((2160, 3840, 3), dtype = "uint8")
    photo_final = bckgrd.copy()

    photo = cv2.imread('data/journey_photos/' + str(img_cnt) + '_' + str(sub_cnt) + '.JPG')
    if sub_cnt == 2:
        # add noise
        photo = np.asarray(photo) 
        photo = random_noise(photo, mode='gaussian', var=0.25)
        photo = (255*photo).astype(np.uint8)
        # blur
        photo = cv2.blur(photo, (5,5))

    elif sub_cnt == 3:
        # add noise
        photo = np.asarray(photo) 
        photo = random_noise(photo, mode='gaussian', var=0.75)
        photo = (255*photo).astype(np.uint8)
        # blur
        photo = cv2.blur(photo, (10,10))
    h, w = photo.shape[:2]

    if h > w:
        photo = cv2.resize(photo, (1400, 2100), Image.LANCZOS)
        h = 2100
        w = 1400
    else:
        photo = cv2.resize(photo, (3000, 2000), Image.LANCZOS)
        h = 2000
        w = 3000

    # based on: https://stackoverflow.com/questions/58248121/opencv-python-how-to-overlay-an-image-into-the-centre-of-another-image
    center_x = 3840 // 2
    left = np.int64(center_x - (w/2))
    right = np.int64(center_x + (w/2))

    center_y = 2160 // 2
    top = np.int64(center_y + (h/2))
    bottom = np.int64(center_y - (h/2))

    photo_final[bottom:top, left:right] = photo

    return(photo_final)

def CreateVideoFile(video_name):
    # based on https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python
    images = []
    for img in range(1,41):
        n=1
        images.append(''.join(['data/journey/journey',str(img),'_',str(n),'_processed.png']))

    height, width = (2160, 3840)
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    video_frames = cv2.VideoWriter(video_name, fourcc, 0.5, (width, height))

    img_cnt = 1
    img_cnt_2 = 1
    for image in images:
        print(image)        
        img = cv2.imread(image)
        img_resized = cv2.resize(img, (3840, 2160), Image.LANCZOS)
        video_frames.write(img_resized)
        
        if img_cnt < 14:
            print('_'.join([str(img_cnt), str(img_cnt_2)]))
            photo = GetPhotos(img_cnt, img_cnt_2)

            photo_resized = cv2.resize(photo, (3840, 2160), Image.LANCZOS) # just to be sure
            video_frames.write(photo_resized)

            img_cnt_2 += 1
            if img_cnt_2 > 3:
                img_cnt += 1
                img_cnt_2 = 1

    cv2.destroyAllWindows()
    video_frames.release()

def Main():
    image_list = glob.glob('data/journey/*.png')
    palette = open('data/palette.txt').read().split('\n')

    #for i, image in enumerate(image_list):
    #    for j in [1,2,3]:
    #        bck_col = ''
    #        lin_col = ''
    #        while bck_col == lin_col:
    #            bck_col = random.choice(palette)
    #            lin_col = random.choice(palette)
    #        ProcessImage(image, j, bck_col, lin_col)

    CreateVideoFile('identity/journey_video.avi')

Main()



