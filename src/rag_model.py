# from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration


# def rag_model():
#     # Initialize the RAG model and tokenizer
#     tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
#     retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="custom")
#     model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)