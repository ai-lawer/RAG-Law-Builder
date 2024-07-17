import pandas as pd
from tqdm import tqdm
import ollama
import json
import csv


def create_fine_tune_data(isAr):
    df = (
        pd.read_csv("../datasets/ar_dataset.csv", header=None)
        if isAr
        else pd.read_csv("../datasets/dataset.csv", header=None)
    )
    csv_file_path = (
        "../datasets/ar_fine_tune_data.csv"
        if isAr
        else "../datasets/fine_tune_data.csv"
    )
    fieldnames = ["instruction", "input", "output"]
    with open(csv_file_path, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    for i in tqdm(range(len(df))):
        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": f"create hypothesis case similar to real life cases, with a corresponding solution depending on this law: \"{df.iloc[i][2]}\". Your answer should only contain a json object with keys 'instruction' the question (ask as you encounter this as yourself), 'input' the complete and exact law, and 'output' the solution (answer should as 'you'). all keys should have a string value. You should mention the law article in the solution.",
                },
            ],
        )

        try:
            string = (
                "{ " + response["message"]["content"].split("{")[1].split("}")[0] + " }"
            )
            json_obj = json.loads(string)
            with open(csv_file_path, mode="a", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(
                    [json_obj["instruction"], json_obj["input"], json_obj["output"]]
                )
        except:
            with open(csv_file_path, mode="a", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["", "", ""])
