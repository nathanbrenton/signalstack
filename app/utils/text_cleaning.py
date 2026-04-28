from html import unescape
from re import sub


def clean_html_summary(raw_summary: str | None) -> str | None:
    if raw_summary is None:
        return None

    text = unescape(unescape(raw_summary))
    text = sub(r"<[^>]+>", "", text)
    text = sub(r"\s+", " ", text)

    text = text.strip()

    # NLP prep: normalize case
    text = text.lower()
    return text
