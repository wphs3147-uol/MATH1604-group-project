import os
import requests

def download_answer_files(cloud_url, path_to_data_folder, respondent_index):
    """
    Downloads files named a1.txt, a2.txt, ..., an.txt from a cloud URL and
    saves them in the specified folder as answers_respondent_1.txt, ..., answers_respondent_n.txt.
    """
    if not os.path.exists(path_to_data_folder):
        os.makedirs(path_to_data_folder)

    for i in range(1, respondent_index + 1):
        url = f"{cloud_url}/a{i}.txt"
        save_path = os.path.join(path_to_data_folder, f"answers_respondent_{i}.txt")

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write(response.text)
        except requests.RequestException as e:
            print(f"Error downloading file {url}: {e}")


def collate_answer_files(data_folder_path):
    """
    Combines all answers_respondent_*.txt files from the given folder into
    one file called collated_answers.txt in the output/ folder.
    Each respondent's data is separated by a line containing '*'.
    """

    if not os.path.exists("output"):
        os.makedirs("output")

    output_file = os.path.join("output", "collated_answers.txt")
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
