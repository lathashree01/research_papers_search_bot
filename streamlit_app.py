import streamlit as st
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

from research_papers_search_bot.document_loader import DocumentLoader
from research_papers_search_bot.retriever import DocumentRetriever
from research_papers_search_bot.vector_store import VectorStore

file_path = "/Users/lathapevi/Documents/latha/learning/git_repos/research_papers_search_bot/data/arxiv_data.csv" 
st.title("Research Papers Search Bot")
# uploaded_file = st.file_uploader("Upload a CSV file containing research papers and search through them.", type=["csv"])
ready_for_query = False

# if uploaded_file is not None:
#     logging.info("File uploaded successfully.")
#     logging.info(uploaded_file)

#     # Read the CSV file and display a preview
#     df = pd.read_csv(uploaded_file)
#     st.write("Data Preview:")
#     st.dataframe(df.head())

#     if st.button("Process Data"):
#         logging.info("Processing data...")
#         # Load documents from the uploaded CSV file
#         document_loader = DocumentLoader(uploaded_file)
#         documents, metadata = document_loader.load_documents(df=df)
#         vector_store = VectorStore()
#         vector_store.create_vector_store(documents)

#         st.write("Data loaded to vector store successfully.")
#         ready_for_query = True

document_loader = DocumentLoader(file_path)
documents, metadata = document_loader.load_documents()
vector_store = VectorStore()
vector_store.create_vector_store(documents)
st.write("Data loaded to vector store successfully.")

query = st.text_input("You can now enter your search query:")
# Initialize the retriever with the vector store
retriever = DocumentRetriever(vector_store)

if query:
    # Retrieve relevant documents based on the query
    logging.info(f"Query received: {query}")
    st.write("Retrieving relevant documents...")
    with st.spinner("Searching..."):
        relevant_docs = retriever.get_relevant_documents(query)
    st.write("Relevant Documents:")
    for doc in relevant_docs:
        st.write(doc.page_content)