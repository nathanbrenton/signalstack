from html import unescape
from re import sub

STOPWORDS = {
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

    filtered_tokens = [w for w in words if w not in STOPWORDS]

    cleaned_text = " ".join(filtered_tokens)

    return cleaned_text, filtered_tokens
