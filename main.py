from transformers import AutoModelForCausalLM, AutoTokenizer
import pandas as pd
from pdf_converter import convert_folder_pdfs_to_txt
from txt_to_csv import txt_to_csv


def load_model():
    model_name = "StevenChen16/llama3-8b-Lawyer"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    input_text = "Your legal question here."
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(response)


def main():
    # convert PDF laws to txt files
    # convert_folder_pdfs_to_txt("./uae_laws_pdf/economy and business", "./uae_laws_txt/economy and business")

    # convert the txt into the csv file
    txt_to_csv("./uae_laws_txt")


main()
