#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import pandas as pd
from create_samples_two_lines import generate_samples_two_lines
from create_samples_poly import generate_samples_pentagon, generate_samples_triangle, generate_samples_hexagon, generate_samples_trapezoid, generate_samples_rectangle, generate_samples_square
from create_samples_congr import generate_samples_triangle_lines 
from create_samples_circle import generate_samples_circle
from create_samples_parallel_lines import generate_samples_parallel_lines


def main(output_dir):
    if os.path.exists(output_dir):
        os.mkdir(output_dir+'circle/')
        os.mkdir(output_dir+'similar_triangle/')
        os.mkdir(output_dir+'parallel_lines/')
        os.mkdir(output_dir+'two_lines/')
        os.mkdir(output_dir+'pentagon/')
        os.mkdir(output_dir+'triangle/')
        os.mkdir(output_dir+'hexagon/')
        os.mkdir(output_dir+'trapezoid/')
        os.mkdir(output_dir+'rectangle/')
        os.mkdir(output_dir+'square/')
    else:
        try:
            os.mkdir(output_dir)
            os.mkdir(output_dir+'circle/')
            os.mkdir(output_dir+'similar_triangle/')
            os.mkdir(output_dir+'parallel_lines/')
            os.mkdir(output_dir+'two_lines/')
            os.mkdir(output_dir+'pentagon/')
            os.mkdir(output_dir+'triangle/')
            os.mkdir(output_dir+'hexagon/')
            os.mkdir(output_dir+'trapezoid/')
            os.mkdir(output_dir+'rectangle/')
            os.mkdir(output_dir+'square/')
        except OSError:
            raise Exception(f"No such {output_dir} directory exists.")
        
    i = 0
    df_1, i = generate_samples_circle(output_dir+'circle/', i)
    df_2, i = generate_samples_triangle_lines(output_dir+'similar_triangle/', i)
    df_3, i = generate_samples_parallel_lines(output_dir+'parallel_lines/', i)
    df_4, i = generate_samples_two_lines(output_dir+'two_lines/', i)
    df_5, i = generate_samples_pentagon(output_dir+'pentagon/', i)
    df_6, i = generate_samples_triangle(output_dir+'triangle/', i)
    df_7, i = generate_samples_hexagon(output_dir+'hexagon/', i)
    df_8, i = generate_samples_trapezoid(output_dir+'trapezoid/', i)
    df_9, i = generate_samples_rectangle(output_dir+'rectangle/', i)
    df_10, i = generate_samples_square(output_dir+'square/', i)
    df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10], ignore_index=False)
    df.to_csv(output_dir+'input.csv', index=False)



def load_args():
    parser = argparse.ArgumentParser(description="Generating math geometry questions with images")
    
    parser.add_argument("--output_directory", required=True,
                        help="output directory for local output dump")
    
    return vars(parser.parse_args())

if __name__ == '__main__':
    """
    sample usage:
    python create_samples_geometry.py --output_directory ./datasets/
    
    """
    args = load_args()
    main(
        #input_filepath=args['input_filepath'],
        output_dir=args['output_directory'],
        #header=args['header'],
        #model_id=args['model_id'],
        #model_type=args["model_type"],
        #batch_size=args["batch_size"],
        #tp_size=args["tp_size"],
        #seed=args["seed"],
        #level=args["level"],
        #answer_column=args['answer']
    )
