# SignalStack Demo Workflow

## 1. Clone the repository

git clone <your-repo-url>
cd signalstack

## 2. Create a Python virtual environment

python -m venv .venv
source .venv/bin/activate

## 3. Install dependencies

pip install -r requirements.txt

## 4. Configure environment

cp .env.example .env

## 5. Start PostgreSQL

docker compose up -d

## 6. Run database migrations

python -m alembic upgrade head

## 7. Ingest articles

python -m app.ingestion.fetch_rss

## 8. Train ML classifier

python -m app.ml.train_real_classifier

## 9. Run article enrichment

python -m app.ml.predict_real_articles

## 10. Start API server

python -m uvicorn app.main:app --reload

## 11. Open API docs

http://127.0.0.1:8000/docs

## Useful endpoints

GET /api/v1/articles

GET /api/v1/articles?search=ai

GET /api/v1/articles?min_ml_confidence=0.70

GET /api/v1/articles?search=ai&min_ml_confidence=0.70

POST /api/v1/ml/predict

GET /api/v1/ml/health

## Example ML prediction payload

{
  "text": "Artificial intelligence improves cybersecurity and software automation systems."
}
