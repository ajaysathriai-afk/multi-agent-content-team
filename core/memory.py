import chromadb
from chromadb.utils import embedding_functions


class KnowledgeBase:

    def __init__(self):

        self.client = chromadb.Client()

        self.embedding = embedding_functions.DefaultEmbeddingFunction()

        self.collection = self.client.get_or_create_collection(
            name="research_memory",
            embedding_function=self.embedding
        )

        print("✅ Knowledge base initialized!")

    def store(self, topic, text):

        self.collection.add(
            documents=[text],
            ids=[topic]
        )

        print(f"📚 Stored research for: {topic}")

    def search(self, topic):

        results = self.collection.query(
            query_texts=[topic],
            n_results=2
        )

        docs = results.get("documents", [])

        if docs:
            return docs[0]

        return []