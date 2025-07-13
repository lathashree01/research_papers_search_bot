import pytest
import pandas as pd

@pytest.fixture
def sample_arxiv_csv(tmp_path):
    """Creates a sample arxiv-style CSV file with columns: titles, summaries, terms"""
    data = {
        "titles": [
            "Transformer Models for Text Classification",
            "Deep Learning for Medical Imaging",
            "Contrastive Learning in NLP",
            "Graph Neural Networks for Recommendation",
            "RL for Autonomous Navigation"
        ],
        "summaries": [
            "We explore the use of transformer-based models for classifying text across various domains.",
            "This paper surveys the application of deep learning techniques to radiological image analysis.",
            "Contrastive learning has emerged as a powerful self-supervised approach in language tasks.",
            "This work applies graph neural networks to large-scale user-item interaction graphs.",
            "We propose a reinforcement learning-based system for autonomous robot navigation."
        ],
        "terms": [
            "transformer, classification, BERT",
            "medical imaging, CNN, deep learning",
            "contrastive learning, self-supervised, NLP",
            "GNN, recommendation, collaborative filtering",
            "reinforcement learning, robotics, navigation"
        ]
    }

    df = pd.DataFrame(data)
    file_path = tmp_path / "sample_arxiv_data.csv"
    df.to_csv(file_path, index=False)
    return file_path
