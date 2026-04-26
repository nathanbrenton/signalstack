from fastapi import FastAPI

app = FastAPI(

    title="SignalStack API",
    description="News Intelligence API for RSS ingestion, deduplication, classification and clustering.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "SignalStack API is running"};
