# SignalStack

SignalStack is an AI-enhanced news intelligence platform built to demonstrate production-style backend engineering, PostgreSQL search architecture, and practical machine learning workflows.

The project combines:

- FastAPI backend engineering
- PostgreSQL full-text search
- RSS ingestion pipelines
- NLP preprocessing
- TF-IDF feature extraction
- supervised machine learning
- persisted ML inference artifacts
- live AI inference APIs
- confidence-aware filtering
- hybrid search + AI retrieval

---

# Features

## News Ingestion Pipeline

- RSS feed ingestion
- duplicate prevention
- article normalization
- clean summary generation
- keyword extraction
- language detection
- quality scoring

---

## PostgreSQL Search Architecture

- TSVECTOR search columns
- weighted full-text ranking
- GIN indexes
- phrase search
- ts_rank_cd ranking
- relevance-aware pagination
- hybrid search workflows

Example:

```text
/api/v1/articles?search=ai
```

Phrase search:

```text
/api/v1/articles?phrase_search=artificial intelligence
```

---

## AI / Machine Learning Features

### Weak Supervision Classifier

Rule-based NLP classification used to bootstrap training labels.

### TF-IDF Feature Extraction

Text vectorization using scikit-learn TF-IDF pipelines.

### Supervised ML Pipeline

- Multinomial Naive Bayes classifier
- persisted model artifacts
- reusable inference service layer
- probability distribution scoring

### Live Inference API

```text
POST /api/v1/ml/predict
```

Returns:
- predicted category
- confidence score
- probability distribution
- inference timing
- model version metadata

### AI Enrichment Persistence

Articles persist:
- ml_category
- ml_confidence
- ml_last_classified_at

---

# Example Hybrid Retrieval

Search + AI confidence filtering:

```text
/api/v1/articles?search=ai&min_ml_confidence=0.70
```

---

# Architecture

See:

- AI_ARCHITECTURE.md
- docs/diagrams/ai_architecture.png

---

# Technology Stack

## Backend

- Python 3.13
- FastAPI
- SQLAlchemy ORM
- Alembic

## Database

- PostgreSQL 16
- TSVECTOR
- GIN indexes
- full-text search

## AI / ML

- scikit-learn
- TF-IDF vectorization
- Naive Bayes classification
- joblib model persistence

## Infrastructure

- Docker Compose
- PostgreSQL containers
- REST API architecture

---

# Quick Start

## Clone repository

```bash
git clone <your-repo-url>
cd signalstack
```

## Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment

```bash
cp .env.example .env
```

## Start PostgreSQL

```bash
docker compose up -d
```

## Run migrations

```bash
python -m alembic upgrade head
```

## Ingest articles

```bash
python -m app.ingestion.fetch_rss
```

## Train ML classifier

```bash
python -m app.ml.train_real_classifier
```

## Run AI enrichment

```bash
python -m app.ml.predict_real_articles
```

## Start API server

```bash
python -m uvicorn app.main:app --reload
```

## Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

# Example API Endpoints

## Articles

```text
GET /api/v1/articles
```

## Search

```text
GET /api/v1/articles?search=ai
```

## Phrase Search

```text
GET /api/v1/articles?phrase_search=artificial intelligence
```

## Confidence Filtering

```text
GET /api/v1/articles?min_ml_confidence=0.70
```

## ML Prediction

```text
POST /api/v1/ml/predict
```

Example payload:

```json
{
  "text": "Artificial intelligence improves cybersecurity systems."
}
```

## ML Health

```text
GET /api/v1/ml/health
```

---

# Current ML Limitations

Current classifier limitations include:

- small dataset size
- weakly supervised bootstrap training labels
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
