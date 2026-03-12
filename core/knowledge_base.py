from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


class KnowledgeBase:

    def __init__(self):

        self.db = Chroma(
            collection_name="articles",
            embedding_function=OpenAIEmbeddings(),
            persist_directory="research_db"
        )

        print("✅ Knowledge base initialized!")

    def add_document(self, data):

        self.db.add_texts(
            [data["content"]],
            metadatas=[{"topic": data["topic"]}]
        )