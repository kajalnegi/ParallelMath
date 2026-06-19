#!/usr/bin/env python
# coding: utf-8

import re
import argparse
import numpy as np
import pandas as pd

def clean_column(data, col):
    data[col] = data[col].str.replace('$', '')
    data[col] = data[col].str.replace(',', '')
    data[col] = data[col].str.replace('}', '')       
    data[col] = data[col].str.split('\\').str[0]       
    data[col] = data[col].str.strip()
    data[col] = data[col].str.extract('(-?\d+)')

    return data

def extract_answer(data, column, new_column):
    def find_answer(row):
        
        split1= row[column].rsplit('####', 1)
        split2 = row[column].rsplit('\\boxed{', 1)
        split3 = row[column].rsplit('**Final Answer:**')
        split4 = row[column].rsplit('**Answer:**')
        split5 = row[column].rsplit('**')
        split6 = row[column].rsplit('\nboxed{')
        split7 = row[column].rsplit('\n\n')
        #print(len(split1))
        #print(split2)
        
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
          
        return np.nan, np.nan

    cal_col = 'calculation_'+column
    data[[cal_col, new_column]] = data.apply(find_answer,axis=1, result_type="expand")
    data[new_column] = data[new_column].str.extract('(-?\d+)')
    return data    

def main(input_file, model_answer_column, answer_column):
    if type(input_file) == str:
        df = pd.read_csv(input_file)
        if answer_column not in df:
            raise Exception(f"{input_file} does not have {answer_column} column")
    else:
        df = input_file
        #print(df.head())
    
    df = extract_answer(df, model_answer_column, f'numeric_{model_answer_column}')
    
    print("Accuracy : ", df[df[answer_column]==df[f'numeric_{model_answer_column}']].shape[0]/df.shape[0])

def load_args():
    parser = argparse.ArgumentParser(description="Parsing output for dataset")
    parser.add_argument("--input_filepath", required=True,
                        help="input csv filepath with the columns, ['answer', '*_prompt', ]")
    parser.add_argument("--answer", required=True,
                        help="name of the field for correct answer of question", default="answer")
    parser.add_argument("--model_answer_column", required=True,
                        help="column for model answer in csv file.", default="question")
    
    return vars(parser.parse_args())

if __name__ == '__main__':
    """
    sample usage:
    python parsing_generated_output.py --input_filepath input.csv --model_answer_column generated_response --answer answer
    """
    args = load_args()
    main(
        input_file=args['input_filepath'],
        model_answer_column=args['model_answer_column'],
        answer_column=args['answer']
        
    )

