import os
import requests

import os

def download_answer_files(cloud_url, path_to_data_folder, respondent_index):
    """Simulates downloading answer files by copying from a local folder instead of downloading from the cloud."""

    source_folder = cloud_url  # here, cloud_url acts like the path to the local folder (e.g., "quiz_answers_named_a1_to_a25")

    if not os.path.exists(path_to_data_folder):
        os.makedirs(path_to_data_folder)

    for i in range(1, respondent_index + 1):
        src_file = os.path.join(source_folder, f"a{i}.txt")
        dst_file = os.path.join(path_to_data_folder, f"answers_respondent_{i}.txt")

        if os.path.exists(src_file):
            with open(src_file, 'r', encoding='utf-8') as src, open(dst_file, 'w', encoding='utf-8') as dst:
                dst.write(src.read())
            print(f"Copied: {src_file} → {dst_file}")
        else:
            print(f"Missing: {src_file}")


def collate_answer_files(data_folder_path):
    """Collates all individual respondent answer files into a single file.

Parameters:
    data_folder_path (str): Path to the folder containing 'answers_respondent_*.txt' files.

Creates:
    A file named 'collated_answers.txt' in the 'output/' folder, with each respondent's
    data separated by a line containing a single asterisk '*'.

    """
    if not os.path.exists("output"):
        os.makedirs("output")

    output_file = "output/collated_answers.txt"
    #open output file in writer mode
    with open(output_file, "w", encoding="utf-8") as out_file:
        i = 1

        while True:
            file_path = os.path.join(data_folder_path, f"answers_respondent_{i}.txt")
            if not os.path.exists(file_path):
                break

            with open(file_path, "r", encoding="utf-8") as f:
                out_file.write(f.read().strip())

            out_file.write("\n*\n")
            i += 1

    print(f"Collated answers saved in {output_file}")
    return output_file

download_answer_files("quiz_answers_named_a1_to_a25", "data", 25)
collate_answer_files("data")
