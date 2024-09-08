from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from logger import TarsLogger
import os
import shutil


class EmbeddingManager:
    def __init__(self, all_sections, logging: TarsLogger, persist_directory="db"):
        self.all_sections = all_sections
        self.persist_directory = persist_directory
        self.vectordb = None
        self.logging = logging

    def create_and_persist_embeddings(self):
        # if os.path.exists(self.persist_directory):
        #     shutil.rmtree(self.persist_directory)

        embedding = OpenAIEmbeddings()
        self.vectordb = Chroma.from_documents(
            documents=self.all_sections,
            embedding=embedding,
            persist_directory=self.persist_directory,
        )

        self.logging.info(
            f"[TARS] Saved {len(self.all_sections)} chunks to {self.persist_directory}"
        )
        self.vectordb.persist()
