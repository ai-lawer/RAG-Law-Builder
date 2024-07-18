from langchain_community.vectorstores import Chroma
from create_vector_database import get_embedding_function


def query_db(query):
    db = Chroma(
        persist_directory="../chroma_openai",
        embedding_function=get_embedding_function(),
    )
    result = db.similarity_search_with_relevance_scores(query, k=3)

    content = ""

    if len(result) != 0:
        for i in range(len(result)):
            if result[i][1] >= 0.7:
                content += (
                    " " + str(i) + "- " + str(result[i][0]).split("page_content='")[1]
                )

    return content
