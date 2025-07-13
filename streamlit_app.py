import streamlit as st
import logging

from research_papers_search_bot.document_loader import DocumentLoader
from research_papers_search_bot.retriever import DocumentRetriever
from research_papers_search_bot.vector_store import VectorStore

# Setup logging
logging.basicConfig(level=logging.INFO)

st.title("🔍   Research Papers Search Bot")

# Static file path to CSV
file_path = "data/arxiv_data_sample.csv"

# Load and process only once
with st.spinner("Loading Vector DB..."):
    if "vector_store" not in st.session_state:
        logging.info("Loading and processing data from CSV...")
        document_loader = DocumentLoader(file_path)
        documents, metadata = document_loader.load_documents()
        
        vector_store = VectorStore()
        vector_store.create_vector_store()
        vector_store.add_documents(documents)

        st.session_state.vector_store = vector_store
        st.session_state.retriever = DocumentRetriever(vector_store)

        st.success("✅ Vector store created from arXiv data.")

# Query Interface
query = st.text_input("🔎 Enter your search query:")

if query and st.session_state.retriever:
    logging.info(f"Received query: {query}")
    st.write("Retrieving relevant documents...")
    
    with st.spinner("Searching..."):
        relevant_docs = st.session_state.retriever.get_relevant_documents(query)

    if relevant_docs:
        st.subheader("📄 Relevant Documents")
        for i, doc in enumerate(relevant_docs, 1):
            st.markdown(f"**Result {i}:**")
            st.write(doc.page_content)
    else:
        st.warning("No relevant documents found.")
