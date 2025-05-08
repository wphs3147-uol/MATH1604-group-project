import os
import numpy as np
from typing import List

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

