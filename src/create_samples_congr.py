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
    draw.line(((160, 190), (190, 190), (300,190) ), fill=fill, width=2)
    draw.text((145, 180), 'L', font=font, fill=(0, 0, 0), width=2)
    draw.text((180, 200), 'A', font=font, fill=(0, 0, 0), width=2)
    draw.text((280, 200), 'B', font=font, fill=(0, 0, 0), width=2)
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
        #draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        #draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
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
        #draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        #draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((90, 260), 'S', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'R', font=font, fill=(0, 0, 0))
    #print(points)
    draw.line((points[0], (points[1][0], points[1][1]-50)), fill=fill, width=2)
    #third place
    #points[1][0]+100, points[1][1]-50
    #if points[1][0] <=100:
    draw.line(((points[1][0], points[1][1]-50), (points[1][0]+100, points[1][1]-50)), fill=fill, width=2)
    draw.line((points[0], (points[1][0]+100, points[1][1]-50)), fill=fill, width=2)
    
    #draw.line((points[0][0]+, (points[1][0]+100, points[1][1]-50)), fill=fill, width=2)
    
    draw.text((points[0][0], points[0][1]-20), 'P', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]+100, points[1][1]-40), 'Q', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]-20,points[1][1]-40), 'R', font=font, fill=(0, 0, 0))


def create_rotate90_triangle_lines(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    draw.line(((190, 110), (190, 150), (190, 250) ), fill=fill, width=2)
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill, width=2)
    font = ImageFont.load_default(13)
    draw.text((180, 90), 'L', font=font, fill=(0, 0, 0), width=2)
    draw.text((200, 110), 'B', font=font, fill=(0, 0, 0), width=2)
    draw.text((200, 210), 'A', font=font, fill=(0, 0, 0), width=2)
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
        #draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        #draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
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
        #draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        #draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        #draw.text((140, 260), 'R', font=font, fill=(0, 0, 0))
        #draw.text((260, 260), 'Q', font=font, fill=(0, 0, 0))
        
    #print(points)
    draw.line((points[0], (points[1][0]-50, points[1][1])), fill=fill, width=2)
    #third point
    #points[1][0]-50, points[1][1]-100
    draw.line((points[0], (points[1][0]-50, points[1][1]-100)), fill=fill, width=2)
    draw.line(((points[1][0]-50, points[1][1]-100), (points[1][0]-50, points[1][1])), fill=fill, width=2)
    draw.text((points[0][0]-20, points[0][1]), 'P', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]-40, points[1][1]-110), 'Q', font=font, fill=(0, 0, 0))
    draw.text((points[1][0]-40,points[1][1]+10), 'R', font=font, fill=(0, 0, 0))


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



def compat_congr(given_side1, given_side2, given_side3, find_side):
    if given_side1 in ["AP", "PB", "AB"] and given_side2 in ["AP", "PB", "AB"] and given_side3 in ["AP", "PB", "AB"]:
        return
    if find_side == "QR" and "AB" not in [given_side1, given_side2, given_side3]:
        return
    if find_side == "BQ" and "PB" not in [given_side1, given_side2, given_side3]:
        return
    if find_side == "RA" and "AP" not in [given_side1, given_side2, given_side3]:
        return
    if find_side == "AP" and "RA" not in [given_side1, given_side2, given_side3]:
        return
    if find_side == "PB" and "BQ" not in [given_side1, given_side2, given_side3]:
        return
    if find_side == "AB" and "QR" not in [given_side1, given_side2, given_side3]:
        return
         

