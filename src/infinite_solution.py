#!/usr/bin/env python
# coding: utf-8

import os
import shutil
import json
import random
import argparse
import pandas as pd
from datasets import load_dataset


def find_answer(n_l, int_list, sign_list):
    answer = dict()
    #print(n_l, int_list, sign_list)
    for l in n_l:
        s = ''
        s = s + str(int_list[-1]) 
        d = ''
        sgn = ''
        for i in range(len(int_list)):
            if i>= len(n_l):
                continue
            if n_l[i] == l:
                d = int_list[i]
                sgn = sign_list[i].strip()
                continue
            if sign_list[i] == '+' or sign_list[i] == '':
                s = s +' - '+ str(int_list[i])+n_l[i]
            if sign_list[i] == '-':
                s = s +' + '+ str(int_list[i])+n_l[i]
        if sgn == '+':
            s = '(' + s + ')/'+ str(d)
        else:          
            s = sgn + '(' + s + ')/'+ str(d)
        answer[l] = s
    #print(answer)
    return answer


letters = ['p', 'q', 'r', 's', 't', 'u', 'v', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
signs = ['+', '-']
def make_equations(n=2):
    equ_list = []
    n_l = random.sample(letters, n)
    f_eq = ''
    s_eq = ''
    int_list = []
    sign_list = []
    sign_list.append('')
    for t in range(n):
        z = random.randint(1, 50)
        int_list.append(z)
        s = random.choice(signs)
        sign_list.append(s)
        f_eq = f_eq + str(z)+n_l[t]+' '+ s +' ' 
    z = random.randint(1, 50)
    int_list.append(z)
    f_eq = f_eq[:-2] +  '= '+ str(z)
    #print(f_eq)#, int_list, n_l)
    equ_list.append(f_eq)
    r = random.randint(2, 5)
    for t in range(n):
        s_eq = s_eq + sign_list[t]+' ' + str(int_list[t]*r)+n_l[t]+' '
    s_eq = s_eq[:-1] +  ' = '+ str(int_list[-1]*r)
    #print(s_eq)
    equ_list.append(s_eq)
    ans = find_answer(n_l, int_list, sign_list)
    #question = 
    if n >2:
        th_eq = ''
        r = random.randint(5,7)
        for t in range(n):
            th_eq = th_eq +  sign_list[t]+' ' +str(int_list[t]*r)+n_l[t]+' '
        th_eq = th_eq[:-1] +  ' = '+ str(int_list[-1]*r)
        equ_list.append(th_eq)
    return equ_list, ans

def make_infinite_quest(i, q, f, output_dir, k):
    dst = output_dir+ str(i)
    #print(dst)
    os.mkdir(dst)
    data = dict()
    data["image_path"] = 'NA'
    data["question"] = "If " + q+ ". Find "+f+'.'
    data['id'] = i 
    data["answer"] =  k#"cannot be determined"#"no solution"
    data["solution cardinality"] = '$\infty$'
    data["solution space"]= '$\mathbb{R}$' 
    #print(data["question"], " ", k)
    r = open(dst+'/data.json', 'w')
    r.write(json.dumps(data, indent=4))
    r.close()
    return data

def main(output_dir, n_samples):
    i = 1000
    n_samples = int(n_samples)
    init = i
    
    df_1 = pd.DataFrame(columns=["image_path", "question", "id", "solution cardinality", "answer", "solution space"])
    for n in [2,3]:
        for _ in range(n_samples):
            equ_list, ans = make_equations(n)
            for k1,v in ans.items():
                if i - init == n_samples:
                    break
                data = make_infinite_quest(i, ", ".join(equ_list), k1,output_dir, v)
                df_1 = pd.concat([df_1, pd.DataFrame([data])], ignore_index=True)
                i = i+1
                
            if i - init == n_samples:
                break
        if i - init == n_samples:
            break

    df_1['image_path'] = df_1['image_path'].fillna('NA')

   
    df_1.to_csv(output_dir+'input.csv', index=False)


def load_args():
    parser = argparse.ArgumentParser(description="Generating math geometry questions with images")
    
    parser.add_argument("--output_directory", required=True,
                        help="output directory for local output dump")
    parser.add_argument("--n_samples", required=True,
                        help="number of samples to be generated.")
    
    return vars(parser.parse_args())

if __name__ == '__main__':
    """
    sample usage:
    python infinite_solution.py --output_directory . --n_samples 5
    
    """
    args = load_args()
    main(
        
        output_dir=args['output_directory'],
        n_samples=args['n_samples']
    )
