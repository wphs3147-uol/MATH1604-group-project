import os
import requests

def download_answer_files(cloud_url, path_to_data_folder, respondent_index):
    """Downloads answer files from a cloud URL and saves them locally with standardized filenames.

    Parameters:
        cloud_url (str): The base URL from which to download files (e.g., 'https://example.com').
        path_to_data_folder (str): The local directory where the files will be saved (e.g., 'data/').
        respondent_index (int): The total number of respondent files to download (e.g., 40).

    Raises:
        requests.RequestException: If a file cannot be downloaded due to a network issue or invalid URL.
    """
    # check if folder exists if not create it
    if not os.path.exists(path_to_data_folder):
        os.makedirs(path_to_data_folder)

    # loop over each respondent index and change name
    for i in range(1, respondent_index + 1):
        url = f"{cloud_url}/a{i}.txt"
        save_path = os.path.join(path_to_data_folder, f"answers_respondent_{i}.txt")
        if not os.path.exists(save_path):
            try:
                response = requests.get(url)
                response.raise_for_status()

                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(response.text)
                print(f"Saved: {save_path}")
                
            except requests.RequestException as e:
                print(f"Failed: {url}: {e}")
                raise

    return path_to_data_folder


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
