import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
import glob

def ProcessPixel(pix, y):
    row = []
    for x in range(0,400):
        row.append(int(pix[x,y]))

    row_mean = np.mean(row)

    data_x = [i for i in range(0,400)]
    data_y = (-(row - row_mean) / 20) + (400 - y)
    return({'x':data_x, 'y':data_y})

def ProcessImage(file, background_col, lines_col):
    plt.figure(figsize = (10,10))
    im = Image.open(file).convert('L')
    size = 400,400
    im_resized = im.resize(size, Image.LANCZOS)
    pix = im_resized.load()

    for y in range(0,400):
        
        row = ProcessPixel(pix, y)
        plt.plot(row['x'],row['y'],'-', c=lines_col,alpha=1, linewidth = 0.5)

    plt.axis('off')
    out_file = file.split('/')[-1].replace('.png', '_processed.png')
    plt.savefig(f'identity/{out_file}', facecolor=background_col, dpi = 1000, bbox_inches='tight')

def Main():
    image_list = glob.glob('data/locations/*.png')
    palette = open('data/palette.txt').read().split('\n')

    for i, image in enumerate(image_list):
        if i == 0:
            background_colour = palette[0]
            lines_colour = palette[1]
        else:
            background_colour = palette[1]
            lines_colour = palette[int(np.floor(i//2)) + 2]
        
        ProcessImage(image, background_colour, lines_colour)

Main()



