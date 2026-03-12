import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()

embedding_function = embedding_functions.DefaultEmbeddingFunction()

collection = client.get_or_create_collection(
    name="research_memory",
    embedding_function=embedding_function
)


def store_research(text, source):
    collection.add(
        documents=[text],
        metadatas=[{"source": source}],
        ids=[source]
    )


def retrieve_research(query, n_results=3):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    documents = results.get("documents", [[]])[0]

    return "\n".join(documents)