def find_answer_congr(given, find_side):#given_side1, given_side2, given_side3, ang, find_side):
    
    #if ang_t in ['vertically opposite',  'alternate_exterior']:
     #   return ang   
    #if ang_t in ['corresponding']:
    #["AP", "PB", "AB", "RA", "BQ", "QR", "RP", "PQ"]
    
    
    if "AP" in given.keys() and "RA" in given.keys() and "RP" not in given.keys():        
        given.update({"RP":given["AP"]+given["RA"]})
        
    if "PB" in given.keys() and "BQ" in given.keys() and "PQ" not in given.keys(): 
        given.update({"PQ":given["PB"]+given["BQ"]})
        
    if "RP" in given.keys() and "AP" in given.keys() and "RA" not in given.keys(): 
        given.update({"RA":given["RP"]-given["AP"]})
        
    if "RP" in given.keys() and "RA" in given.keys() and  "AP" not in given.keys(): 
        given.update({"AP":given["RP"]-given["RA"]})
        
    if "PQ" in given.keys() and "BQ" in given.keys() and "PB" not in given.keys(): 
        given.update({"PB":given["PQ"]-given["BQ"]})
    if "PQ" in given.keys() and "PB" in given.keys() and "BQ" not in given.keys(): 
        given.update({"BQ":given["PQ"]-given["PB"]})
 
    #print(given)
    s = None
    if find_side in "QR" and "QR" not in given.keys():
        if "AB" in given.keys():#[given_side1, given_side2, given_side3]:
            if "PB" in given.keys() and "BQ" in given.keys():#[given_side1, given_side2, given_side3]:
                #print("yes")
                s = given["AB"]*(given["PB"]+given["BQ"])
                s = s/given["PB"]
                #print(s)
                given.update({ "QR":int(s)  })
            elif "AP" in given.keys() and "RA" in given.keys():#[given_side1, given_side2, given_side3]:
               # print("yes1")
                s = given["AP"]*(given["AP"]+given["RA"])
                s = s/given["AP"]
                given.update({ "QR":int(s)  })
    if find_side in "AB" and "AB" not in given.keys():
        if "QR" in given.keys():#[given_side1, given_side2, given_side3]:
            if "PB" in given.keys() and "BQ" in given.keys():#[given_side1, given_side2, given_side3]:
                s = given["QR"]/(given["PB"]+given["BQ"])
                s = s*given["PB"]
                given.update({ "AB":int(s)  })
            elif "AP" in given.keys() and "RA" in given.keys():#[given_side1, given_side2, given_side3]:
                s = given["QR"]/(given["AP"]+given["RA"])
                s = s*given["AP"]
                given.update({ "AB":int(s)  })
    if find_side in "BQ" and "BQ" not in given.keys():
        #{'AB': 30, 'RP': 450, 'QR': 180, 'RA': 375, 'PB': 67, 'AP': 75}
        if "PB" in given.keys():#[given_side1, given_side2, given_side3]:
            if "AB" in given.keys() and "QR" in given.keys():#[given_side1, given_side2, given_side3]:
                s = given["PB"]*given["QR"]#+given["BQ"])
                print(s)
                s = s/given["AB"]
                print(s)
                s = s - given["PB"]
                print(s)
                given.update({ "BQ":int(s)  })
            elif "AP" in given.keys() and "RA" in given.keys():#[given_side1, given_side2, given_side3]:
                s = given["AP"]*given["RA"]#+given["RA"])
                s = s/given["AP"]
                given.update({ "BQ":int(s)  })
    """
    if find_side in "PB" and "PB" not in given.keys():
        if "BQ" in given.keys():#[given_side1, given_side2, given_side3]:
            if "AB" in given.keys() and "QR" in given.keys():#[given_side1, given_side2, given_side3]:
                s = given["QR"]/(given["PB"]+given["BQ"])
                s = s*given["PB"]
                given.update({ "PB":int(s)  })
            elif "AP" in given.keys() and "RA" in given.keys():#[given_side1, given_side2, given_side3]:
                s = given["QR"]/(given["AP"]+given["RA"])
                s = s*given["AP"]
                given.update({ "PB":int(s)  })
    
    if find_side in "AP" and "AP" not in given.keys():
        if "RA" in given.keys():#[given_side1, given_side2, given_side3]:
            if "PB" in given.keys() and "BQ" in given.keys():#[given_side1, given_side2, given_side3]:
                s = given["PB"]*(given["RA"]+given["AP"])
                s = s/(given["PB"]+given["BQ"])   
                given.update({ "AP":int(s)  })
            elif "AB" in given.keys() and "QR" in given.keys():#[given_side1, given_side2, given_side3]:
                s = given["AB"]*(given["RA"]+given["AP"])#+given["RA"])
                s = s/given["QR"]
                given.update({ "AP":int(s)  })
    """
    if find_side in "RA" and "RA" not in given.keys():
        if "AP" in given.keys():#[given_side1, given_side2, given_side3]:
            if "PB" in given.keys() and "BQ" in given.keys():#[given_side1, given_side2, given_side3]:
                s = given["AP"]*(given["PB"]+given["BQ"])
                s = s/given["PB"]
                s = s-given["AP"]
                given.update({ "RA":int(s)  })
            elif "AB" in given.keys() and "QR" in given.keys():#[given_side1, given_side2, given_side3]:
                s = given["QR"]*given["AP"]#+given["RA"])
                s = s/given["AB"]
                s = s-given["AP"]
                given.update({ "RA":int(s)  }) 
    #print(find_side)
    if find_side in given.keys():
       # print( given[find_side])
        return given, given[find_side]
    return given, None


