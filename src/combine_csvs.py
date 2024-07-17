import pandas as pd


def combine_csv(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    combined_df = pd.concat([df1, df2], ignore_index=True)

    combined_df.to_csv("combined_fine_tune_datasets.csv", index=False)
