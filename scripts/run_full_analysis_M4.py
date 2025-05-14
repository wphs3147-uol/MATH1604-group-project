'''
This script runs the full analysis pipeline for the data.
It uses collated_answers.txt from the output folder.
It makes a scatter plot of the average answers and a line plot showing what each respondent answered.
'''

import os
import matplotlib.pyplot as plt
import numpy as np

# import functions from other team members (commented out because they didn’t work as expected)
# from scripts.data_preparation_M2 import collate_answer_files  # this function tried to download from a url and didn’t match the expected input/output
# from scripts.data_extraction_M1 import extract_answers_sequence  # this one had a bug using .lower() on a list so it crashed
# from scripts.data_analysis_M3 import generate_means_sequence, visualize_data  # this one expected a folder instead of the actual collated_answers.txt file and threw a NotADirectoryError
collated_file_path = os.path.join("output", "collated_answers.txt")

#my own version of the function
def generate_means_sequence(file_path):
    '''
    this reads the collated_answers.txt file and works out the average answer for each question
    '''
    question_data = [[] for _ in range(100)]
    respondent_answers = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '*':
                for i, ans in enumerate(respondent_answers):
                    if ans != 0:
                        question_data[i].append(ans)
                respondent_answers = []
            elif line:
                respondent_answers.append(int(line))

    means_sequence = []
    for answers in question_data:
        if answers:
            means_sequence.append(float(np.mean(answers)))
        else:
            means_sequence.append(0.0)
    return means_sequence

#I also made my own visualisation function

def visualize_data(file_path, plot_type):
    '''
    this shows either the average answer per question or each respondent's answers
    plot_type 1 = scatter plot of averages
    plot_type 2 = line plot per respondent
    '''
    if plot_type == 1:
        means = generate_means_sequence(file_path)
        plt.figure(figsize=(12, 5))
        plt.scatter(range(1, 101), means, color='blue', alpha=0.6)
        plt.title("mean answer per question")
        plt.xlabel("question number")
        plt.ylabel("mean answer")
        plt.grid(True)
        plt.show()

    elif plot_type == 2:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        all_responses = []
        respondent = []
        for line in lines:
            line = line.strip()
            if line == '*':
                all_responses.append(respondent)
                respondent = []
            elif line:
                respondent.append(int(line))

        plt.figure(figsize=(12, 5))
        for r in all_responses:
            plt.plot(range(1, len(r) + 1), r, alpha=0.5)
        plt.title("answer patterns per respondent")
        plt.xlabel("question number")
        plt.ylabel("answer selected")
        plt.grid(True)
        plt.show()
    else:
        print("invalid plot_type: choose 1 or 2")


# Main fucntion
def main():
    '''
    this runs the script and shows both plots
    '''
    print("running tm4 integration script...")

    if not os.path.exists(collated_file_path):
        print("collated_answers.txt not found in output folder")
        return

    print("generating mean answer sequence...")
    means = generate_means_sequence(collated_file_path)
    print("first 5 mean values:", means[:5])

    print("showing scatter plot of averages...")
    visualize_data(collated_file_path, 1)

    print("showing line plot of respondents...")
    visualize_data(collated_file_path, 2)

    print("done.")

if __name__ == "__main__":
    main()