triangle_congr_type = [
"In the diagram, PQR is a Triangle, and a line L parallel to the side QR and cuts other two sides at A and B. If length of \
{given_letter1}={given_side1}, {given_letter2}={given_side2} and {given_letter3}={given_side3}\
. What is the length of side {find_letter}, rounded to the nearest integer?"
    ,"In the diagram, PQR is a triangle, and a line L parallel to the side QR cuts the other two sides at A and B.\
 If the length of {given_letter1} is {given_side1}, {given_letter2}  is {given_side2}, and {given_letter3} is {given_side3},\
 what is the length of side {find_letter}, rounded to the nearest integer?"
]




def choose_length(ang):#, sides):
    def fill_side_angle(ang_side):
        if "AP" in ang_side.keys() and "RA" in ang_side.keys():        
            ang_side.update({"RP":ang_side["AP"]+ang_side["RA"]})
        
        if "PB" in ang_side.keys() and "BQ" in ang_side.keys(): 
            ang_side.update({"PQ":ang_side["PB"]+ang_side["BQ"]})
            
        if "RP" in ang_side.keys() and "AP" in ang_side.keys(): 
            ang_side.update({"RA":ang_side["RP"]-ang_side["AP"]})
            
        if "RP" in ang_side.keys() and "RA" in ang_side.keys(): 
            ang_side.update({"AP":ang_side["RP"]-ang_side["RA"]})
            
        if "PQ" in ang_side.keys() and "BQ" in ang_side.keys(): 
            ang_side.update({"PB":ang_side["PQ"]-ang_side["BQ"]})
        if "PQ" in ang_side.keys() and "PB" in ang_side.keys(): 
            ang_side.update({"BQ":ang_side["PQ"]-ang_side["PB"]})
        return ang_side
 
    given = dict()
    ang_side = dict()
    given_side = ["AP", "PB", "AB", "RA", "BQ", "QR", "RP", "PQ"]

    side_length = {60:{},
              90:{"AP":[4, 8, 12, 15, 16, 29], 
                  "PB":[5, 10, 15, 17, 20, 21], 
                  "AB":[3, 6, 9, 8, 12, 20],
                  #"RA":[4, 4, 3, ],
                 },
              120: {}}
    if ang==60:
        #for s in sides:
         #   if s in side_length[90].keys():
           #     given[s] = random.choice(side_length[90][s])
        r = random.randint(2, 6)
        AP = random.randint(4, 50)
        PB = int(AP*0.9)#np.sin(np.deg2rad(ang))
        #PB = PB/np.sin(np.deg2rad(80))
        AB = int(AP*0.4)#np.sin(np.deg2rad(40))
        #AB = AB/np.sin(np.deg2rad(80))
        ang_side.update({"AP":AP, "PB":PB, "AB":AB })
        RP = AP*r #- int(0.2*AP)
        
        PQ = PB*r#np.sin(np.deg2rad(80))
        
        QR = AB*r#np.sin(np.deg2rad(40))
        ang_side.update({"RP":RP, "PQ":PQ, "QR":QR })
        ang_side = fill_side_angle(ang_side)
    if ang==120:
        #for s in sides:
         #   if s in side_length[90].keys():
           #     given[s] = random.choice(side_length[90][s])
        r = random.randint(2, 6)
        AP = random.randint(4, 50)
        PB = int(AP*1.7)#np.sin(np.deg2rad(ang))
        #PB = PB/np.sin(np.deg2rad(40))
        AB = int(AP*0.5)#np.sin(np.deg2rad(20))
        #AB = AB/np.sin(np.deg2rad(40))
        ang_side.update({"AP":AP, "PB":PB, "AB":AB })
        RP = AP*r #- int(0.2*AP)
        PQ = PB*r#np.sin(np.deg2rad(ang))
        #PQ = PQ/np.sin(np.deg2rad(40))
        QR = AB*r#np.sin(np.deg2rad(20))
        #QR = QR*np.sin(np.deg2rad(40))
        ang_side.update({"RP":RP, "PQ":PQ, "QR":QR })
        ang_side = fill_side_angle(ang_side)

    if ang==90:
        #for s in sides:
         #   if s in side_length[90].keys():
           #     given[s] = random.choice(side_length[90][s])
        ind = random.choice(range(len(side_length[90]["AP"])))
        AP = side_length[90]["AP"][ind]
        PB = side_length[90]["PB"][ind]
        AB = side_length[90]["AB"][ind]
        ang_side.update({"AP":AP, "PB":PB, "AB":AB })
        ind = random.choice(range(len(side_length[90]["AP"])))
        while side_length[90]["AP"][ind] < AP:
            ind = random.choice(range(len(side_length[90]["AP"])))
        RP = side_length[90]["AP"][ind]
        #PQ = RP*np.sin(np.deg2rad(ang))
        PQ = side_length[90]["PB"][ind]
        #QR = RP*np.sin(np.deg2rad(30))
        QR = side_length[90]["AB"][ind]
        ang_side.update({"RP":RP, "PQ":PQ, "QR":QR })
        ang_side = fill_side_angle(ang_side)
    return ang_side

