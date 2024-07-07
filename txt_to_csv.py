import re
import csv
import os


def txt_to_csv(folder_path):
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        process_txts_in_folder(file_path)


def process_txts_in_folder(folder_path):
    csv_file = get_dataset_file("dataset.csv")

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)

            content = get_txt_content(file_path)

            indices = get_matches_indices(content)

            fill_csv_from_txt(indices, csv_file, folder_path, file_name, content)


def get_dataset_file(csv_file):
    if os.path.exists(csv_file):
        return csv_file

    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(
            [
                [
                    "Law kind",
                    "Law date & authority",
                    "Content",
                ]
            ]
        )
        return csv_file


def get_txt_content(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content


def get_matches_indices(content):
    previous_number = 0
    indices = []
    matches = re.finditer(
        r"Article \(\s*(\d+)\s*\)",
        content,
    )
    for match in matches:
        number = int(match.group(1))
        if number == previous_number + 1:
            indices.append(match.start())
            previous_number = number

    return indices


def fill_csv_from_txt(indices, csv_file, folder_path, file_name, content):
    for i in range(len(indices)):
        if i < len(indices) - 1:
            with open(csv_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(
                    [
                        [
                            f"{folder_path.split('/')[2]}",
                            f"{file_name.split('.txt')[0]}",
                            content[indices[i] : indices[i + 1]],
                        ]
                    ]
                )
        else:
            with open(csv_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(
                    [
                        [
                            f"{folder_path.split('/')[2]}",
                            f"{file_name.split('.txt')[0]}",
                            content[indices[i] : len(content)],
                        ]
                    ]
                )
