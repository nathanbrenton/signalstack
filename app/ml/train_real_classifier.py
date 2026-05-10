# app/ml/train_real_classifier.py

from app.db.session import SessionLocal
from app.models.article import Article
from collections import Counter

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB


db = SessionLocal()

articles = (
    db.query(Article)
    .filter(Article.ml_category.isnot(None))
    .filter(Article.clean_summary.isnot(None))
    .limit(200)
    .all()
)


documents = []
labels = []

for article in articles:
    documents.append(article.clean_summary)
    labels.append(article.ml_category)

label_counts = Counter(labels)

filtered_documents = []
filtered_labels = []

for document, label in zip(documents, labels):
    if label_counts[label] >= 2:
        filtered_documents.append(document)
        filtered_labels.append(label)

documents = filtered_documents
labels = filtered_labels

print()
print(f"Documents Loaded: {len(documents)}")
print(f"Label Counts: {Counter(labels)}")



x_train, x_test, y_train, y_test = train_test_split(
    documents,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels,
)


vectorizer = TfidfVectorizer()

x_train_matrix = vectorizer.fit_transform(x_train)

x_test_matrix = vectorizer.transform(x_test)


classifier = MultinomialNB()

classifier.fit(x_train_matrix, y_train)


predictions = classifier.predict(x_test_matrix)

accuracy = accuracy_score(y_test, predictions)

print()
print(f"Real Dataset Accuracy: {accuracy:.2f}")
