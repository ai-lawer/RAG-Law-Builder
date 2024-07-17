from pdf_converter import convert_folder_pdfs_to_txt
from txt_to_csv import txt_to_csv
from combine_csvs import combine_csv
from create_fine_tune_data import create_fine_tune_data


def main():
    # convert PDF laws to txt files
    # convert_folder_pdfs_to_txt("./uae_laws_pdf/economy and business", "./uae_laws_txt/economy and business")

    # convert the txt into the csv file
    # txt_to_csv("./uae_laws_txt", False)
    # convert the arabic txt into the csv file
    # txt_to_csv("./uae_laws_txt", True)

    # combine the two CSVs
    # combine_csv('./dataset.csv', './ar_dataset.csv')

    # convert the csv into a dataset for fine-tuning
    # create_fine_tune_data(False)
    # convert the arabic csv into a dataset for fine-tuning
    # create_fine_tune_data(True)

    # combine the two fine-tune CSVs
    combine_csv("../datasets/ar_fine_tune_data.csv", "../datasets/fine_tune_data.csv")


main()


# def load_model():
#     model_name = "StevenChen16/llama3-8b-Lawyer"
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     model = AutoModelForCausalLM.from_pretrained(model_name)
#     input_text = "Your legal question here."
#     inputs = tokenizer(input_text, return_tensors="pt")
#     outputs = model.generate(**inputs)
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     print(response)
