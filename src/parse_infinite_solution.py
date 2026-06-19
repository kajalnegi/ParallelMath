#!/usr/bin/env python
# coding: utf-8


import re
import argparse
import numpy as np
import pandas as pd


def in_words_detection(row):
    #text = row['generated_response_answer'].strip()
    #text = text.replace('####', '')
    text1 = row['generated_response'].strip()
    
    if '= any real number.' in text1.lower() or 'no unique solution' in text1.lower() or \
    'no consistent' in text1.lower() or 'not consistent' in text1.lower() or 'no unique solution' in text1.lower() or 'no standard solution' in text1.lower() \
    or 'true for any value of' in text1.lower() or 'infinitely many solution' in text1.lower() or 'not uniquely determined' in text1.lower():
        return 'infinite solution'
    

def find_answer(model_answer):
        
        try:
            filter_assistant = model_answer.rsplit('assistant', 1)[1]
        except IndexError:
            filter_assistant = model_answer
        if filter_assistant.endswith('####'):
            filter_assistant = filter_assistant[:-4]
        filter_assistant = filter_assistant.lower()
        
        split1= filter_assistant.rsplit('####', 1)
        #return filter_assistant, split1[1]
        split2 = filter_assistant.rsplit('\\boxed{', 1)
        split3 = filter_assistant.rsplit('final answer')
        split4 = filter_assistant.rsplit('the solution is')
        split5 = filter_assistant.rsplit('**')
        split6 = filter_assistant.rsplit('\nboxed{')
        split7 = filter_assistant.rsplit('\n\n')
        split8 = filter_assistant.rsplit('\n2.')
        
        
        if len(split1)>1: 
            
            if len(split1[0]) > len(split1[1]):
                
                return split1[0], split1[1]
            else:
                return split1[1], split1[0]
        if len(split3)>1:
           
            if len(split3[1]) > len(split3[0]):
                return split3[1], split3[0]
            else:
                return split3[0], split3[1]
        if len(split4)>1:
            
            if len(split4[1]) > len(split4[0]):
                return split4[1], split4[0]
            else:
                return split4[0], split4[1]
        
        if len(split2)>1:
            
            if len(split2[1]) > len(split2[0]):
                return split2[1], split2[0].split('}')[0]
            else:
                return split2[0],split2[1].split('}')[0]
        if len(split6)>1:
            
            if len(split6[1]) > len(split6[0]):
                return split6[1], split6[0].split('}')[0]
            else:
                return split6[0], split6[1].split('}')[0]        
        if len(split5)>1:
            
            if len(split5[1]) > len(split5[0]):
                return split5[1], split5[0].split('**')[0]
            else:
                return split5[0], split5[1].split('**')[0]
        if len(split7)>1:
            
            if len(split7[1]) > len(split7[0]):
                return split7[1], split7[0]
            else:
                return split7[0], split7[1]
        if len(split8)>1:
            
            if len(split8[1]) > len(split8[0]):
                return split8[1], split8[0]
            else:
                return split8[0], split8[1]
        
        return filter_assistant, filter_assistant

def find_end_index(ans):
    next_ind = ans.find('}\\')
    if next_ind != -1:
            pass
    else:
            next_ind = ans.find(').')
            if next_ind != -1:
                pass
            else:
                next_ind = ans.find('} \\')
                if next_ind != -1:
                    pass
                else:
                    next_ind = ans.find('.')
                    if next_ind != -1:
                        pass
                    else:
                        next_ind = len(ans)
    return next_ind

def clean_answer(ans):
    all_expression = []
    all_ind = [i for i, x in enumerate(ans) if x == "="]
    all_ind.sort(reverse=True)
    
    for last_equal_index in all_ind:
        if last_equal_index != -1:
            ans = ans[last_equal_index-2:]
            ans = ans.replace('\n', '')
            
        ans = ans.strip()
        
        if ans.endswith('.'):
            ans = ans[:-1]
        next_ind = find_end_index(ans)                          
        
        exp = ans.strip()[:next_ind]
        all_expression.append(exp)
    return all_expression
        
def segment_exp(exp):
        sign_list = []
        if '=' in exp:
            exp = exp.split('=')[-1]
        for t in exp:
            if t=='+' or t=='-':
                sign_list.append(t)
        
        segm = re.split('\+|\-', exp)
        if len(sign_list)+1==len(segm):
            #first is positive
            sign_list.insert(0, '')
        ratio = []
        letter = []
        
        for t in segm:
            
            try: 
                i = float(t)
                ratio.append(float(i))
            except ValueError:    
                try: 
                    i = t.strip()[:-1]
                    if i!='':
                        ratio.append(float(i))
                        letter.append(t[-1])
                    else:
                        ratio.append(1)
                        letter.append('')
                except ValueError:  
                    ratio.append(1)
                    letter.append('')
        if len(letter)+1==len(segm):
            
            letter.insert(0, '')
        return ratio, letter, sign_list
    
