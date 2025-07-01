# Research Paper Chatbot

A local-first chatbot to semantically search research papers. Built with **Streamlit**, **FAISS** for vector search, and a local **LLM** for indexing and retrieval.

## Project Overview

This project enables users to:
- Ask natural language questions about the papers.
- Retrieve and display relevant content using semantic search.


Note: The research papers database is stored in a csv file, which is processed to create a vector index for efficient searching.

The aim is to demonstrate practical application of semantic search with a simple front-end using Streamlit and a local backend.
- **Streamlit**: For building the web interface.
- **FAISS**: For efficient indexing and vector similarity search.
- **Local LLM**: For generating answers based on retrieved content - using SentenceTransformers model - `all-MiniLM-L6-v2` model from HuggingFace.

## To Run the Project Locally
This project requires Python 3.11 or higher and uses Poetry for dependency management.  Install Poetry if you haven't already:

```bash
pip install poetry
```
Then, follow these steps to set up and run the project:
1. Clone the repository:
   ```bash
   git clone git@github.com:lathashree01/research_papers_search_bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd research_papers_search_bot
   ```
 
3. Install the required dependencies:
    ```bash 
    poetry install
    ```
4. Run the Streamlit app:
    ```bash 
    streamlit run streamlit_app.py
    ```
5. Open your browser and go to `http://localhost:8501` to interact with the search interface.

## Potential Enhancements:
- Enhance the knowledge base with more papers - maybe integrate with a search API.
- Extend capability to upload papers and do Q&A on them.
- Generate summaries of papers.
- Add more advanced search features like filtering by author, year, etc.

