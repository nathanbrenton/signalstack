# app/ml/embeddings.py
# Reusable semantic embeddings service layer.

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


EMBEDDING_MODEL_NAME = "models/sentence-transformers/all-MiniLM-L6-v2"

model = SentenceTransformer(
    EMBEDDING_MODEL_NAME
)


def generate_embedding(
    text: str,
) -> list[float]:
    """
    Generate a semantic embedding vector for text.
    """

    embedding = model.encode([text])[0]

    return embedding.tolist()


def calculate_similarity(
    text_a: str,
    text_b: str,
) -> float:
    """
    Calculate cosine similarity between two texts.
    """

    embedding_a = model.encode([text_a])

    embedding_b = model.encode([text_b])

    similarity = cosine_similarity(
        embedding_a,
        embedding_b,
    )[0][0]

    return float(similarity)
