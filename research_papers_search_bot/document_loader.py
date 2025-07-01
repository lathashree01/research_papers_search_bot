import pandas as pd
import pickle
from langchain_core.documents import Document


class DocumentLoader:
    def __init__(self, file_path=None):
        """Initialize the DocumentLoader with a file path."""
        self.documents = []
        self.metadata = []
        self.file_path = file_path

    def load_documents(self, df=None):
        """Load documents from a CSV file and return them as a list of Document objects."""
        if df is None:
            df = pd.read_csv(self.file_path)
        print("df cols:", df.columns)
        custom_documents = []
        custom_metadata = []

        for idx, row in df.iterrows():
            content = f"Title: {row['titles']}\nSummary: {row['summaries']}"
            metadata = {"terms": row.get("terms", ""), "row": idx}
            custom_documents.append(Document(page_content=content, metadata=metadata))
            custom_metadata.append(metadata)

        self.documents = custom_documents
        self.metadata = custom_metadata
        return self.documents, self.metadata

    def get_documents(self):
        """Return the loaded documents."""
        return self.documents

    def get_metadata(self):
        """Return the metadata associated with the documents."""
        return self.metadata

    def save_documents_to_location(self, output_path):
        """Save the documents and metadata to a pickle file."""
        with open(output_path, "wb") as f:
            pickle.dump((self.documents, self.metadata), f)

    def load_documents_from_location(self, input_path):
        """Load the documents and metadata from a pickle file."""
        with open(input_path, "rb") as f:
            self.documents, self.metadata = pickle.load(f)

    def get_document_by_index(self, index):
        """Get a document by its index."""
        if 0 <= index < len(self.documents):
            return self.documents[index]
        else:
            raise IndexError("Index out of range.")
