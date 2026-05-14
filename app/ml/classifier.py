# app/ml/classifier.py
# Rule-based weak-supervision classifier for bootstrapping article categories.

TECH_KEYWORDS = {
    "ai",
    "artificial intelligence",
    "machine learning",
    "software",
    "cybersecurity",
    "data",
    "algorithm",
    "robot",
    "automation",
}

BUSINESS_KEYWORDS = {
    "market",
    "stock",
    "economy",
    "business",
    "company",
    "earnings",
    "finance",
    "trade",
}

POLITICS_KEYWORDS = {
    "election",
    "president",
    "senate",
    "congress",
    "governor",
    "policy",
    "campaign",
    "vote",
}

SPORTS_KEYWORDS = {
    "game",
    "team",
    "season",
    "player",
    "coach",
    "score",
    "league",
    "tournament",
}


def classify_article_text(text: str | None) -> str:
    """
    Classify article text using deterministic keyword matching.
    """
    if not text:
        return "unknown"

    normalized_text = text.lower()

    category_keywords = {
        "technology": TECH_KEYWORDS,
        "business": BUSINESS_KEYWORDS,
        "politics": POLITICS_KEYWORDS,
        "sports": SPORTS_KEYWORDS,
    }

    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in normalized_text:
                return category

    return "general"
