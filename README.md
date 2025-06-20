# Research Paper Chatbot

A local-first chatbot to semantically search research papers. Built with **Streamlit**, **FAISS** for vector search, and a local **LLM** for indexing and retrieval.

## Project Overview

This project enables users to:
- Ask natural language questions about the papers.
- Retrieve and display relevant content using semantic search.


Note: The research papers database is stored in a csv file, which is processed to create a vector index for efficient searching.

The aim is to demonstrate practical application of semantic search with an intuitive front-end and a privacy-preserving local backend.
- **Streamlit**: For building the web interface.
- **FAISS**: For efficient vector similarity search.
- **Local LLM**: For generating answers based on retrieved content.


## Potential Enhancements:
- Enhance the knowledge base with more papers.
- Extend capability to upload papers and do Q&A on them.
- Generate summaries of papers.
- Add more advanced search features like filtering by author, year, etc.

