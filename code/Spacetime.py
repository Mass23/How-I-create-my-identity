import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
import numpy as np
import pandas as pd
import glob
import random
import cv2
import os

palette = open('data/palette.txt').read().split('\n')

def PlotEpoch(df, name, glitch):
    grouped = df.groupby('ID')

    # Create a new figure
    fig, ax = plt.subplots(figsize=(12.8,7.2))
    plt.rcParams["font.family"] = "Arial"

    back_col = palette[0]
    line_col = palette[1]
    glitch_back_col = random.choice(palette[2:4])
    glitch_line_col = glitch_back_col
    while glitch_line_col == glitch_back_col:
        glitch_line_col = random.choice(palette[2:4])

    # Iterate through groups and plot lines
    for group_id, group_data in grouped:
        past_group = group_data[group_data['epoch'] <= 10]
        future_group = group_data[group_data['epoch'] >= 10]
        if glitch == True:
            plt.plot(past_group['Time'], past_group['Space'], '-', color = glitch_line_col, lw = 3.5)
            plt.plot(future_group['Time'], future_group['Space'], '--', color = glitch_line_col, lw = 3.5)
        elif name.endswith('10'): # if the 10th epoch, change colours
            plt.plot(past_group['Time'], past_group['Space'], '-', color = back_col, lw = 3.5)
            plt.plot(future_group['Time'], future_group['Space'], '--', color = back_col, lw = 3.5)
        else:
            plt.plot(past_group['Time'], past_group['Space'], '-', color = line_col, lw = 3.5)
            plt.plot(future_group['Time'], future_group['Space'], '--', color = line_col, lw = 3.5)

    # Add labels and title
    if glitch == True:
        ax.set_facecolor(glitch_back_col)
        ax.spines['bottom'].set_color(glitch_line_col)
        ax.spines['top'].set_color(glitch_back_col) 
        ax.spines['right'].set_color(glitch_back_col)
        ax.spines['left'].set_color(glitch_line_col)
        ax.yaxis.label.set_color(glitch_line_col)
        ax.xaxis.label.set_color(glitch_line_col)

    elif name.endswith('10'):
        ax.set_facecolor(line_col)
        ax.spines['bottom'].set_color(back_col)
        ax.spines['top'].set_color(line_col) 
        ax.spines['right'].set_color(line_col)
        ax.spines['left'].set_color(back_col)
        ax.yaxis.label.set_color(back_col)
        ax.xaxis.label.set_color(back_col)

    else:
        ax.set_facecolor(back_col)
        ax.spines['bottom'].set_color(line_col)
        ax.spines['top'].set_color(back_col) 
        ax.spines['right'].set_color(back_col)
        ax.spines['left'].set_color(line_col)
        ax.yaxis.label.set_color(line_col)
        ax.xaxis.label.set_color(line_col)
    
    plt.xlabel('TIME', weight='bold', style='italic', size = 15)
    plt.ylabel('SPACE', weight='bold', style='italic', size = 15)
    plt.xticks([])
    plt.yticks([])  
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    ax.set_aspect('equal')

    if glitch == True:
        plt.savefig(''.join(['data/spacetime/st_', name, '.png']), facecolor=glitch_back_col, dpi = 800)
    elif name.endswith('10'):
        plt.savefig(''.join(['data/spacetime/st_', name, '.png']), facecolor=palette[1], dpi = 800)
    else:
        plt.savefig(''.join(['data/spacetime/st_', name, '.png']), facecolor=palette[0], dpi = 800)
    plt.close()

def CreateIdentities(name):
    past_df = []
    for id in range(1, 11):
        intercept_axis = random.choice(['Time','Space'])
        slope = random.uniform(0.5,1)
        if intercept_axis == 'Time':
            past_df.extend([[str(id), i, i*slope, ((i+1)*10)+1] for i in [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1]])
        else:
            past_df.extend([[str(id), i/slope/2, i, ((i+1)*10)+1] for i in [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1]])
        past_df.extend([[str(id),0,0,10]])
    past_df = pd.DataFrame(past_df, columns=['ID', 'Space', 'Time', 'epoch'])

    future_table = []
    for id in range(1, 11):
        future_table.extend([[str(id),0,0,10]])
        for epoch in range(11,31):
            if epoch == 11:
                curr_time = random.uniform(0, 0.05)
                curr_space = random.uniform(0, 0.05)
            else:
                curr_time = curr_time + random.uniform(0, 0.5*curr_time)
                curr_space = curr_space + random.uniform(0, 0.5*curr_space)
            future_table.extend([[str(id), curr_space, curr_time, epoch]])
    future_df = pd.DataFrame(future_table, columns=['ID', 'Space', 'Time', 'epoch'])
    df = pd.concat([past_df, future_df])

    for epoch in range(1,31):
        if (epoch % 2) != 0:
            glitch = random.random() < 0.1
        PlotEpoch(df[df['epoch'] <= epoch], name + '_' + str(epoch), glitch)

def Main():
    #os.mkdir('data/spacetime')
    universes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','n','o','p','q']
    images = []
    for universe in universes:
        #CreateIdentities(universe)
        for epoch in range(1,31):
            images.append('data/spacetime/st_' + universe + '_' + str(epoch) + '.png')
    
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    video_frames = cv2.VideoWriter('identity/spacetime.avi', fourcc, 6, (width,height))
    for image in images:
        img = cv2.imread(image)
        video_frames.write(img)

    cv2.destroyAllWindows()
    video_frames.release()
    
Main()
