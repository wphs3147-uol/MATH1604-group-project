import os
import numpy as np
from typing import List

def extract_answers_sequence(......)

def generate_means_sequence(data_folder_path: str) -> List[float]:
    
    question_data = [[] for _ in range(100)]

    for filename in sorted(os.listdir(data_folder_path)):
        if filename.startswith("answers_respondent_") and filename.endswith(".txt"):
            file_path = os.path.join(data_folder_path, filename)
            answers = extract_answers_sequence(file_path)

            for i, ans in enumerate(answers):
                if ans != 0:  
                    question_data[i].append(ans)

    means_sequence = []
    for answers in question_data:
        if answers:
            means_sequence.append(float(np.mean(answers)))
        else:
            means_sequence.append(0.0) 

    return means_sequence

import matplotlib.pyplot as plt

def visualize_data(data_folder_path: str, n: int) -> None:
    if n == 1:
        means = generate_means_sequence(data_folder_path)
        plt.figure(figsize=(12, 5))
        plt.scatter(range(1, 101), means, color='red', alpha=0.7)
        plt.title("Average answers on scatter plot")
        plt.xlabel("Question Number")
        plt.ylabel("Mean Answer")
        plt.grid(True)
        plt.show()

    elif n == 2:
        plt.figure(figsize=(12, 6))
        for filename in sorted(os.listdir(data_folder_path)):
            if filename.startswith("answers_respondent_") and filename.endswith(".txt"):
                file_path = os.path.join(data_folder_path, filename)
                answers = extract_answers_sequence(file_path)
                plt.plot(range(1, 101), answers, alpha=0.5, label=filename)
        plt.title("Respondence on Line Plot")
        plt.xlabel("Question Number")
        plt.ylabel("Answer")
        plt.grid(True)
        plt.show()

    else:
        print("n must be 1 or 2!")
