#!/usr/bin/env python
# coding: utf-8


from PIL import Image, ImageDraw,ImageFont
import math
import os
import json
import numpy as np
from IPython.display import display
import pandas as pd
import shutil
import random




def get_coords(x, y, angle, imwidth, imheight):

    #x1_length = (x-imwidth) / math.cos(angle)
    #y1_length = (y-imheight) / math.sin(angle)
    length =  y-50
    endx1 = x + length * math.cos(math.radians(angle))/math.sin(math.radians(angle))
    endy1 = 50

    #x2_length = (x-imwidth) / math.cos(angle)
    #y2_length = (y-imheight) / math.sin(angle+18)
    length = 50
    endx2 = x - length * math.cos(math.radians(angle))/math.sin(math.radians(angle))
    endy2 = imheight-50

    return [(endx1, endy1), (endx2, endy2)]#, [x1, x2]



def text_position(angle_type, angle, position=3, parallel_line='horizontal'):
    #print(angle_type, angle, position)
    if parallel_line=='horizontal':
        if position==1:
            #pos_a = (max(points[0][0]-80, 80), points[0][1]+70)
            ang = list(np.arange(150, 29, -1))
            y = list(range(90,211))
            ind = ang.index(angle)
            pos_a = (y[ind], 130)
            if angle_type == 'vertically_opposite':
                #done
                
                pos_b = (y[ind] +65, 170)
            if angle_type == 'corresponding':    
                #done
                y = list(np.arange(171, 140, -1))
                print("ind<len(y) ", ind<len(y))
                pos_b = (y[ind] if ind<len(y) else 130, 230)
            
            if angle_type == 'alternate_exterior':
                #if angle<90:
                 #   pos_b = (min(points[0][1]+90,215), 260)#(max(points[0][0]-30, 230), 270)
                #else:
                 #   pos_b = (max(points[0][1]+60, 220), 260)
                y = list(np.arange(280, 200, -1))
                print("ind<len(y) ", ind<len(y))
                pos_b = (y[ind] if ind<len(y) else 200, 260)
        if position==3:
            ang = list(np.arange(150, 29, -1))
            y = list(range(80,201))
            ind = ang.index(angle)
            pos_a = (max(110, y[ind]), 155)
            if angle_type == 'alternate_interior':
                y = list(np.arange(220, 200, -1))
                print("ind<len(y) ", ind<len(y))
                pos_b = (y[ind] if ind<len(y) else 220, 230)
            if angle_type == 'linear':
                #y = list(np.arange(200, 200, -1))
                #print("ind<len(y) ", ind<len(y))
                pos_b = (y[ind] +70, 155)
            if angle_type == 'corresponding':
                y = list(np.arange(181, 130, -1))
                print("ind<len(y) ", ind<len(y))
                pos_b = (y[ind] if ind<len(y) else 125, 255)
            if angle_type == 'vertically_opposite':
                #done
                pos_b = (y[ind] +75, 130)
        if position==4:
            ang = list(np.arange(150, 29, -1))
            y = list(range(150,271))
            ind = ang.index(angle)
            pos_a = (max(90, y[ind]), 155)
            if angle_type == "co_interior":
                y = list(np.arange(241, 210, -1))
                print("ind<len(y) ", ind<len(y))
                pos_b = (y[ind] if ind<len(y) else 210, 230)
    if parallel_line == 'vertical':
        if position==1:
            ang = list(np.arange(150, 29, -1))
            y = list(range(100,221))
            ind = ang.index(angle)
            pos_a = (270, y[ind])
            if angle_type == 'vertically_opposite':
                #done
                #y = list(range(165, 271))
               # y = list(np.arange(210, 180, -1))
                #print("ind<len(y) ", ind<len(y))
                #print(len(y))
                pos_b = (230, y[ind] +85)
            if angle_type == 'corresponding':
                #done
                #y = list(range(185, 291))
                #print(ind if ind< len(y) else 279)
                #print(len(y))
                y = list(np.arange(205, 110, -1))
                pos_b = (160, y[ind] if ind<len(y) else 120)
            if angle_type == 'alternate_exterior':
                y = list(np.arange(271, 190, -1))
                print("ind<len(y) ", ind<len(y))
                pos_b = (130, y[ind] if ind<len(y) else 200)  
        if position==3:
            ang = list(np.arange(150, 29, -1))
            y = list(range(80,201))
            ind = ang.index(angle)
            pos_a = (230, max(150, y[ind]))
            if angle_type == 'alternate_interior':
                y = list(np.arange(255, 200, -1))
                print("ind<len(y) ", ind<len(y))
                pos_b = (160, y[ind] if ind<len(y) else 210)
            if angle_type == 'linear':
                #y = list(np.arange(200, 200, -1))
                #print("ind<len(y) ", ind<len(y))
                pos_b = (230, min(y[ind] +110,235))
            if angle_type == 'corresponding':
                y = list(np.arange(220, 110, -1))
                print("ind<len(y) ", ind<len(y))
                pos_b = (130, y[ind] if ind<len(y) else 100)
            if angle_type == 'vertically_opposite':
                #done
                #y = list(range(165, 271))
                #y = list(np.arange(180, 10, -1))
                #print("ind<len(y) ", ind<len(y))
                #print(len(y))
                pos_b = (270, y[ind] +85)#y[ind] if ind< len(y) else 265)
        if position==4:
            ang = list(np.arange(150, 29, -1))
            y = list(range(140,270))
            ind = ang.index(angle)
            pos_a = (230, max(200, y[ind]))
            if angle_type == "co_interior":
                y = list(np.arange(235, 210, -1))
                print("ind<len(y) ", ind<len(y))
                pos_b = (160, y[ind] if ind<len(y) else 210)
    return pos_a, pos_b



