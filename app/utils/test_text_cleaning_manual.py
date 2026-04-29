from app.utils.text_cleaning import clean_html_summary, extract_keywords


sample = "&lt;p&gt;Hello &amp;amp; welcome&lt;/p&gt;"

print(clean_html_summary(sample))



tokens = ["ai", "news", "ai", "model", "news", "ai", "data"]

print(extract_keywords(tokens))
