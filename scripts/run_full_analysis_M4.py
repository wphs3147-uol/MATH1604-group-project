'''
run_full_analysis_M4.py

This script is written by team member 4 and is responsible for running the full analysis pipeline 
for the project. It uses the collated_answers.txt file located in the output folder 
and generates two visualisations, a scatter plot showing the mean answer for each question, 
and a line plot showing how each respondent answered the questions.
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
    Reads the collated_answers.txt file and calculates the average answer for each of the 100 questions.

    It processes each respondent’s answer sequence from the file, where answers are separated by "*" symbols. 
    Unanswered questions are recorded as 0 and excluded from the average calculation. 
    The final result is a list of 100 mean values, one for each question, which will be used for visualisation.

    The parameter takes a file path which is a string data type.This string is a path to the collated_answers.txt file containing answer sequences.

    This function returns a list of 100 float values representing the mean answer per question.
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
            elif line.isdigit():
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
    This function displays a visualisation of the answer data based on the specified plot type.

    If plot_type is 1, it generates a scatter plot of the average answer per question using
    the generate_means_sequence function. If plot_type is 2, it generates a line plot for each
    respondent showing their selected answers across all 100 questions.

    Parameters taken are file_path which is a string that is the path to the collated_answers.txt file 
    and plot_type which is an integeer and it determines which type of plot to generate - 1 for scatter plot, 2 for line plot.

    Should return None. Displays the plot directly using matplotlib. I found that you need to click on exit after the initial scatter plot
    displays and then the program continues and produces the line plot and then you have to exit that before the program can complete.
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
    Main function that runs the full integration script.

    It checks if the collated_answers.txt file exists in the output folder.
    If found, it calculates mean answers, then displays both the scatter plot and line plot.
    This script avoids calling broken functions and assumes the collated data is already present.
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