def create_square_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    font = ImageFont.load_default(13)
    draw.line(((150, 150), (150, 150), (250,150) ), fill=fill, width=2)
    #draw.text((50, 160), 'L1', font=font, fill=(0, 0, 0))
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    draw.text((140, 140), 'P', font=font, fill=(0, 0, 0))
    draw.text((260, 140), 'Q', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (200, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((150, 250), (200, 250), (250,250)), fill=fill, width=2)
        draw.line(((150, 150), (150, 250), (150,250)), fill=fill, width=2)
        draw.line(((250, 150), (250, 250), (250,250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((140, 260), 'S', font=font, fill=(0, 0, 0))
        draw.text((260, 260), 'R', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (150, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((150, 250), (200, 250), (250,250)), fill=fill, width=2)
        draw.line(((150, 150), (150, 250), (150, 250)), fill=fill, width=2)
        draw.line(((250, 150), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((140, 260), 'S', font=font, fill=(0, 0, 0))
        draw.text((260, 260), 'R', font=font, fill=(0, 0, 0))
    #print(points)
    draw.line(points, fill=fill, width=2)
    #font = ImageFont.load_default()
    
    #draw.line(points, fill=fill)


def get_vertical_coords(x, y, angle, imwidth, imheight):

    #x1_length = (x-imwidth) / math.cos(angle)
    #y1_length = (y-imheight) / math.sin(angle)
    length = x- 50
    #endy1= y  + length * math.cos(math.radians(angle))/math.sin(math.radians(angle))
    endx1 =  50
    endy1 = y#-length
    #if 90-angle!=0:
    endy1 = y-length * math.cos(math.radians(angle))/math.sin(math.radians(angle))

    #x2_length = (x-imwidth) / math.cos(angle)
    #y2_length = (y-imheight) / math.sin(angle+18)
    length = 50
    endx2 = imwidth - 50#x - length * math.cos(math.radians(angle))/math.sin(math.radians(angle))
    #endy2 = y#+length
    #if 90-angle!=0:
    endy2 = y+length * math.cos(math.radians(angle))/math.sin(math.radians(angle))#imwidth-50

    return [(endx1, endy1), (endx2, endy2)]#, [x1, x2]



def create_rotate90_square_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    draw.line(((150, 150), (150, 150), (150, 250) ), fill=fill, width=2)
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    font = ImageFont.load_default(13)
    #draw.text((130, 50), 'L2', font=font, fill=(0, 0, 0))
    draw.text((140, 140), 'S', font=font, fill=(0, 0, 0))
    draw.text((260, 140), 'P', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (100, 200)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((250, 150), (250, 200), (250, 250)), fill=fill, width=2)
        draw.line(((150, 250), (250, 250), (250, 250)), fill=fill, width=2)
        draw.line(((150, 150), (250, 150), (250, 150)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (170, 250)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((250, 150), (250, 200), (250, 250)), fill=fill, width=2)
        draw.line(((150, 250), (250, 250), (250, 250)), fill=fill, width=2)
        draw.line(((150, 150), (250, 150), (250, 150)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
        
    #print(points)
    draw.line(points, fill=fill, width=2)
    #font = ImageFont.load_default()
    #draw.text((ref_point[0], ref_point[1]), 'A', font=font, fill=(0, 0, 0))
    #draw.line(points, fill=fill)



def create_rectangle_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    font = ImageFont.load_default(13)
    draw.line(((100, 150), (150, 150), (250,150) ), fill=fill, width=2)
    #draw.text((50, 160), 'L1', font=font, fill=(0, 0, 0))
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    draw.text((90, 140), 'P', font=font, fill=(0, 0, 0))
    draw.text((260, 140), 'Q', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (200, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((100, 250), (200, 250), (250,250)), fill=fill, width=2)
        draw.line(((100, 150), (100, 250), (100,250)), fill=fill, width=2)
        draw.line(((250, 150), (250, 250), (250,250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((90, 260), 'S', font=font, fill=(0, 0, 0))
        draw.text((260, 260), 'R', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (150, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((100, 250), (200, 250), (250,250)), fill=fill, width=2)
        draw.line(((100, 150), (100, 250), (100, 250)), fill=fill, width=2)
        draw.line(((250, 150), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((90, 260), 'S', font=font, fill=(0, 0, 0))
        draw.text((260, 260), 'R', font=font, fill=(0, 0, 0))
    #print(points)
    draw.line(points, fill=fill, width=2)
    #font = ImageFont.load_default()
    
    #draw.line(points, fill=fill)

def create_rotate90_rectangle_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    draw.line(((150, 100), (150, 150), (150, 250) ), fill=fill, width=2)
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    font = ImageFont.load_default(13)
    #draw.text((130, 50), 'L2', font=font, fill=(0, 0, 0))
    draw.text((140, 90), 'S', font=font, fill=(0, 0, 0))
    draw.text((260, 90), 'P', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (100, 200)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((250, 100), (250, 200), (250, 250)), fill=fill, width=2)
        draw.line(((150, 250), (250, 250), (250, 250)), fill=fill, width=2)
        draw.line(((150, 100), (250, 100), (250, 100)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (170, 250)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((250, 100), (250, 200), (250, 250)), fill=fill, width=2)
        draw.line(((150, 250), (250, 250), (250, 250)), fill=fill, width=2)
        draw.line(((150, 100), (250, 100), (250, 100)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
        
    #print(points)
    draw.line(points, fill=fill, width=2)
    #font = ImageFont.load_default()
    #draw.text((ref_point[0], ref_point[1]), 'A', font=font, fill=(0, 0, 0))
    #draw.line(points, fill=fill)


# In[10]:


def create_trapezoid_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    font = ImageFont.load_default(13)
    draw.line(((150, 150), (150, 150), (270,150)), fill=fill, width=2)
    #draw.text((50, 160), 'L1', font=font, fill=(0, 0, 0))
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    draw.text((140, 140), 'P', font=font, fill=(0, 0, 0))
    draw.text((280, 130), 'Q', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (200, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((100, 250), (200, 250), (350, 250)), fill=fill, width=2)
        draw.line(((150, 150), (100, 250), (100, 250)), fill=fill, width=2)
        draw.line(((270, 150), (350, 250), (350, 250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((90, 260), 'S', font=font, fill=(0, 0, 0))
        draw.text((360, 260), 'R', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (150, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((100, 250), (200, 250), (350, 250)), fill=fill, width=2)
        draw.line(((150, 150), (100, 250), (100, 250)), fill=fill, width=2)
        draw.line(((270, 150), (350, 250), (350, 250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((90, 260), 'S', font=font, fill=(0, 0, 0))
        draw.text((360, 260), 'R', font=font, fill=(0, 0, 0))
    #print(points)
    draw.line(points, fill=fill, width=2)
    #font = ImageFont.load_default()
    
    #draw.line(points, fill=fill)

def create_rotate90_trapezoid_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    draw.line(((150, 100), (150, 150), (150, 350) ), fill=fill, width=2)
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    font = ImageFont.load_default(13)
    #draw.text((130, 50), 'L2', font=font, fill=(0, 0, 0))
    draw.text((140, 90), 'S', font=font, fill=(0, 0, 0))
    draw.text((260, 140), 'P', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (100, 200)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((250, 150), (250, 200), (250, 250)), fill=fill, width=2)
        draw.line(((150, 350), (250, 250), (250, 250)), fill=fill, width=2)
        draw.line(((150, 100), (250, 150), (250, 150)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((140, 350), 'R', font=font, fill=(0, 0, 0))
        draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (170, 250)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((250, 150), (250, 200), (250, 250)), fill=fill, width=2)
        draw.line(((150, 350), (250, 250), (250, 250)), fill=fill, width=2)
        draw.line(((150, 100), (250, 150), (250, 150)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.text((140, 350), 'R', font=font, fill=(0, 0, 0))
        draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
        
    #print(points)
    draw.line(points, fill=fill, width=2)
    #font = ImageFont.load_default()
    #draw.text((ref_point[0], ref_point[1]), 'A', font=font, fill=(0, 0, 0))
    #draw.line(points, fill=fill)


# In[11]:


def create_hexagon_line(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a rotated hexagon centered at `center`."""
    angle1 = 45
    font = ImageFont.load_default(13)

    points = [
        (center[0] + size * math.cos(math.radians(angle1 + offset)),
         center[1] + size * math.sin(math.radians(angle1 + offset)))
        for offset in range(-45, 305, 60)  # Hexagon has 6 sides, 60 degrees apart
    ]
    draw.polygon(points, outline=fill, width=2)
    #print(points)
    draw.text((points[0][0]+10, points[0][1]), 'W', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]-10, points[1][1]+10), 'X', font=font, fill=(0, 0, 0))
    draw.text((points[2][0]-10, points[2][1]+10), 'Y', font=font, fill=(0, 0, 0))
    draw.text((points[3][0]-10, points[3][1]-10), 'Z', font=font, fill=(0, 0, 0))
    draw.text((points[4][0]-15, points[4][1]-10), 'U', font=font, fill=(0, 0, 0))
    draw.text((points[5][0]+10, points[5][1]-10), 'V', font=font, fill=(0, 0, 0))

    if angle>=45:
        ref_point = ((points[4][0]+points[5][0]-20)/2, points[4][1])
        print(ref_point)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
    elif angle<45:
        ref_point = ((points[4][0]+points[5][0])/2, points[4][1])
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
    draw.line(points, fill=fill, width=2)
    pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
    draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
    draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))

def create_90degree_hexagon_line(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a rotated hexagon centered at `center`."""
    angle1 = 45
    points = [
        (center[0] + size * math.cos(math.radians(angle1 + offset)),
         center[1] + size * math.sin(math.radians(angle1 + offset)))
        for offset in range(45, 395, 60)  # Hexagon has 6 sides, 60 degrees apart
    ]
    #print(points)
    font = ImageFont.load_default(13)
    draw.text((points[0][0], points[0][1]+10), 'W', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]-10, points[1][1]+10), 'X', font=font, fill=(0, 0, 0))
    draw.text((points[2][0]-15, points[2][1]-10), 'Y', font=font, fill=(0, 0, 0))
    draw.text((points[3][0], points[3][1]-20), 'Z', font=font, fill=(0, 0, 0))
    draw.text((points[4][0]+10, points[4][1]-10), 'U', font=font, fill=(0, 0, 0))
    draw.text((points[5][0]+10, points[5][1]-10), 'V', font=font, fill=(0, 0, 0))
    draw.polygon(points, outline=fill, width=2)
    if angle>=45:
        ref_point = (points[1][0],(points[2][1]+points[5][1]-20)/2)
        points1 = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
    elif angle<45:
        ref_point = (points[1][0],(points[2][1]+points[5][1])/2)
        points1 = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
    draw.line(points1, fill=fill, width=2)



def create_pentagon_line(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a rotated hexagon centered at `center`."""
    angle1 = 207
    font = ImageFont.load_default(13)

    points = [
        (center[0] + size * math.cos(math.radians(angle1 + offset)),
         center[1] + size * math.sin(math.radians(angle1 + offset)))
        for offset in range(-45, 305, 72)  # pentagon has 5 sides, 72 degrees apart
    ]
    draw.polygon(points, outline=fill, width=2)
    print(points)
    draw.text((points[0][0]-20, points[0][1]-10), 'W', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]+10, points[1][1]-20), 'X', font=font, fill=(0, 0, 0))
    draw.text((points[2][0]-10, points[2][1]-20), 'Y', font=font, fill=(0, 0, 0))
    draw.text((points[3][0]+20, points[3][1]-10), 'Z', font=font, fill=(0, 0, 0))
    draw.text((points[4][0]-15, points[4][1]+10), 'U', font=font, fill=(0, 0, 0))
    #draw.text((points[5][0]+10, points[5][1]-10), 'V', font=font, fill=(0, 0, 0))
    draw.line(((50, 150), (150, 150), (350,150) ), fill=fill, width=2)
    draw.text((30, 150), 'L2', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = ((points[4][0]+points[3][0]-20)/2, points[4][1])
        ref_point = (200, 150)
        draw.line(((50, 250), (200, 250), (350,250)), fill=fill, width=2)
        draw.text((30, 250), 'L1', font=font, fill=(0, 0, 0))
        #print(ref_point)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
    elif angle<45:
        ref_point = ((points[4][0]+points[3][0])/2, points[4][1])
        ref_point = (150, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((50, 250), (200, 250), (350,250)), fill=fill, width=2)
        draw.text((30, 250), 'L1', font=font, fill=(0, 0, 0))
    draw.line(points, fill=fill, width=2)
    pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
    #draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
    #draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))

def create_90degree_pentagon_line(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a rotated hexagon centered at `center`."""
    angle1 = 27
    points = [
        (center[0] + size * math.cos(math.radians(angle1 + offset)),
         center[1] + size * math.sin(math.radians(angle1 + offset)))
        for offset in range(45, 395, 72)  # pentagon has 5 sides, 72 degrees apart
    ]
    print(points)
    font = ImageFont.load_default(13)
    draw.text((points[0][0]-10, points[0][1]+10), 'W', font=font, fill=(0, 0, 0))
    draw.text((points[1][0], points[1][1]+20), 'X', font=font, fill=(0, 0, 0))
    draw.text((points[2][0], points[2][1]-20), 'Y', font=font, fill=(0, 0, 0))
    draw.text((points[3][0]-10, points[3][1]-20), 'Z', font=font, fill=(0, 0, 0))
    draw.text((points[4][0]+10, points[4][1]-10), 'U', font=font, fill=(0, 0, 0))
    #draw.text((points[5][0]+10, points[5][1]-10), 'V', font=font, fill=(0, 0, 0))
    draw.polygon(points, outline=fill, width=2)
    draw.line(((150, 50), (150, 150), (150, 350) ), fill=fill, width=2)
    draw.text((150, 30), 'L2', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (points[1][0],(points[2][1]+points[4][1]-20)/2)
        ref_point = (150, 200)
        points1 = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((250, 50), (250, 200), (250, 350)), fill=fill, width=2)
        draw.text((250, 30), 'L1', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (points[1][0],(points[2][1]+points[4][1])/2)
        ref_point = (170, 230)
        points1 = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((250, 50), (250, 200), (250, 350)), fill=fill, width=2)
        draw.text((250, 30), 'L1', font=font, fill=(0, 0, 0))
    draw.line(points1, fill=fill, width=2)


# In[109]:


def create_triangle_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    font = ImageFont.load_default(13)
    draw.line(((30, 190), (150, 190), (350,190) ), fill=fill, width=2)
    draw.text((30, 170), 'L1', font=font, fill=(0, 0, 0))
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    #draw.text((90, 140), 'P', font=font, fill=(0, 0, 0))
    #draw.text((260, 140), 'Q', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (200, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        #draw.line((points[1], (200, points[1][1]), (250,points[1][1])), fill=fill, width=2)
        #draw.line(((100, 150), (100, 250), (100,250)), fill=fill, width=2)
        #draw.line(((250, 150), (250, 250), (250,250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((90, 260), 'S', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'R', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (150, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        #draw.line((points[1], (200, points[1][1]), (250,points[1][1])), fill=fill, width=2)
        #draw.line(((100, 150), (100, 250), (100, 250)), fill=fill, width=2)
        #draw.line(((250, 150), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((90, 260), 'S', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'R', font=font, fill=(0, 0, 0))
    #print(points)
    draw.line(points, fill=fill, width=2)
    #third place
    #points[1][0]+100, points[1][1]-50
    #if points[1][0] <=100:
    draw.line(((points[1][0]-50, points[1][1]-50), (points[1][0]+100, points[1][1]-50)), fill=fill, width=2)
    draw.line((points[0], (points[1][0]+100, points[1][1]-50)), fill=fill, width=2)
    draw.text((points[0][0], points[0][1]-20), 'P', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]+100, points[1][1]-40), 'Q', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]-20,points[1][1]-40), 'R', font=font, fill=(0, 0, 0))
    #draw.line(points, fill=fill, width=2)
    #font = ImageFont.load_default()
    
    #draw.line(points, fill=fill)

def create_rotate90_triangle_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    draw.line(((190, 30), (190, 150), (190, 350) ), fill=fill, width=2)
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    font = ImageFont.load_default(13)
    draw.text((170, 50), 'L1', font=font, fill=(0, 0, 0))
    #draw.text((140, 90), 'S', font=font, fill=(0, 0, 0))
    #draw.text((260, 90), 'P', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (100, 180)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        #draw.line(((250, 100), (250, 200), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 250), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 100), (250, 100), (250, 100)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (170, 20)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        #draw.line(((250, 100), (250, 200), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 250), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 100), (250, 100), (250, 100)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
        
    #print(points)
    draw.line(points, fill=fill, width=2)
    #third point
    #points[1][0]-50, points[1][1]-100
    draw.line((points[0], (points[1][0]-50, points[1][1]-100)), fill=fill, width=2)
    draw.line(((points[1][0]-50, points[1][1]-100), (points[1][0]-50, points[1][1]+50)), fill=fill, width=2)
    draw.text((points[0][0]-20, points[0][1]), 'P', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]-40, points[1][1]-110), 'Q', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]-40,points[1][1]+10), 'R', font=font, fill=(0, 0, 0))
    #font = ImageFont.load_default()
    #draw.text((ref_point[0], ref_point[1]), 'A', font=font, fill=(0, 0, 0))
    #draw.line(points, fill=fill)




def create_congr_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    font = ImageFont.load_default(13)
    draw.line(((50, 150), (150, 150), (350,150) ), fill=fill, width=2)
    #draw.text((30, 170), 'L1', font=font, fill=(0, 0, 0))
    draw.line(((50, 250), (200, 250), (350,250)), fill=fill, width=2)
    #draw.text((90, 140), 'P', font=font, fill=(0, 0, 0))
    #draw.text((260, 140), 'Q', font=font, fill=(0, 0, 0))
    first_angle = np.random.choice([30,35,40, 45])
    print(first_angle)
    if angle>=45:
        ref_point = (200, 150)
        points = get_coords(ref_point[0], ref_point[1], first_angle, 400, 400)
        new_ref = ((points[0][0]+points[1][0])/2, (points[0][1]+points[1][1])/2)
        new_ref = ((points[0][0]+points[1][0])/2, 150)

        points1 = get_coords(new_ref[0], new_ref[1], angle+first_angle, 400, 400)

        #draw.line((points[1], (200, points[1][1]), (250,points[1][1])), fill=fill, width=2)
        #draw.line(((100, 150), (100, 250), (100,250)), fill=fill, width=2)
        #draw.line(((250, 150), (250, 250), (250,250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        #draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        #draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((90, 260), 'S', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'R', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (150, 150)
        points = get_coords(ref_point[0], ref_point[1], first_angle, 400, 400)
        points1 = get_coords(ref_point[0], ref_point[1], angle+first_angle, 400, 400)

        #draw.line((points[1], (200, points[1][1]), (250,points[1][1])), fill=fill, width=2)
        #draw.line(((100, 150), (100, 250), (100, 250)), fill=fill, width=2)
        #draw.line(((250, 150), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        #draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        #draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((90, 260), 'S', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'R', font=font, fill=(0, 0, 0))
    #print(points)
    draw.line(points, fill=fill, width=2)
    draw.line(points1, fill=fill, width=2)

    #third place
    #points[1][0]+100, points[1][1]-50
    #if points[1][0] <=100:
    #draw.line(((points[1][0]-50, points[1][1]-50), (points[1][0]+100, points[1][1]-50)), fill=fill, width=2)
    #draw.line((points[0], (points[1][0]+100, points[1][1]-50)), fill=fill, width=2)
    #draw.text((points[0][0], points[0][1]-20), 'P', font=font, fill=(0, 0, 0))
    #draw.text((points[1][0]+100, points[1][1]-40), 'Q', font=font, fill=(0, 0, 0))
    #draw.text((points[1][0]-20,points[1][1]-40), 'R', font=font, fill=(0, 0, 0))
    #draw.line(points, fill=fill, width=2)
    #font = ImageFont.load_default()
    
    #draw.line(points, fill=fill)

def create_rotate90_congr_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    draw.line(((190, 30), (190, 150), (190, 350) ), fill=fill, width=2)
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    font = ImageFont.load_default(13)
    draw.text((170, 50), 'L1', font=font, fill=(0, 0, 0))
    #draw.text((140, 90), 'S', font=font, fill=(0, 0, 0))
    #draw.text((260, 90), 'P', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (100, 200)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        #draw.line(((250, 100), (250, 200), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 250), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 100), (250, 100), (250, 100)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (170, 250)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        #draw.line(((250, 100), (250, 200), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 250), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 100), (250, 100), (250, 100)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
        
    #print(points)
    draw.line(points, fill=fill, width=2)
    #third point
    #points[1][0]-50, points[1][1]-100
    draw.line((points[0], (points[1][0]-50, points[1][1]-100)), fill=fill, width=2)
    draw.line(((points[1][0]-50, points[1][1]-100), (points[1][0]-50, points[1][1]+50)), fill=fill, width=2)
    draw.text((points[0][0]-20, points[0][1]), 'P', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]-40, points[1][1]-110), 'Q', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]-40,points[1][1]+10), 'R', font=font, fill=(0, 0, 0))
    #font = ImageFont.load_default()
    #draw.text((ref_point[0], ref_point[1]), 'A', font=font, fill=(0, 0, 0))
    #draw.line(points, fill=fill)


# In[59]:


def define_canvas(canvas_size=(400, 400), bg_color = "white", size = 200, fill = "black"):
    img = Image.new("RGB", canvas_size, color=bg_color)
    draw = ImageDraw.Draw(img)
    center = (canvas_size[0] / 2, canvas_size[1] / 2)
    return draw, center, size, fill, img





output_dir = 'D:/PycharmProjects/mllm_math/dataset/generated/pentagon/'
#output_dir1 = 'D:/PycharmProjects/mllm_math/dataset/generated/math_1/'





position_angle_type = dict()
position_angle_type = {1: ['corresponding', 'vertically_opposite', 'alternate_exterior', ],
                      3:['alternate_interior', 'linear', 'corresponding', 'vertically_opposite'],
                       4:['co_interior']
                      }



def find_answer(ang, ang_t, pos):
    
    #if ang_t in ['vertically opposite',  'alternate_exterior']:
     #   return ang   
    #if ang_t in ['corresponding']:
    if pos==1:
        return 180-ang, 180-ang
    if pos==3:
        if ang_t=='linear':
            return ang, 180-ang
        if ang_t=='alternate_interior':
            return ang, ang
        if ang_t=='corresponding':
            return ang, ang
        if ang_t=='vertically_opposite':
            return ang, ang
    if pos==4:
        if ang_t=='co_interior':
            return 180-ang, ang



def find_answer_congr_lines(ang, ang_t, pos):
    
    #if ang_t in ['vertically opposite',  'alternate_exterior']:
     #   return ang   
    #if ang_t in ['corresponding']:
    if pos==1:
        return 180-ang, 180-ang
    if pos==3:
        if ang_t=='linear':
            return ang, 180-ang
        if ang_t=='alternate_interior':
            return ang, ang
        if ang_t=='corresponding':
            return ang, ang
        if ang_t=='vertically_opposite':
            return ang, ang
    if pos==4:
        if ang_t=='co_interior':
            return 180-ang, ang




line_type = [

"In the diagram, lines L1 and L2 are parallel, and a transversal intersects two sides, creating an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "As shown in the figure, lines L1 and L2 are parallel, and another line cuts two sides, forming an angle {given_letter} of {ang_}. What is the value of angle {find_letter}?"
, "In the figure, lines L1 and L2 are parallel, and a transversal intersects two sides, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "As illustrated, lines L1 and L2 are parallel, and a line intersects two sides, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the diagram, lines L1 and L2 are parallel, and a line crosses two sides, forming a {ang_} angle at point {given_letter}. What is the measure of angle {find_letter}?"
, "Lines L1 and L2 are parallel, and a transversal intersects two sides, forming a {ang_} angle labeled {given_letter}. Find the measure of angle {find_letter}."
, "As shown in the diagram, a transversal intersects parallel lines L1 and L2, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "The figure shows a transversal crossing parallel lines L1 and L2, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the figure, lines L1 and L2 are parallel, and a transversal cuts across both, forming an angle {given_letter} of {ang_}. What is the measure of angle {find_letter}?"
, "As depicted, lines L1 and L2 are parallel, and a line intersecting two sides creates an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "In the given figure, a line intersects the parallel lines L1 and L2, forming a {ang_} angle labeled {given_letter}. Determine the measure of angle {find_letter}."
, "The diagram shows parallel lines L1 and L2, being intersected by another line, forming a {ang_} angle at point {given_letter}. What is the value of angle {find_letter}?"
, "Lines L1 and L2 are parallel and are intersected by a line, forming a {ang_} angle marked as {given_letter}. What is the measure of angle {find_letter}?"
,"A transversal crosses parallel lines L1 and L2, creating a {ang_} angle labeled {given_letter}. What is the corresponding angle {find_letter}?"
]


square_type = [

"In the diagram, PQRS is a square, and a transversal intersects two sides, creating an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "As shown in the figure, PQRS is a square, and another line cuts two sides, forming an angle {given_letter} of {ang_}. What is the value of angle {find_letter}?"
, "In the figure, PQRS is a square, and a transversal intersects two sides, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "As illustrated, PQRS is a square, and a line intersects two sides, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the diagram, PQRS is a square, and a line crosses two sides, forming a {ang_} angle at point {given_letter}. What is the measure of angle {find_letter}?"
, "PQRS is a square, and a transversal intersects two sides, forming a {ang_} angle labeled {given_letter}. Find the measure of angle {find_letter}."
, "As shown in the diagram, a transversal intersects square PQRS, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "The figure shows a transversal crossing square PQRS, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the figure, PQRS is a square, and a transversal cuts across two sides, forming an angle {given_letter} of {ang_}. What is the measure of angle {find_letter}?"
, "As depicted, PQRS is a square, and a line intersecting two sides creates an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "In the given figure, a line intersects the square PQRS, forming a {ang_} angle labeled {given_letter}. Determine the measure of angle {find_letter}."
, "The diagram shows square PQRS, being intersected by a line, forming a {ang_} angle at point {given_letter}. What is the value of angle {find_letter}?"
, "PQRS is a square and are intersected by a line, forming a {ang_} angle marked as {given_letter}. What is the measure of angle {find_letter}?"
,"A transversal crosses square PQRS, creating a {ang_} angle labeled {given_letter}. What is the corresponding angle {find_letter}?"
]


rectangle_type = [

"In the diagram, PQRS is a rectangle, and a transversal intersects two sides, creating an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "As shown in the figure, PQRS is a rectangle, and a line cuts two sides, forming an angle {given_letter} of {ang_}. What is the value of angle {find_letter}?"
, "In the figure, PQRS is a rectangle, and a transversal intersects two sides, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "As illustrated, PQRS is a rectangle, and a line intersects two sides, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the diagram, PQRS is a rectangle, and a line crosses two sides, forming a {ang_} angle at point {given_letter}. What is the measure of angle {find_letter}?"
, "PQRS is a rectangle, and a transversal intersects two sides, forming a {ang_} angle labeled {given_letter}. Find the measure of angle {find_letter}."
, "As shown in the diagram, a transversal intersects rectangle PQRS, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "The figure shows a transversal crossing rectangle PQRS, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the figure, PQRS is a rectangle, and a transversal cuts across two sides, forming an angle {given_letter} of {ang_}. What is the measure of angle {find_letter}?"
, "As depicted, PQRS is a rectangle, and a line intersecting two sides creates an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "In the given figure, a line intersects the rectangle PQRS, forming a {ang_} angle labeled {given_letter}. Determine the measure of angle {find_letter}."
, "The diagram shows rectangle PQRS, being intersected by a line, forming a {ang_} angle at point {given_letter}. What is the value of angle {find_letter}?"
, "PQRS is a rectangle and are intersected by a line, forming a {ang_} angle marked as {given_letter}. What is the measure of angle {find_letter}?"
,"A transversal crosses rectangle PQRS, creating a {ang_} angle labeled {given_letter}. What is the corresponding angle {find_letter}?"
]



trapezoid_type = [

"In the diagram, PQRS is a trapezoid, and a transversal intersects two sides, creating an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "As shown in the figure, PQRS is a trapezoid, and a line cuts two sides, forming an angle {given_letter} of {ang_}. What is the value of angle {find_letter}?"
, "In the figure, PQRS is a trapezoid, and a transversal intersects two sides, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "As illustrated, PQRS is a trapezoid, and a line intersects two sides, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the diagram, PQRS is a trapezoid, and a line crosses two sides, forming a {ang_} angle at point {given_letter}. What is the measure of angle {find_letter}?"
, "PQRS is a trapezoid, and a transversal intersects two sides, forming a {ang_} angle labeled {given_letter}. Find the measure of angle {find_letter}."
, "As shown in the diagram, a transversal intersects trapezoid PQRS, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "The figure shows a transversal crossing trapezoid PQRS, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the figure, PQRS is a trapezoid, and a transversal cuts across two sides, forming an angle {given_letter} of {ang_}. What is the measure of angle {find_letter}?"
, "As depicted, PQRS is a trapezoid, and a line intersecting two sides creates an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "In the given figure, a line intersects the trapezoid PQRS, forming a {ang_} angle labeled {given_letter}. Determine the measure of angle {find_letter}."
, "The diagram shows trapezoid PQRS, being intersected by a line, forming a {ang_} angle at point {given_letter}. What is the value of angle {find_letter}?"
, "PQRS is a trapezoid and are intersected by a line, forming a {ang_} angle marked as {given_letter}. What is the measure of angle {find_letter}?"
,"A transversal crosses trapezoid PQRS, creating a {ang_} angle labeled {given_letter}. What is the corresponding angle {find_letter}?"
]



hexagon_type = [

"In the diagram, UVWXYZ is a regular hexagon, and a transversal intersects two sides, creating an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "As shown in the figure, UVWXYZ is a regular hexagon, and a line cuts two sides, forming an angle {given_letter} of {ang_}. What is the value of angle {find_letter}?"
, "In the figure, UVWXYZ is a regular hexagon, and a transversal intersects two sides, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "As illustrated, UVWXYZ is a regular hexagon, and a line intersects two sides, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the diagram, UVWXYZ is a regular hexagon, and a line crosses two sides, forming a {ang_} angle at point {given_letter}. What is the measure of angle {find_letter}?"
, "UVWXYZ is a regular hexagon, and a transversal intersects two sides, forming a {ang_} angle labeled {given_letter}. Find the measure of angle {find_letter}."
, "As shown in the diagram, a transversal intersects regular hexagon UVWXYZ, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "The figure shows a transversal crossing regular hexagon UVWXYZ, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the figure, UVWXYZ is a regular hexagon, and a transversal cuts across two sides, forming an angle {given_letter} of {ang_}. What is the measure of angle {find_letter}?"
, "As depicted, UVWXYZ is a regular hexagon, and a line intersecting two sides creates an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "In the given figure, a line intersects the regular hexagon UVWXYZ, forming a {ang_} angle labeled {given_letter}. Determine the measure of angle {find_letter}."
, "The diagram shows regular hexagon UVWXYZ, intersected by a line, forming a {ang_} angle at point {given_letter}. What is the value of angle {find_letter}?"
, "UVWXYZ is a regular hexagon and is intersected by a line, forming a {ang_} angle marked as {given_letter}. What is the measure of angle {find_letter}?"
,"A transversal crosses regular hexagon UVWXYZ, creating a {ang_} angle labeled {given_letter}. What is the corresponding angle {find_letter}?"
]


# In[25]:


triangle_type = [

"In the diagram, PQR is a Triangle, and a line L1 parallel to the side QR and cuts other two sides, creating an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "As shown in the figure, PQR is a Triangle, and a line L1 parallel to the side QR and cuts other two sides, forming an angle {given_letter} of {ang_}. What is the value of angle {find_letter}?"
, "In the figure, PQR is a Triangle, and a line L1 parallel to the side QR and cuts other two sides, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "As illustrated, PQR is a Triangle, and a line L1 parallel to the side QR and intersects other two sides, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the diagram, PQR is a Triangle, and a line L1 parallel to the side QR, crosses other two sides, forming a {ang_} angle at point {given_letter}. What is the measure of angle {find_letter}?"
, "PQR is a Triangle, and a transversal L1 parallel to the side QR, intersects other two sides, forming a {ang_} angle labeled {given_letter}. Find the measure of angle {find_letter}."
, "As shown in the diagram, a transversal L1 parallel to the side QR of triangle PQR, cuts other two sides forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "The figure shows a transversal L1 parallel to a side of triangle PQR cuts other two sides, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the figure, PQR is a Triangle, and a transversal L1 parallel to the side QR, cuts across other two side of triangle PQR, forming an angle {given_letter} of {ang_}. What is the measure of angle {find_letter}?"
, "As depicted, PQR is a Triangle, and a line L1 parallel to the side QR and intersecting two sides creates an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "In the given figure, a line L1 intersects two sides of the triangle PQR and is parallel to QR, forming a {ang_} angle labeled {given_letter}. Determine the measure of angle {find_letter}."
, "The diagram shows a triangle PQR, being intersected by a line L1 parallel to the side QR and cuts other two sides, forming a {ang_} angle at point {given_letter}. What is the value of angle {find_letter}?"
, "PQR is a Triangle and is intersected by a line L1 parallel to the side QR and cuts other two sides, forming a {ang_} angle marked as {given_letter}. What is the measure of angle {find_letter}?"
,"A transversal L1 parallel to the side QR crosses a triangle PQR and cuts other two sides, creating a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
]


pentagon_type = [

"In the diagram, UWXYZ is a pentagon, and lines L1 and L2 are parallel. A transversal cuts them, creating an angle {given_letter} measuring {ang_} degrees. What is the measure of angle {find_letter}?"
]




def generate_samples_pentagon(output_dir, i, no_solution=False):
    #i = 0
    df = pd.DataFrame(columns=['id', 'image_path', 'question', 'answer', ])
    angles = list(range(45,146,20))
    for pos, ang_type in position_angle_type.items():
        for ang_t in ang_type:
            for ang in angles:
                data1 = 'data_1.json'
                data2 = 'data_2.json'
                ang_a, ang_b = find_answer(ang, ang_t, pos)
                directory = f"{ang_t}_{ang}_pos_{pos}"
                os.mkdir(output_dir+directory)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_pentagon_line(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/horizontal.png"
                display(img)
                img.save(filename)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_90degree_pentagon_line(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/vertical.png"
                display(img)
                img.save(filename)
                print(f"Saved: {filename}")
                #os.remove(f"{output_dir}{directory}/"+'data.json')
                r = open(f"{output_dir}{directory}/"+data1, 'w')
                d = dict()
                question = random.choice(pentagon_type).format(given_letter = "A", find_letter = "B",
                                                                          ang_=ang_a, )
                print(question)
                d.update({"image_path": [f"./{directory}/vertical.png", f"./{directory}/horizontal.png"]})
                d.update({"question": question})#f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle A of {ang_a}. What is the value of angle B?"})
                d.update({"answer": ang_b})
                d.update({"id": i})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
                d.update({"id": i})
                #data = 'data_2.json'
                #r = open(f"{output_dir}/{ang_t}_{ang}/"+data, 'w')
                r = open(f"{output_dir}{directory}/"+data2, 'w')
                question = random.choice(pentagon_type).format(given_letter = "B", find_letter = "A",
                                                                          ang_=ang_b, )
                d.update({"question":question})# f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle B of {ang_b}. What is the value of angle A?"})
                d.update({"answer": ang_a})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
    df = df.explode(['image_path'])
    #df.to_csv(output_dir+'input.csv', index=False)
    return df, i
    
def generate_samples_triangle(output_dir, i, no_solution=False):
    #i = 0
    df = pd.DataFrame(columns=['id', 'image_path', 'question', 'answer', ])
    angles = list(range(45,146,20))
    for pos, ang_type in position_angle_type.items():
        for ang_t in ang_type:
            for ang in angles:
                data1 = 'data_1.json'
                data2 = 'data_2.json'
                ang_a, ang_b = find_answer(ang, ang_t, pos)
                directory = f"{ang_t}_{ang}_pos_{pos}"
                os.mkdir(output_dir+directory)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_triangle_lines(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/horizontal.png"
                display(img)
                img.save(filename)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_rotate90_triangle_lines(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/vertical.png"
                display(img)
                img.save(filename)
                print(f"Saved: {filename}")
                #os.remove(f"{output_dir}{directory}/"+'data.json')
                r = open(f"{output_dir}{directory}/"+data1, 'w')
                d = dict()
                question = random.choice(triangle_type).format(given_letter = "A", find_letter = "B",
                                                                          ang_=ang_a, )
                print(question)
                d.update({"image_path": [f"./{directory}/vertical.png", f"./{directory}/horizontal.png"]})
                d.update({"question": question})#f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle A of {ang_a}. What is the value of angle B?"})
                d.update({"answer": ang_b})
                d.update({"id": i})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
                d.update({"id": i})
                #data = 'data_2.json'
                #r = open(f"{output_dir}/{ang_t}_{ang}/"+data, 'w')
                r = open(f"{output_dir}{directory}/"+data2, 'w')
                question = random.choice(triangle_type).format(given_letter = "B", find_letter = "A",
                                                                          ang_=ang_b, )
                d.update({"question":question})# f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle B of {ang_b}. What is the value of angle A?"})
                d.update({"answer": ang_a})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
    df = df.explode(['image_path'])
    #df.to_csv(output_dir+'input.csv', index=False)
    return df, i
    
def generate_samples_hexagon(output_dir, i, no_solution=False):
    #i = 0
    df = pd.DataFrame(columns=['id', 'image_path', 'question', 'answer', ])
    angles = list(range(45,146,20))
    for pos, ang_type in position_angle_type.items():
        for ang_t in ang_type:
            for ang in angles:
                data1 = 'data_1.json'
                data2 = 'data_2.json'
                ang_a, ang_b = find_answer(ang, ang_t, pos)
                directory = f"{ang_t}_{ang}_pos_{pos}"
                os.mkdir(output_dir+directory)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_hexagon_line(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/horizontal.png"
                display(img)
                img.save(filename)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_90degree_hexagon_line(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/vertical.png"
                display(img)
                img.save(filename)
                print(f"Saved: {filename}")
                #os.remove(f"{output_dir}{directory}/"+'data.json')
                r = open(f"{output_dir}{directory}/"+data1, 'w')
                d = dict()
                question = random.choice(hexagon_type).format(given_letter = "A", find_letter = "B",
                                                                          ang_=ang_a, )
                print(question)
                d.update({"image_path": [f"{output_dir}{directory}/vertical.png", f"{output_dir}{directory}/horizontal.png"]})
                d.update({"question": question})#f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle A of {ang_a}. What is the value of angle B?"})
                d.update({"answer": ang_b})
                d.update({"id": i})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
                d.update({"id": i})
                #data = 'data_2.json'
                #r = open(f"{output_dir}/{ang_t}_{ang}/"+data, 'w')
                r = open(f"{output_dir}{directory}/"+data2, 'w')
                question = random.choice(hexagon_type).format(given_letter = "B", find_letter = "A",
                                                                          ang_=ang_b, )
                d.update({"question":question})# f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle B of {ang_b}. What is the value of angle A?"})
                d.update({"answer": ang_a})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
    df = df.explode(['image_path'])
    #df.to_csv(output_dir+'input.csv', index=False)
    return df, i


def generate_samples_trapezoid(output_dir, i, no_solution=False):
    #i = 0
    df = pd.DataFrame(columns=['id', 'image_path', 'question', 'answer', ])
    angles = list(range(45,146,20))
    for pos, ang_type in position_angle_type.items():
        for ang_t in ang_type:
            for ang in angles:
                data1 = 'data_1.json'
                data2 = 'data_2.json'
                ang_a, ang_b = find_answer(ang, ang_t, pos)
                directory = f"{ang_t}_{ang}_pos_{pos}"
                os.mkdir(output_dir+directory)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_trapezoid_lines(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/horizontal.png"
                display(img)
                img.save(filename)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_rotate90_trapezoid_lines(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/vertical.png"
                display(img)
                img.save(filename)
                print(f"Saved: {filename}")
                #os.remove(f"{output_dir}{directory}/"+'data.json')
                r = open(f"{output_dir}{directory}/"+data1, 'w')
                d = dict()
                question = random.choice(trapezoid_type).format(given_letter = "A", find_letter = "B",
                                                                          ang_=ang_a, )
                print(question)
                d.update({"image_path": [f"./{directory}/vertical.png", f"./{directory}/horizontal.png"]})
                d.update({"question": question})#f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle A of {ang_a}. What is the value of angle B?"})
                d.update({"answer": ang_b})
                d.update({"id": i})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
                d.update({"id": i})
                #data = 'data_2.json'
                #r = open(f"{output_dir}/{ang_t}_{ang}/"+data, 'w')
                r = open(f"{output_dir}{directory}/"+data2, 'w')
                question = random.choice(trapezoid_type).format(given_letter = "B", find_letter = "A",
                                                                          ang_=ang_b, )
                d.update({"question":question})# f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle B of {ang_b}. What is the value of angle A?"})
                d.update({"answer": ang_a})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
    df = df.explode(['image_path'])
    #df.to_csv(output_dir+'input.csv', index=False)
    return df, i

def generate_samples_rectangle(output_dir, i, no_solution=False):
    #i = 0
    df = pd.DataFrame(columns=['id', 'image_path', 'question', 'answer', ])
    angles = list(range(45,146,20))
    for pos, ang_type in position_angle_type.items():
        for ang_t in ang_type:
            for ang in angles:
                data1 = 'data_1.json'
                data2 = 'data_2.json'
                ang_a, ang_b = find_answer(ang, ang_t, pos)
                directory = f"{ang_t}_{ang}_pos_{pos}"
                os.mkdir(output_dir+directory)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_rectangle_lines(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/horizontal.png"
                display(img)
                img.save(filename)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_rotate90_rectangle_lines(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/vertical.png"
                display(img)
                img.save(filename)
                print(f"Saved: {filename}")
                #os.remove(f"{output_dir}{directory}/"+'data.json')
                r = open(f"{output_dir}{directory}/"+data1, 'w')
                d = dict()
                question = random.choice(rectangle_type).format(given_letter = "A", find_letter = "B",
                                                                          ang_=ang_a, )
                print(question)
                d.update({"image_path": [f"./{directory}/vertical.png", f"./{directory}/horizontal.png"]})
                d.update({"question": question})#f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle A of {ang_a}. What is the value of angle B?"})
                d.update({"answer": ang_b})
                d.update({"id": i})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
                d.update({"id": i})
                #data = 'data_2.json'
                #r = open(f"{output_dir}/{ang_t}_{ang}/"+data, 'w')
                r = open(f"{output_dir}{directory}/"+data2, 'w')
                question = random.choice(rectangle_type).format(given_letter = "B", find_letter = "A",
                                                                          ang_=ang_b, )
                d.update({"question":question})# f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle B of {ang_b}. What is the value of angle A?"})
                d.update({"answer": ang_a})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
    df = df.explode(['image_path'])
    #df.to_csv(output_dir+'input.csv', index=False)
    return df, i
    
def generate_samples_square(output_dir, i, no_solution=False):
    #i = 0
    df = pd.DataFrame(columns=['id', 'image_path', 'question', 'answer', ])
    angles = list(range(45,146,20))
    for pos, ang_type in position_angle_type.items():
        for ang_t in ang_type:
            for ang in angles:
                data1 = 'data_1.json'
                data2 = 'data_2.json'
                ang_a, ang_b = find_answer(ang, ang_t, pos)
                directory = f"{ang_t}_{ang}_pos_{pos}"
                os.mkdir(output_dir+directory)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_square_lines(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/horizontal.png"
                display(img)
                img.save(filename)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_rotate90_square_lines(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/vertical.png"
                display(img)
                img.save(filename)
                print(f"Saved: {filename}")
                #os.remove(f"{output_dir}{directory}/"+'data.json')
                r = open(f"{output_dir}{directory}/"+data1, 'w')
                d = dict()
                question = random.choice(square_type).format(given_letter = "A", find_letter = "B",
                                                                          ang_=ang_a, )
                print(question)
                d.update({"image_path": [f"./{directory}/vertical.png", f"./{directory}/horizontal.png"]})
                d.update({"question": question})#f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle A of {ang_a}. What is the value of angle B?"})
                d.update({"answer": ang_b})
                d.update({"id": i})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
                d.update({"id": i})
                #data = 'data_2.json'
                #r = open(f"{output_dir}/{ang_t}_{ang}/"+data, 'w')
                r = open(f"{output_dir}{directory}/"+data2, 'w')
                question = random.choice(square_type).format(given_letter = "B", find_letter = "A",
                                                                          ang_=ang_b, )
                d.update({"question":question})# f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle B of {ang_b}. What is the value of angle A?"})
                d.update({"answer": ang_a})
                d.update({"solution cardinality": 1})
                if no_solution == True:
                    d.update({"answer": "no solution"})
                    d.update({"solution cardinality": 0})
                    from create_samples_no_solution import alter_digit
                    d.update({"question":alter_digit(question)})
                d.update({"solution space": '$\mathbb{R}$'})
                df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
    df = df.explode(['image_path'])
    #df.to_csv(output_dir+'input.csv', index=False)
    return df, i

