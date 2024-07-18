from ai_chatbot import ai_chatbot
from pdf_converter import convert_folder_pdfs_to_txt
from create_vector_database import create_vector_database
from query_db import query_db
from txt_to_csv import txt_to_csv
from combine_csvs import combine_csv
from create_fine_tune_data import create_fine_tune_data


def main():
    # convert PDF laws to txt files
    # convert_folder_pdfs_to_txt(
    #     "./uae_laws_pdf/economy and business", "./uae_laws_txt/economy and business"
    # )

    # convert the txt into the csv file
    # txt_to_csv("./uae_laws_txt", False)
    # convert the arabic txt into the csv file
    # txt_to_csv("./uae_laws_txt", True)

    # combine the two CSVs
    # combine_csv("./dataset.csv", "./ar_dataset.csv")

    # convert the csv into a dataset for fine-tuning
    # create_fine_tune_data(False)
    # convert the arabic csv into a dataset for fine-tuning
    # create_fine_tune_data(True)

    # combine the two fine-tune CSVs
    # combine_csv("../datasets/ar_fine_tune_data.csv", "../datasets/fine_tune_data.csv")

    # fine-tuneing using unsloth
    # https://github.com/unslothai/unsloth/tree/main#installation-instructions

    # creating a vector database
    # create_vector_database()

    question = input("Enter your legal question\n")

    # query the vector db
    content = query_db(question)

    ai_chatbot(
        question,
        content,
    )


main()
