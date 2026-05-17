#!/bin/bash

set -e

SRC_DIR="$HOME/projects/signalstack"
OUT_DIR="$HOME/projects/signalstack_keyfiles"

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

cd "$SRC_DIR"

mkdir -p "$OUT_DIR/app/api/v1/endpoints"
mkdir -p "$OUT_DIR/app/ml"
mkdir -p "$OUT_DIR/app/models"
mkdir -p "$OUT_DIR/app/schemas"
mkdir -p "$OUT_DIR/app/crud"
mkdir -p "$OUT_DIR/app/ingestion"
mkdir -p "$OUT_DIR/app/utils"
mkdir -p "$OUT_DIR/app/db"
mkdir -p "$OUT_DIR/app/config"
mkdir -p "$OUT_DIR/app/services"
mkdir -p "$OUT_DIR/app/static"
mkdir -p "$OUT_DIR/docs/diagrams"
mkdir -p "$OUT_DIR/alembic/versions"

cp README.md "$OUT_DIR/" 2>/dev/null || true
cp DEMO.md "$OUT_DIR/" 2>/dev/null || true
cp AI_ARCHITECTURE.md "$OUT_DIR/" 2>/dev/null || true
cp .env.example "$OUT_DIR/" 2>/dev/null || true
cp requirements.txt "$OUT_DIR/" 2>/dev/null || true
cp docker-compose.yaml "$OUT_DIR/" 2>/dev/null || true
cp alembic.ini "$OUT_DIR/" 2>/dev/null || true

cp app/main.py "$OUT_DIR/app/"
cp app/api/v1/router.py "$OUT_DIR/app/api/v1/"

cp app/api/v1/endpoints/articles.py "$OUT_DIR/app/api/v1/endpoints/"
cp app/api/v1/endpoints/ml.py "$OUT_DIR/app/api/v1/endpoints/"
cp app/api/v1/endpoints/ml_health.py "$OUT_DIR/app/api/v1/endpoints/"
cp app/api/v1/endpoints/health.py "$OUT_DIR/app/api/v1/endpoints/"
cp app/api/v1/endpoints/rss_feeds.py "$OUT_DIR/app/api/v1/endpoints/"
cp app/api/v1/endpoints/dashboard.py "$OUT_DIR/app/api/v1/endpoints/"

cp app/crud/article.py "$OUT_DIR/app/crud/"

cp app/models/article.py "$OUT_DIR/app/models/"
cp app/models/rss_feed_source.py "$OUT_DIR/app/models/"

cp app/schemas/article.py "$OUT_DIR/app/schemas/"
cp app/schemas/ml.py "$OUT_DIR/app/schemas/"

cp app/ml/classifier.py "$OUT_DIR/app/ml/"
cp app/ml/inference.py "$OUT_DIR/app/ml/"
cp app/ml/embeddings.py "$OUT_DIR/app/ml/"
cp app/ml/semantic_search.py "$OUT_DIR/app/ml/"
cp app/ml/hybrid_search.py "$OUT_DIR/app/ml/"
cp app/ml/article_similarity.py "$OUT_DIR/app/ml/"
cp app/ml/article_clustering_demo.py "$OUT_DIR/app/ml/"
cp app/ml/generate_article_embeddings.py "$OUT_DIR/app/ml/"
cp app/ml/train_real_classifier.py "$OUT_DIR/app/ml/"
cp app/ml/predict_real_articles.py "$OUT_DIR/app/ml/"
cp app/ml/hybrid_search_demo.py "$OUT_DIR/app/ml/"
cp app/ml/embeddings_demo.py "$OUT_DIR/app/ml/"
cp app/ml/article_similarity_demo.py "$OUT_DIR/app/ml/"

cp app/ingestion/fetch_rss.py "$OUT_DIR/app/ingestion/"

cp app/utils/text_cleaning.py "$OUT_DIR/app/utils/"

cp app/db/session.py "$OUT_DIR/app/db/"
cp app/db/deps.py "$OUT_DIR/app/db/"
cp app/db/base.py "$OUT_DIR/app/db/"
cp app/db/__init__.py "$OUT_DIR/app/db/" 2>/dev/null || true

cp app/config/rss_feeds.py "$OUT_DIR/app/config/"

cp app/services/rss_feed_sources.py "$OUT_DIR/app/services/"
cp app/services/rss_ingestion.py "$OUT_DIR/app/services/"

cp app/static/index.html "$OUT_DIR/app/static/"
cp app/static/styles.css "$OUT_DIR/app/static/"
cp app/static/app.js "$OUT_DIR/app/static/"
cp app/static/favicon.svg "$OUT_DIR/app/static/" 2>/dev/null || true

cp docs/diagrams/ai_architecture.puml "$OUT_DIR/docs/diagrams/" 2>/dev/null || true
cp docs/diagrams/ai_architecture.png "$OUT_DIR/docs/diagrams/" 2>/dev/null || true

cp alembic/versions/*.py "$OUT_DIR/alembic/versions/" 2>/dev/null || true

tree -a -I ".venv|__pycache__|.git|*.pyc|.pytest_cache|models|offline_packages|app/ml/models" > "$OUT_DIR/PROJECT_TREE.txt"

find app -type f \
  -not -path "*/__pycache__/*" \
  -not -path "app/ml/models/*" \
  | sort > "$OUT_DIR/PROJECT_FILES.txt"

cd "$HOME/projects"

zip -r signalstack_keyfiles.zip signalstack_keyfiles

echo
echo "Created:"
echo "$OUT_DIR"
echo "$HOME/projects/signalstack_keyfiles.zip"
