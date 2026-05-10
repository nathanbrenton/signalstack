# app/ml/tfidf_demo.py

from sklearn.feature_extraction.text import TfidfVectorizer


documents = [
    "Artificial intelligence is transforming software engineering",
    "Machine learning improves recommendation systems",
    "The basketball team won the championship game",
    "The election campaign focused on economic policy",
]


vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

print("Feature Names:")
print(feature_names)

print()
print("TF-IDF Matrix Shape:")
print(tfidf_matrix.shape)
