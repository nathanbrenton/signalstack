# Semantic embeddings demo using sentence transformers.

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

sentences = [
    "Artificial intelligence improves cybersecurity.",
    "Machine learning enhances digital security.",
    "The baseball team won the championship.",
]

embeddings = model.encode(sentences)

print()
print("Embedding Shape:")
print(embeddings.shape)

print()
print("Cosine Similarity Matrix:")

similarity_matrix = cosine_similarity(
    embeddings
)

for row in similarity_matrix:
    print(row)
