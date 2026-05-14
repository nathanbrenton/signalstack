# SignalStack AI Architecture
SignalStack is an AI-enhanced news intelligence platform built to demonstrate production-style backend engineering, PostgreSQL search architecture, and practical machine learning workflows.

## Overview

SignalStack includes an AI enrichment pipeline built on top of a PostgreSQL-backed news ingestion platform.

The system combines:

- RSS ingestion
- NLP preprocessing
- PostgreSQL full-text search
- TF-IDF feature extraction
- supervised machine learning
- persisted ML inference artifacts
- live inference APIs
- confidence scoring
- hybrid retrieval

---

# AI Pipeline

RSS Feed
→ Article Cleaning
→ Keyword Extraction
→ Rule-Based Classification
→ TF-IDF Vectorization
→ Naive Bayes Training
→ Model Persistence
→ Live Inference
→ Confidence Scoring
→ PostgreSQL Enrichment Storage
→ API Exposure

---

# Core AI Components

## Rule-Based Classifier

Location:

app/ml/classifier.py

Purpose:
- bootstrap weak supervision labels
- create initial training data
- provide deterministic baseline classification

---

## TF-IDF Feature Extraction

Location:

app/ml/tfidf_demo.py

Purpose:
- convert text into numerical vectors
- prepare features for ML classification

Technologies:
- scikit-learn
- TfidfVectorizer

---

## Supervised ML Training

Location:

app/ml/train_real_classifier.py

Purpose:
- train a Naive Bayes classifier
- evaluate accuracy
- generate persisted model artifacts

Technologies:
- MultinomialNB
- train_test_split
- accuracy_score

---

## Persisted Model Artifacts

Location:

app/ml/models/

Artifacts:
- article_classifier.joblib
- article_vectorizer.joblib

Purpose:
- reusable inference
- production-style ML serving

---

## Inference Service Layer

Location:

app/ml/inference.py

Purpose:
- centralized prediction logic
- reusable ML inference abstraction
- confidence scoring
- probability distribution generation

---

## ML API Endpoints

Location:

app/api/v1/endpoints/ml.py

Endpoints:
- POST /api/v1/ml/predict
- GET /api/v1/ml/health

Purpose:
- live inference API
- model health monitoring
- production-style AI service exposure

---

# PostgreSQL AI Enrichment Fields

Articles include persisted AI metadata:

- ml_category
- ml_confidence
- ml_last_classified_at

Purpose:
- AI enrichment persistence
- confidence filtering
- ranking
- hybrid search integration

---

# Hybrid Retrieval

SignalStack supports combined:

- PostgreSQL full-text search
- ML confidence filtering
- AI-aware ranking workflows

Example:

/api/v1/articles?search=ai&min_ml_confidence=0.70

---

# Current ML Limitations
- weakly supervised bootstrap training labels

Current classifier limitations include:

- small dataset size
- weak supervision labels
- class imbalance
- limited category diversity

Future improvements may include:

- embeddings
- semantic similarity
- transformer models
- clustering
- recommendation systems
- vector databases
- retraining pipelines
- human-annotated datasets

---

# Technologies

- Python 3.13
- FastAPI
- PostgreSQL 16
- SQLAlchemy ORM
- Alembic
- scikit-learn
- Docker Compose
- TF-IDF NLP pipelines
- Naive Bayes classification

# Production Engineering Concepts

SignalStack demonstrates:

- reusable inference service layers
- persisted ML model artifacts
- inference latency monitoring
- AI subsystem health checks
- hybrid search + ML retrieval
- PostgreSQL AI enrichment persistence
- confidence-aware filtering
- API-first backend architecture
- modular query-builder design