def solution(given, find_side):
    if find_side=="AP" and "RA" not in given.keys() and "AP" not in given.keys() and "RP" not in given.keys():
        return 1
    if find_side=="RA" and "RA" not in given.keys() and "AP" not in given.keys() and "RP" not in given.keys():
        return 1
    if find_side=="RP" and "RA" not in given.keys() and "AP" not in given.keys() and "RP" not in given.keys():
        return 1
    if find_side=="PB" and "PB" not in given.keys() and "BQ" not in given.keys() and "PQ" not in given.keys():
        return 1
    if find_side=="BQ" and "PB" not in given.keys() and "BQ" not in given.keys() and "PQ" not in given.keys():
        return 1
    if find_side=="PQ" and "PB" not in given.keys() and "BQ" not in given.keys() and "PQ" not in given.keys():
        return 1
    if find_side=="AB" and "AB" not in given.keys() and "QR" not in given.keys():
        return 1
    if find_side=="QR" and "AB" not in given.keys() and "QR" not in given.keys():
        return 1


def generate_samples_triangle_lines(output_dir, i):
    #i = 0
    df = pd.DataFrame(columns=['id', 'image_path', 'question', 'answer', ])
    #df1 = pd.DataFrame(columns=['id', 'image_path', 'question', 'answer', ])

    angles = list(range(60,121,30))
    random.choice(angles)
    #{'AP': 14, 'PB': 12, 'AB': 5, 'RP': 84, 'PQ': 72, 'QR': 30, 'RA': 70, 'BQ': 60}
    poss_find_side = ["AP", "PB", "AB", "RA", "BQ", 
                       "QR", "RP", "PQ"]
    poss_given_side = ["AP", "PB", "AB", "RA", "BQ", 
                       "QR", "RP", "PQ"]
    pairs = [["AP", "RP" , "any" ,"RA"], ["AP", "RP" , "AB" ,"QR"], ["AB", "QR", "BQ", "PB"], ["BQ", "PB",  "QR","AB" ],
            ["PB", "BQ" , "any" ,"PQ"], ["AP", "RP" , "PB" ,"PQ"], ["PB" ,"PQ", "AP", "RP" , ]]
    random.choice(poss_find_side)
    random.choice(poss_given_side)

    for ang in [60, 120]:
        for pair in pairs:
            #for find_side in poss_find_side:
                given = dict()
                #for g in given_side:
                ang_total_side = choose_length(ang)
                #if all(ang_total_side.values()==0):
                
                any_choice = random.sample(poss_given_side, 8)# random.choice(3,4)) 
                if "any" in pair:
                    for t in any_choice:
                        if t!=pair[0] and t!=pair[1]:
                            pair[2] = t
                            break
                given.update({pair[0]: ang_total_side[pair[0]], pair[1]: ang_total_side[pair[1]], pair[2]: ang_total_side[pair[2]]})    
                find_side = pair[3]
                print(given, find_side)
                data1 = 'data.json'
                #data2 = 'data_2.json'
                #no_sol_flag = True#no_solution(given, find_side)
                #for itr in range(8):
                 #   given, ans = find_answer_congr(given, find_side)
                folder = None
                directory = f"{list(given.values())[0]}_{list(given.values())[1]}_{list(given.values())[2]}_Fside_{find_side}"
                #if no_sol_flag:            
                   # folder =  output_dir1+directory
                #if ans !=None:
                folder =  output_dir+directory
                #else:
                 #   continue

                #os.mkdir(output_dir+directory)
                os.mkdir(folder)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_triangle_lines(draw, center, size, ang, fill,)
                filename = f"{folder}/horizontal.png"
                display(img)
                img.save(filename)
                draw, center, size, fill, img = define_canvas()
                size=120

                create_rotate90_triangle_lines(draw, center, size, ang, fill, )
                filename = f"{folder}/vertical.png"
                display(img)
                img.save(filename)
                print(f"Saved: {filename}")
                #os.remove(f"{output_dir}{directory}/"+'data.json')
                r = open(f"{folder}/"+data1, 'w')
                d = dict()
                question = random.choice(triangle_congr_type).format(given_letter1=list(given.keys())[0], given_side1=list(given.values())[0], 
                                                                     given_letter2=list(given.keys())[1],
                                                                     given_side2=list(given.values())[1], 
                                              given_letter3=list(given.keys())[2], given_side3=list(given.values())[2],  find_letter = find_side,
                                                                          )
                print(question)
                d.update({"image_path": [f"./{directory}/vertical.png", f"./{directory}/horizontal.png"]})
                d.update({"question": question})#f"As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle A of {ang_a}. What is the value of angle B?"})
                
                d.update({"id": i})
                #if no_sol_flag:
                    #df1 = pd.concat([df1,pd.DataFrame(d)], ignore_index=True)
                #if ans !=None:
                d.update({"answer": ang_total_side[find_side]})
                df = pd.concat([df, pd.DataFrame(d)], ignore_index=True)
                r.write(json.dumps(d, indent=4))
                r.close()
                i = i+1
                
    df = df.explode(['image_path'])
    
    return df, i
