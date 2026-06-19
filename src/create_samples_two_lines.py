#!/usr/bin/env python
# coding: utf-8


from PIL import Image, ImageDraw,ImageFont
import math
import os
import json
import random
import numpy as np
from IPython.display import display
import pandas as pd
import shutil



SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")



position = [1#,2,3,4,5,6, 7, 8
           ]
angle_type = [#'alternate interior', 
              'corresponding', 'vertically_opposite', 'alternate_exterior', ]
angle = [#20,
         30, #45, 75, 90, 110, 135, 
    150]



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


def create_two_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4, first_angle=45, given="1,2"):
    """Draw a pair of parallel lines."""
    font = ImageFont.load_default(13)
    draw.line(((50, 150), (150, 150), (350,150) ), fill=fill, width=2)
    
    draw.line(((50, 250), (200, 250), (350,250)), fill=fill, width=2)
    draw.text((50, 160), 'L1', font=font, fill=(0, 0, 0), width=2)
    draw.text((50, 260), 'L2', font=font, fill=(0, 0, 0), width=2)
    draw.text((340, 130), given, font=font, fill=(0, 0, 0), width=2)
    #draw.text((260, 140), 'Q', font=font, fill=(0, 0, 0))
    #first_angle = np.random.choice([30,35,40, 45])
    #print(first_angle)
    if angle>=45:
        ref_point = (150, 150)
        points = get_coords(ref_point[0], ref_point[1], first_angle, 400, 400)
        new_ref = ((points[0][0]+points[1][0])/2, (points[0][1]+points[1][1])/2)
        new_ref = ((points[0][0]+points[1][0])/2, 150)

        points1 = get_coords(ref_point[0], ref_point[1], angle+first_angle, 400, 400)

      
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        
    elif angle<45:
        ref_point = (150, 150)
        points = get_coords(ref_point[0], ref_point[1], first_angle, 400, 400)
        points1 = get_coords(ref_point[0], ref_point[1], angle+first_angle, 400, 400)

        #draw.line((points[1], (200, points[1][1]), (250,points[1][1])), fill=fill, width=2)
        #draw.line(((100, 150), (100, 250), (100, 250)), fill=fill, width=2)
        #draw.line(((250, 150), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        
    draw.line(points, fill=fill, width=2)
    draw.line(points1, fill=fill, width=2)

 

def create_rotate90_two_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4, first_angle=45, given="1,2"):
    """Draw a pair of parallel lines."""
    draw.line(((150, 30), (150, 150), (150, 350) ), fill=fill, width=2)
    draw.line(((250, 30), (250, 200), (250, 350)), fill=fill, width=2)
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    font = ImageFont.load_default(13)
    draw.text((130, 40), 'L1', font=font, fill=(0, 0, 0), width=2)
    draw.text((230, 50), 'L2', font=font, fill=(0, 0, 0), width=2)
    #draw.text((140, 90), 'S', font=font, fill=(0, 0, 0))
    #draw.text((260, 90), 'P', font=font, fill=(0, 0, 0))
    draw.text((340, 130), given, font=font, fill=(0, 0, 0), width=2)
    if angle>=45:
        ref_point = (150, 200)
        points = get_vertical_coords(ref_point[0], ref_point[1], first_angle, 400, 400)
        new_ref = ((190, (points[0][1]+points[1][1])/2))
        points1 = get_vertical_coords(ref_point[0], ref_point[1], angle+first_angle, 400, 400)
        #draw.line(((250, 100), (250, 200), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 250), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 100), (250, 100), (250, 100)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        #draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        #draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
    elif angle<45:
        ref_point = (170, 250)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        points1 = get_vertical_coords(ref_point[0], ref_point[1], angle+first_angle, 400, 400)

        #draw.line(((250, 100), (250, 200), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 250), (250, 250), (250, 250)), fill=fill, width=2)
        #draw.line(((150, 100), (250, 100), (250, 100)), fill=fill, width=2)
        #draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        #draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        #draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
        
    #print(points)
    draw.line(points, fill=fill, width=2)
    draw.line(points1, fill=fill, width=2)


def define_canvas(canvas_size=(400, 400), bg_color = "white", size = 200, fill = "black"):
    img = Image.new("RGB", canvas_size, color=bg_color)
    draw = ImageDraw.Draw(img)
    center = (canvas_size[0] / 2, canvas_size[1] / 2)
    return draw, center, size, fill, img




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


