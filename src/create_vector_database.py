from dotenv import dotenv_values
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import pandas as pd


def create_vector_database():
    chunks = create_chunks()

    create_chroma(chunks)


def create_chunks():
    chunks = []
    df = pd.read_csv("../datasets/combined_datasets.csv", header=None)
    for i in range(len(df)):
        chunks.append(
            f"Law Category: {df.iloc[i][0]}, Law Name: {df.iloc[i][1]}, Law Content: {df.iloc[i][2]}"
        )
    return chunks


def create_chroma(chunks):
    db = Chroma(
        persist_directory="chroma_openai", embedding_function=get_embedding_function()
    )

    db.add_texts(chunks)


def get_embedding_function():
    env_variables = dotenv_values()

    embeddings = OpenAIEmbeddings(openai_api_key=env_variables["OPEN_AI_KEY"])
    return embeddings
