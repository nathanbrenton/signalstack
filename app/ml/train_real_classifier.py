# app/ml/train_real_classifier.py
# Train a TF-IDF + Naive Bayes article classifier.

from collections import Counter

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

from app.db.session import SessionLocal
from app.models.article import Article

# Load training data
db = SessionLocal()

articles = (
    db.query(Article)
    .filter(Article.ml_category.isnot(None))
    .filter(Article.clean_summary.isnot(None))
    .limit(200)
    .all()
)


# Filter undersized classes
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

print()
print("Category Distribution:")

total_documents = len(labels)

for label, count in Counter(labels).items():
    percentage = (count / total_documents) * 100

    print(
        f"{label}: "
        f"{count} documents "
        f"({percentage:.1f}%)"
    )



x_train, x_test, y_train, y_test = train_test_split(
    documents,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels,
)


# TF-IDF feature extraction
vectorizer = TfidfVectorizer()

x_train_matrix = vectorizer.fit_transform(x_train)

x_test_matrix = vectorizer.transform(x_test)


# Model training
classifier = MultinomialNB()

classifier.fit(x_train_matrix, y_train)


# Evaluation
predictions = classifier.predict(x_test_matrix)

accuracy = accuracy_score(y_test, predictions)

print()
print(f"Real Dataset Accuracy: {accuracy:.2f}")


# Persist trained artifacts
joblib.dump(
    classifier,
    "app/ml/models/article_classifier.joblib",
)

joblib.dump(
    vectorizer,
    "app/ml/models/article_vectorizer.joblib",
)

print()
print("Model artifacts saved.")