def extract_ratio(true_ans):
    frac_split = true_ans.split('/')
    if len(frac_split)>1:
        den = frac_split[-1]
    else:
        den = 1
    num = frac_split[0]
    num = num.replace('(', '')
    num = num.replace(')', '')
    coef, letter, sign_list = segment_exp(num)
    ratio = []
    for t in coef:
        
        ratio.append(float(int(t)/int(den)))
    return ratio, letter, sign_list

def convert_frac(model_answer):
    if '\frac' in model_answer:
        frac = model_answer.split('}{')
        ind2 = frac[1].find('}')
        den = frac[1][:ind2]
        ind1 = frac[0].find('\frac{')
        num = frac[0][:ind1+6]
        return num+'/'+den
        
def same_ratio(model_answer_ratio, model_answer_letter, ans_ratio, ans_letter, tol=0.01):
    flag = True
    for l in range(len(model_answer_letter)):
        for z in range(len(ans_letter)):
            if model_answer_letter[l]==ans_letter[z]:
                if abs(model_answer_ratio[l]-ans_ratio[z])<tol:
                    pass
                else:
                    flag = False
    return flag

def compare_ratio(ans, model_answer):
    #c, c1, c2, c3 = 0          
    model_answer_ratio, model_answer_letter, model_answer_sign_list = segment_exp(model_answer) 
    #print(model_answer_ratio, model_answer_letter, model_answer_sign_list)
    ans_ratio, ans_letter, ans_sign_list = extract_ratio(ans)  
    #print(ans_ratio, ans_letter, ans_sign_list)
    match_or_not = same_ratio(model_answer_ratio, model_answer_letter, ans_ratio, ans_letter)
    return match_or_not
    
def exact_match(true_answer, model_answer):
    if true_answer in model_answer:
        return True
    true_answer = true_answer.replace(' ', '')
    model_answer = model_answer.replace(' ', '')
    if true_answer in model_answer:
        return True

def remake_true_answer_match(true_answer, model_answer):
    model_answer = model_answer.replace(' ' ,'')
    true_answer1 = true_answer.replace('(', '\\(')
    true_answer1 = true_answer1.replace(')', '\\)')
    true_answer1 = true_answer1.replace(' ' ,'')
    true_answer2 = true_answer.replace('(', '\frac{')
    true_answer2 = true_answer2.replace(')/', '}{')
    true_answer2 = true_answer2.replace(' ' ,'')
    #print(true_answer2, true_answer2 in model_answer,model_answer)
    if true_answer1 in model_answer or true_answer2 in model_answer:
        
        return True
                                                
    
def check_if_true_answer_arrived(row):
    true_answer = row['answer']
    model_answer = row['generated_response']
    #print(model_answer)
    all_matches = []
    match_or_not = remake_true_answer_match(true_answer, model_answer)
    all_matches.append(match_or_not)
    if match_or_not:
        return match_or_not
    model_answer, hash_split = find_answer(model_answer)
    #print(true_answer, model_answer)
    all_expression = clean_answer(model_answer)
    #print(all_expression)
    for model_answer1 in all_expression:
        match_or_not = exact_match(true_answer, model_answer1)
        all_matches.append(match_or_not)
    for model_answer1 in all_expression:
        match_or_not =  compare_ratio(true_answer, model_answer1)
        all_matches.append(match_or_not)   
    return any(all_matches)



def load_args():
    parser = argparse.ArgumentParser(description="Generating math geometry questions with images")
    
    parser.add_argument("--input_directory", required=True,
                        help="input csv file for model generated answer.")
    parser.add_argument("--model_answer_column", required=True,
                        help="column in the input_directory for model answer.")
    
    return vars(parser.parse_args())

def main(input_dir, model_answer_column, true_answer_column):
    df = pd.read_csv(input_dir)
    column = model_answer_column
    new_column = 'generated_response_answer'
    df[true_answer_column] = df[true_answer_column].str.strip()
    df[new_column] = df[[true_answer_column, column]].apply(check_if_true_answer_arrived, axis=1, result_type="expand")
    df['cardinality'] = df.apply(in_words_detection, axis=1, result_type="expand")

    
    print("---- Correct answer count ----------", df[df[new_column]==True].shape[0])

    print("---- Correct cardinality detection percentage  ----------",df[~df['cardinality'].isnull()].shape[0]/df.shape[0])



if __name__ == '__main__':
    """
    sample usage:
    python parse_infinite_solution.py --input_directory input.csv --model_answer_column generated_response --true_answer_column answer
    
    """
    args = load_args()
    main(
        
        input_dir=args['input_directory'],
        model_answer_column=args['model_answer_column'],
        true_answer_column= args['true_answer_column']
        
    )

