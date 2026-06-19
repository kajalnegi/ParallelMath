#!/usr/bin/env python
# coding: utf-8


import re
import argparse
import numpy as np
import pandas as pd


def extract_answer(data, column, new_column):
    def find_answer(row):
        #print(row[column])#, row[1], row[3], row[4])
        #row = " ####"
        try:
            filter_assistant = row[column].rsplit('assistant', 1)[1]
        except IndexError:
            filter_assistant = row[column]
        if filter_assistant.endswith('####'):
            filter_assistant = filter_assistant[:-4]
        split1= filter_assistant.rsplit('####', 1)
        split2 = filter_assistant.rsplit('\\boxed{', 1)
        split3 = filter_assistant.rsplit('Final Answer')
        split4 = filter_assistant.rsplit('**Answer:**')
        split5 = filter_assistant.rsplit('**')
        split6 = filter_assistant.rsplit('\nboxed{')
        split7 = filter_assistant.rsplit('\n\n')
        split8 = filter_assistant.rsplit('\n2.')
        
        
        if len(split1)>1: 
            #print(split1)
            if len(split1[0]) > len(split1[1]):
                #print("im here")
                return split1[0], split1[1]
            else:
                return split1[1], split1[0]
        if len(split3)>1:
            #print(split3)
            if len(split3[1]) > len(split3[0]):
                return split3[1], split3[0]
            else:
                return split3[0], split3[1]
        if len(split4)>1:
            #print(split4)
            if len(split4[1]) > len(split4[0]):
                return split4[1], split4[0]
            else:
                return split4[0], split4[1]
        
        if len(split2)>1:
            #print(split2)
            if len(split2[1]) > len(split2[0]):
                return split2[1], split2[0].split('}')[0]
            else:
                return split2[0],split2[1].split('}')[0]
        if len(split6)>1:
            #print(split6)
            if len(split6[1]) > len(split6[0]):
                return split6[1], split6[0].split('}')[0]
            else:
                return split6[0], split6[1].split('}')[0]        
        if len(split5)>1:
            #print(split5)
            if len(split5[1]) > len(split5[0]):
                return split5[1], split5[0].split('**')[0]
            else:
                return split5[0], split5[1].split('**')[0]
        if len(split7)>1:
            #print(split7)
            if len(split7[1]) > len(split7[0]):
                return split7[1], split7[0]
            else:
                return split7[0], split7[1]
        if len(split8)>1:
            #print(split7)
            if len(split8[1]) > len(split8[0]):
                return split8[1], split8[0]
            else:
                return split8[0], split8[1]
          
        return filter_assistant, filter_assistant
            
    cal_col = 'calculation_'+column
    
    
    data[[cal_col, new_column]] = data.apply(find_answer,axis=1, result_type="expand")
    data[new_column] = data[new_column].str.strip()
    
    return data   


def clean_answer(row):
    text = row['generated_response_answer'].strip()
    text = text.replace('####', '')
    text1 = row['generated_response'].strip()
    if 'no solution' in text1.lower() or 'undefined' in text1.lower() or 'no valid numeric solution' in text1.lower()\
    or 'there is no value' in text1.lower() or 'contradiction' in text1.lower():
        return "no solution"
    return text.lower()


def main(input_dir, model_answer_column, true_answer_column):
    df = pd.read_csv(input_dir)
    #print(df)
    column = model_answer_column
    new_column = 'generated_response_answer'
    column = 'generated_response'
    new_column = 'generated_response_answer'
    df = extract_answer(df, column, new_column)
    df[true_answer_column] = df[true_answer_column].str.strip()
    
    df['small_clean_answer'] = df.apply(clean_answer, axis=1, result_type="expand")
    
    print("---- Correct answer count ----------", df[df['small_clean_answer']==df[true_answer_column]].shape[0])

def load_args():
    parser = argparse.ArgumentParser(description="Generating math geometry questions with images")
    
    parser.add_argument("--input_directory", required=True,
                        help="input csv file for model generated answer.")
    parser.add_argument("--model_answer_column", required=True,
                        help="column in the input_directory for model answer.")
                       
    parser.add_argument("--true_answer_column", required=True,
                        help="column in the input_directory for true answer.")
    
    return vars(parser.parse_args())


if __name__ == '__main__':
    """
    sample usage:
    python parse_no_solution.py --input_directory input.csv --model_answer_column generated_response --true_answer_column answer
    
    """
    args = load_args()
    main(
        
        input_dir=args['input_directory'],
        model_answer_column=args['model_answer_column'],
        true_answer_column= args['true_answer_column']
    )