def find_answer_two_lines(first_angle ,ang, find_angle, given_ang_1=1, given_ang_2=3):
    
    #if ang_t in ['vertically opposite',  'alternate_exterior']:
     #   return ang   
    #if ang_t in ['corresponding']:
    """
    return P, Q, 
    """
    second_angle = first_angle+ ang
    if given_ang_1 in [1, 7, 8, 13,]:
        first_given = first_angle
    if given_ang_1 in [4, 5, 10,  12]:
        first_given = 180 - second_angle
    if given_ang_1 in [6, 9]:
        first_given = 180-(first_angle+180-second_angle)
    if given_ang_1 in [3, 11]:
        first_given = second_angle
    if given_ang_1 in [2, 14]:    
        first_given = 180 - first_angle
        
    if given_ang_2 in [1, 7, 8, 13,]:
        second_given = first_angle
    if given_ang_2 in [4, 5, 10,  12]:
        second_given = 180 - second_angle
    if given_ang_2 in [6, 9]:
        second_given = 180-(first_angle+180-second_angle)
    if given_ang_2 in [3, 11]:
        second_given = second_angle
    if given_ang_2 in [2, 14]:
        second_given = 180-first_angle
        
    if find_angle in [1, 7, 8, 13,]:
        return first_given, second_given, first_angle
    if find_angle in [4, 5, 10,  12]:
        return first_given, second_given, 180-second_angle
    if find_angle in [6, 9]:
        return first_given, second_given, 180-(first_angle+180-second_angle)
    if find_angle in [3, 11]:
        return first_given, second_given, second_angle
    if find_angle in [2, 14]:
        return first_given, second_given, 180 - first_angle
        


two_line_type = [

"In the diagram, lines L1 and L2 are parallel, and two transversals intersects at a point in L2, creating an angle {given_letter} measuring {ang_} and {given_letter_1} measuring {ang_1}. What is the measure of angle {find_letter}?"
, "As shown in the figure, lines L1 and L2 are parallel, and two lines cuts at a point in L2, forming an angle {given_letter} of {ang_} and {given_letter_1} measuring {ang_1}. What is the value of angle {find_letter}?"
, "In the figure, lines L1 and L2 are parallel, and two transversals intersects at a point in L2, forming a {ang_} angle labeled {given_letter} and {given_letter_1} measuring {ang_1}. What is the measure of angle {find_letter}?"
, "As illustrated, lines L1 and L2 are parallel, and two lines intersects at a point in L2, creating a {ang_} angle labeled {given_letter} and {given_letter_1} measuring {ang_1}. What is the value of angle {find_letter}?"
, "In the diagram, lines L1 and L2 are parallel, and two lines meet at a point in L2, forming a {ang_} angle at point {given_letter} and {given_letter_1} measuring {ang_1}. What is the measure of angle {find_letter}?"
, "Lines L1 and L2 are parallel, and two transversals intersects at a point in L2, forming a {ang_} angle labeled {given_letter} and {given_letter_1} measuring {ang_1}. Find the measure of angle {find_letter}."
, "As shown in the diagram, two transversals intersects parallel lines L1 and L2 at a point in L2, forming a {ang_} angle labeled {given_letter} and {given_letter_1} measuring {ang_1}. What is the measure of angle {find_letter}?"
, "The figure shows two transversals meeting parallel lines L1 and L2 at a point in L2, creating a {ang_} angle labeled {given_letter} and {given_letter_1} measuring {ang_1}. What is the value of angle {find_letter}?"
, "In the figure, lines L1 and L2 are parallel, and two transversals cuts across at a point in L2. If an angle {given_letter} is {ang_} and {given_letter_1} measuring {ang_1}. What is the measure of angle {find_letter}?"
, "As depicted, lines L1 and L2 are parallel, and two lines intersecting at a point in L2. If an angle {given_letter} measuring {ang_} and {given_letter_1} measuring {ang_1}. What is the measure of angle {find_letter}?"
, "In the given figure, two lines intersects the parallel lines L1 and L2, forming a {ang_} angle labeled {given_letter} and {given_letter_1} measuring {ang_1}. Determine the measure of angle {find_letter}."
, "The diagram shows parallel lines L1 and L2, being intersected by two lines at a point in L2, forming a {ang_} angle at point {given_letter} and {given_letter_1} measuring {ang_1}. What is the value of angle {find_letter}?"
, "Lines L1 and L2 are parallel and are intersected by two lines at a point in L2, forming a {ang_} angle marked as {given_letter} and {given_letter_1} measuring {ang_1}. What is the measure of angle {find_letter}?"
,"Two transversals meets parallel lines L1 and L2 at a point in L2, creating a {ang_} angle labeled {given_letter} and {given_letter_1} measuring {ang_1}. What is the angle {find_letter}?"
]



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
,"A transversal L1 parallel to the side QR crosses a triangle PQR and cuts other two sides, creating a {ang_} angle labeled {given_letter}. What is the corresponding angle {find_letter}?"
]



