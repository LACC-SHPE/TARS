from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

from core.QueryManager import QueryManager
from logger import TarsLogger

import settings
import os


class GPTAgent:
    def __init__(self, logging: TarsLogger, vectordb, temperature=0.5):
        self.logging = logging
        self.vectordb = vectordb
        self.temperature = temperature
        self.bot = None

    def setup(self):
        self.bot = ChatOpenAI(
            temperature=self.temperature,
        )

    def ask(self, question):
        results = QueryManager.relevancy_check(self, question)
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

        prompt = PromptTemplate(
            template=settings.ASK_TEMPLATE,
            input_variables=["question"],
            partial_variables={"context": context_text},
        )

        parser = StrOutputParser()

        chain = RunnablePassthrough() | prompt | self.bot | parser

        rag_chain_with_source = RunnableParallel(
            {"context": self.vectordb.as_retriever(), "question": RunnablePassthrough()}
        ).assign(answer=chain)

        output = {}

        # Run the chain in streaming mode to get the answer in real time
        # Only compatible with NLUX. Using Postman for testing may not be ideal. Alternatively,
        # You can use the test.py file for testing.
        curr_key = None
        for chunk in rag_chain_with_source.stream(question):
            for key in chunk:
                if key not in output:
                    output[key] = chunk[key]
                else:
                    output[key] += chunk[key]
                if key == "answer":
                    answer = f"{chunk[key]}"
                    yield answer
