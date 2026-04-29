from collections import Counter
from html import unescape
from re import sub

STOPWORDS = {
    "a",
    "the", 
    "and", 
    "is", 
    "to", 
    "of", 
    "in", 
    "that", 
    "it", 
    "on", 
    "for", 
    "with", 
    "as", 
    "was", 
    "at", 
    "by", 
    "an", 
    "had",
    "he",
    "her",
}

def clean_html_summary(raw_summary: str | None):
    if raw_summary is None:
        return "", []

    text = unescape(unescape(raw_summary))
    text = sub(r"<[^>]+>", "", text)
    text = sub(r"\s+", " ", text)

    text = text.strip()
    text = text.lower() # NLP prep: normalize case
    text = sub(r"[^\w\s\.\,\!\?]", "", text) # Remove excess punctuation (keep .,!? for now)

    if len(text) < 40:
        return "", []

    words = text.split()

    filtered_tokens = [
        w.strip(".,!?")
        for w in words
        if w.strip(".,!?") and w.strip(".,!?") not in STOPWORDS
    ]

    cleaned_text = " ".join(filtered_tokens)

    return cleaned_text, filtered_tokens


def extract_keywords(tokens: list[str], top_n: int = 5) -> list[str]:
    if not tokens:
        return []

    counts = Counter(tokens)
    most_common = counts.most_common(top_n)

    return [word for word, _ in most_common]
