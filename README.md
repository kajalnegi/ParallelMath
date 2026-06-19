# An Evaluation of Mathematical Reasoning in (M)LLMs

This repository contains dataset and code used in the paper. 
<br>
**ParallelMath**:  The dataset ParallelMath contains pairs of geometric math problems whose questions can be solved using the properties of parallel lines, triangles, rectangles, squares, pentagons, hexagons, and trapezoids.
<br>
<br>
**NoUni**:  The dataset NoUni contains 300 samples of math problems with no solution or infinitely many solution.
<br>

A subsets from **sub-MathVista** and **sub-MATH-V** was also used in analysis.
<br>
These datasets are manually verified to ensure the question's equivalence(mathematically) remains
constant when a “flip” or “rotate by 90 degrees clockwise” transformation is applied
to the images, with the text question and answer remaining the same.
<br>

**MATHVISTA**: (https://huggingface.co/datasets/AI4Math/MathVista)
<br>

**MATH-V**: (https://huggingface.co/datasets/MathLLMs/MathVision)

<br>

For parsing the model answer following commands are used.

<br>

*python parsing_generated_output.py --input_filepath <input_filepath>* --model_answer_column <generated_response> --true_answer_column <answer>

<br>

*python no solution parse.py --input_directory input.csv --model_answer_column generated_response --true_answer_column answer*

<br>

*python parse_infinite_solution.py --input_directory input.csv --model_answer_column generated_response --true_answer_column answer*
<br>
