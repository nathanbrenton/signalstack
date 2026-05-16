# Article clustering demo using embeddings.

from collections import defaultdict

from sklearn.cluster import KMeans

from app.db.session import SessionLocal
from app.models.article import Article


db = SessionLocal()

articles = (
    db.query(Article)
    .filter(Article.embedding.isnot(None))
    .limit(50)
    .all()
)

print()
print("Articles Loaded:")
print(len(articles))

embeddings = [
    article.embedding
    for article in articles
]

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init="auto",
)

labels = kmeans.fit_predict(
    embeddings
)

clusters = defaultdict(list)

for article, label in zip(
    articles,
    labels,
):
    clusters[label].append(article)

print()
print("Cluster Results")
print()

for cluster_id, cluster_articles in clusters.items():

    print(
        "================================"
    )

    print(
        f"Cluster {cluster_id}"
    )

    print(
        "================================"
    )

    for article in cluster_articles[:10]:
        print(article.title)

    print()
