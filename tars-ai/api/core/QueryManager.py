from logger import TarsLogger


class QueryManager:
    def __init__(self, vectordb, logging: TarsLogger):
        self.vectordb = vectordb
        self.logging = logging

    def relevancy_check(self, query):
        results = self.vectordb.similarity_search_with_relevance_scores(query, k=5)

        try:
            if len(results) == 0 or results[0][1] < 0.7:
                self.logging.error(
                    "Unable to find matching results or context is limited. It doesn't necessarily mean that the context is inaccurate."
                )
        except:
            return "Unable to find matching results"

        return results