def generate_samples_two_lines(output_dir, i, no_solution=False):
    df = pd.DataFrame(columns=['id', 'image_path', 'question', 'answer', ])
    angles = list(range(50, 106,10))
    done_ang = []
    ang = np.random.choice(angles)
    done_ang.append(ang)
    f_g_ang = list(range(1, 15, 1))
    s_g_ang = list(range(1, 15, 1))
    f_ang = list(range(1, 15, 1))
    random.shuffle(f_g_ang)
    random.shuffle(s_g_ang)
    random.shuffle(f_ang)
    random.shuffle(angles)
    size=200 
    #i = 143
    j = 1
    total = 500
    for given_ang_1 in f_g_ang:
        #for ang in angles:
        #given_ang_1 = random.choice(f_g_ang)
        if i<total:
            pass
        else:
            break
            #ang = np.random.choice(angles)
            #print("hi")
        for ang in angles:
            if j%3==0:
                j=1
                continue
            j=j+1
            j=1
            for given_ang_2 in s_g_ang:
                #given_ang_2 = random.choice(s_g_ang)
                if given_ang_2 == given_ang_1 or (j)%3==0:
                    j=1
                    continue
                j=j+1
                if i<total:
                    j=1
                    for find_angle in f_ang:
                        #find_angle = random.choice(f_ang)
                        if find_angle == given_ang_2 or find_angle== given_ang_1 or (j)%3==0:
                            j=1
                            continue
                        j=j+1
                        data1 = 'data.json'
                        #data2 = 'data_2.json'
                        first_angle = np.random.choice(list(range(30, 45)))
                        ang_p, ang_q, ang_r = find_answer_two_lines(first_angle, ang, find_angle, given_ang_1, given_ang_2)
                        directory = f"given_{given_ang_1}_ang_{given_ang_2}_{first_angle}_{ang}_find_{find_angle}"
                        os.mkdir(output_dir+directory)
                        draw, center, size, fill, img = define_canvas()
                        
                        given_str = str(given_ang_1)+','+str(given_ang_2)+','+str(find_angle)
                        create_two_lines(draw, center, size, ang, fill, first_angle=first_angle, given=given_str)
                        filename = f"{output_dir}{directory}/horizontal.png"
                        display(img)
                        img.save(filename)
                        draw, center, size, fill, img = define_canvas()
                        
            
                        create_rotate90_two_lines(draw, center, size, ang, fill, first_angle=first_angle, given=given_str)
                        filename = f"{output_dir}{directory}/vertical.png"
                        display(img)
                        img.save(filename)
                        print(f"Saved: {filename}")
                        #os.remove(f"{output_dir}{directory}/"+'data.json')
                        r = open(f"{output_dir}{directory}/"+data1, 'w')
                        d = dict()
                        question = np.random.choice(two_line_type).format(given_letter = "P", find_letter = "R",
                                                                                  ang_=ang_p, given_letter_1="Q", ang_1=ang_q)
                        print(question)
                        d.update({"image_path": [f"{output_dir}{directory}/vertical.png", f"{output_dir}{directory}/horizontal.png"]})
                        d.update({"question": question})#f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle A of {ang_a}. What is the value of angle B?"})
                        d.update({"answer": int(ang_r)})
                        d.update({"id": i})
                        d.update({"solution cardinality": 1})
                        if no_solution == True:
                            d.update({"answer": "no solution"})
                            d.update({"solution cardinality": 0})
                            from create_samples_no_solution import alter_digit
                            d.update({"question":alter_digit(question)})
                        d.update({"solution space": '$\mathbb{R}$'})
                        print(json.dumps(d, indent=4,))# fp=f"{output_dir}{directory}/"+data1))
                        df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
                        r.write(json.dumps(d, indent=4))
                        r.close()
                        #i = i+1
                        d.update({"id": i})
                        
                        i = i+1
                        j =1
            
    df = df.explode(['image_path'])
    
    return df, i

