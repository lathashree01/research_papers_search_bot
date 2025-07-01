import os
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS


class VectorStore:
    def __init__(self, model_name="all-MiniLM-L6-v2", path="vector_store"):
        self.model_name = model_name
        self.embedding_model = HuggingFaceEmbeddings(model_name=model_name)
        self.vector_store = None
        self.path = path

    def create_vector_store(self):
        """Create a vector store using FAISS with the specified embedding model.
        Returns:
            FAISS: An instance of the FAISS vector store.
        """
        index = faiss.IndexFlatL2(len(self.embedding_model.embed_query("hello world")))

        self.vector_store = FAISS(
            embedding_function=self.embedding_model,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )
        return self.vector_store

    def add_documents(self, documents):
        """Add documents to the vector store.

        Args:
            documents (list): A list of Document objects to be added to the vector store.
        """
        if self.vector_store is None:
            self.create_vector_store()

        uuids = [str(i) for i in range(len(documents))]
        self.vector_store.add_documents(documents=documents, uuids=uuids)
        return self.vector_store

    def get_vector_store(self):
        """Return the vector store."""
        return self.vector_store

    def save_vector_store(self, path):
        """Save the vector store to the specified path."""
        if self.vector_store is not None:
            self.vector_store.save_local(path)
        else:
            raise ValueError("Vector store is not created yet. Please create it before saving.")

    def load_vector_store(self, path):
        """Load the vector store from the specified path."""
        if os.path.exists(path):
            self.path = path
            self.vector_store = FAISS.load_local(path, self.embedding_model)
        else:
            raise FileNotFoundError(f"The specified path {path} does not exist.")
