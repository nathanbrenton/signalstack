# app/ml/train_classifier_demo.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


training_documents = [
    "Artificial intelligence improves software systems",
    "Machine learning powers recommendation engines",
    "Cybersecurity protects computer networks",

    "The stock market reacted to economic news",
    "Investors analyzed company earnings reports",

    "The basketball team won the playoff game",
    "The football coach discussed the season",

    "The election campaign focused on healthcare policy",
    "Congress voted on the new legislation",
]

training_labels = [
    "technology",
    "technology",
    "technology",

    "business",
    "business",

    "sports",
    "sports",

    "politics",
    "politics",
]


vectorizer = TfidfVectorizer()

training_matrix = vectorizer.fit_transform(training_documents)

classifier = MultinomialNB()

classifier.fit(training_matrix, training_labels)


test_documents = [
    "AI software transforms cybersecurity operations",
    "The senator discussed economic legislation",
    "The championship team celebrated the victory",
]

test_matrix = vectorizer.transform(test_documents)

predictions = classifier.predict(test_matrix)

print("Predictions:")

for document, prediction in zip(test_documents, predictions):
    print()
    print(f"Document: {document}")
    print(f"Predicted Category: {prediction}")
