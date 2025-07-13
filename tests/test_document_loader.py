from research_papers_search_bot.vector_store import VectorStore
from research_papers_search_bot.document_loader import DocumentLoader
from research_papers_search_bot.retriever import DocumentRetriever


def test_vector_store(sample_arxiv_csv):
    print("sample_arxiv_csv:", sample_arxiv_csv)
    assert sample_arxiv_csv.exists(), "Sample CSV file does not exist."

    loader = DocumentLoader(sample_arxiv_csv)
    documents, metadata = loader.load_documents()
    assert len(documents) == 5
    assert len(metadata) == 5
    assert "transformer" in documents[0].page_content


def test_vector_store_creation(sample_arxiv_csv):
    print("sample_arxiv_csv:", sample_arxiv_csv)
    assert sample_arxiv_csv.exists(), "Sample CSV file does not exist."

    loader = DocumentLoader(sample_arxiv_csv)
    documents, metadata = loader.load_documents()
    assert len(documents) == 5
    assert len(metadata) == 5
    assert "transformer" in documents[0].page_content

    vector_store = VectorStore()
    vector_store.add_documents(documents)
    assert vector_store.get_vector_store() is not None, "Vector store should not be None after adding documents."

    retriever = DocumentRetriever(vector_store)
    query = "transformer models"
    results = retriever.get_relevant_documents(query)
    # print("Results:", results)

    assert len(results) > 0
    assert "transformer" in results[0]
