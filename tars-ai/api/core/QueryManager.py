class QueryManager:
    def __init__(self, vectordb):
        self.vectordb = vectordb

    def relevancy_check(self, query):
        results = self.vectordb.similarity_search_with_relevance_scores(query, k=5)

        try:
            if len(results) == 0 or results[0][1] < 0.7:
                print("Unable to find matching results")
        except:
            return "Unable to find matching results"

        return results
