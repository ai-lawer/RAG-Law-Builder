import os
import PyPDF2


def convert_folder_pdfs_to_txt(folder_path, output_path):
    print(folder_path)
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            txt_path = os.path.join(output_path, filename[:-4] + ".txt")
            convert_pdf_to_txt(pdf_path, txt_path)


def convert_pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        with open(txt_path, "w") as txt_file:
            for page in pdf_reader.pages:
                text = page.extract_text()
                txt_file.write(text)
