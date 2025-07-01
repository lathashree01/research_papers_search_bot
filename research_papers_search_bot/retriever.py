import logging

logging.basicConfig(level=logging.INFO)


class DocumentRetriever:
    def __init__(self, vector_store=None):
        """Initialize the DocumentRetriever with a vector store."""
        if vector_store is None:
            logging.error("Vector store is not provided.")

        self.retriever = vector_store.as_retriever(
            search_type="similarity", search_kwargs={"k": 5}
        )

    def get_relevant_documents(self, query):
        """Retrieve documents relevant to the query."""
        logging.info(f"Retrieving documents for query: {query}")

        relevant_docs = self.retriever.invoke(query)
        logging.info(f"Retrieved {len(relevant_docs)} relevant documents.")

        relevant_contents = []
        for doc in relevant_docs:
            relevant_contents.append(doc.page_content)
        return relevant_contents
