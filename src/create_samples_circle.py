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



def create_parallel_lines_circle(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    font = ImageFont.load_default(13)
    draw.line(((50, 150), (200, 150), (350,150) ), fill=fill, width=2)
    draw.text((50, 160), 'L1', font=font, fill=(0, 0, 0))
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    
    if angle>=45:
        ref_point = (200, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((50, 250), (200, 250), (350,250)), fill=fill, width=2)
        draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.circle((200, 200), 110, outline=fill, width=2)
    elif angle<45:
        ref_point = (150, 150)
        points = get_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((50, 250), (200, 250), (350,250)), fill=fill, width=2)
        draw.text((50, 270), 'L2', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='horizontal')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.circle((200, 200), 110, outline=fill, width=2)

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


def create_rotate90_parallel_lines_circle(draw, center, size, angle, fill, angle_type='co_interior', position=4):
    """Draw a pair of parallel lines."""
    draw.line(((150, 50), (150, 200), (150, 350) ), fill=fill, width=2)
    #draw.line(((50, 250), (200, 250), (350,250)), fill=fill,)
    font = ImageFont.load_default(13)
    draw.text((130, 50), 'L2', font=font, fill=(0, 0, 0))
    if angle>=45:
        ref_point = (100, 200)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((250, 50), (250, 200), (250, 350)), fill=fill, width=2)
        draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.circle((200, 200), 110, outline=fill, width=2)

    elif angle<45:
        ref_point = (170, 250)
        points = get_vertical_coords(ref_point[0], ref_point[1], angle, 400, 400)
        draw.line(((250, 50), (250, 200), (250, 350)), fill=fill, width=2)
        draw.text((230, 50), 'L1', font=font, fill=(0, 0, 0))
        pos_a, pos_b = text_position(angle_type, angle, position, parallel_line='vertical')
        draw.text(pos_a, 'A', font=font, fill=(0, 0, 0))
        draw.text(pos_b, 'B', font=font, fill=(0, 0, 0))
        draw.circle((200, 200), 110, outline=fill, width=2)
        
    #print(points)
    draw.line(points, fill=fill, width=2)
    #font = ImageFont.load_default()
    #draw.text((ref_point[0], ref_point[1]), 'A', font=font, fill=(0, 0, 0))
    #draw.line(points, fill=fill)


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


sentences_type = [

"In the diagram, lines L1 and L2 are parallel, and a transversal intersects both, creating an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "As shown in the figure, lines L1 and L2 are parallel to each other, and another line cuts both lines, forming an angle {given_letter} of {ang_}. What is the value of angle {find_letter}?"
, "In the figure, lines L1 and L2 are parallel, and a transversal intersects them, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "As illustrated, lines L1 and L2 are parallel, and a third line intersects both, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the diagram, lines L1 and L2 are parallel, and a line crosses both, forming a {ang_} angle at point {given_letter}. What is the measure of angle {find_letter}?"
, "Lines L1 and L2 are parallel, and a transversal intersects them, forming a {ang_} angle labeled {given_letter}. Find the measure of angle {find_letter}."
, "As shown in the diagram, a transversal intersects the parallel lines L1 and L2, forming a {ang_} angle labeled {given_letter}. What is the measure of angle {find_letter}?"
, "The figure shows a transversal crossing two parallel lines, L1 and L2, creating a {ang_} angle labeled {given_letter}. What is the value of angle {find_letter}?"
, "In the figure, lines L1 and L2 are parallel, and a transversal cuts across them, forming an angle {given_letter} of {ang_}. What is the measure of angle {find_letter}?"
, "As depicted, lines L1 and L2 are parallel, and a line intersecting both creates an angle {given_letter} measuring {ang_}. What is the measure of angle {find_letter}?"
, "In the given figure, a line intersects the parallel lines L1 and L2, forming a {ang_} angle labeled {given_letter}. Determine the measure of angle {find_letter}."
, "The diagram shows two parallel lines, L1 and L2, being intersected by another line, forming a {ang_} angle at point {given_letter}. What is the value of angle {find_letter}?"
, "Lines L1 and L2 are parallel and are intersected by a third line, forming a {ang_} angle marked as {given_letter}. What is the measure of angle {find_letter}?"
,"A transversal crosses two parallel lines, L1 and L2, creating a {ang_} angle labeled {given_letter}. What is the corresponding angle {find_letter}?"
]




def generate_samples_circle(output_dir, i, no_solution=False):
    #i = 0
    df = pd.DataFrame(columns=['id', 'image_path', 'question', 'answer', ])
    angles = list(range(40,121,30))
    for pos, ang_type in position_angle_type.items():
        for ang_t in ang_type:
            for ang in angles:
                data1 = 'data_1.json'
                data2 = 'data_2.json'
                ang_a, ang_b = find_answer(ang, ang_t, pos)
                directory = f"{ang_t}_{ang}_pos_{pos}"
                os.mkdir(output_dir+directory)
                draw, center, size, fill, img = define_canvas()
                create_parallel_lines_circle(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/vertical.png"
                display(img)
                img.save(filename)
                draw, center, size, fill, img = define_canvas()
                create_rotate90_parallel_lines_circle(draw, center, size, ang, fill, angle_type=ang_t, position=pos)
                filename = f"{output_dir}{directory}/horizontal.png"
                display(img)
                img.save(filename)
                print(f"Saved: {filename}")
                #os.remove(f"{output_dir}{directory}/"+'data.json')
                r = open(f"{output_dir}{directory}/"+data1, 'w')
                d = dict()
                question = random.choice(sentences_type).format(given_letter = "A", find_letter = "B",
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
                question = random.choice(sentences_type).format(given_letter = "B", find_letter = "A",
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
