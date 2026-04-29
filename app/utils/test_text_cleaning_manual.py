from app.utils.text_cleaning import clean_html_summary, create_summary_hash, extract_keywords, detect_language




#sample = "&lt;p&gt;Hello &amp;amp; welcome&lt;/p&gt;"

#print(clean_html_summary(sample))

#tokens = ["ai", "news", "ai", "model", "news", "ai", "data"]
#print(extract_keywords(tokens))

#tokens = ["this", "is", "a", "test", "article"]
#print(detect_language(tokens))

#print(detect_language("This is a test article with several English words."))

#print(create_summary_hash("example cleaned summary"))

##############

from app.utils.text_cleaning import calculate_quality_score

print(calculate_quality_score("This is a cleaned summary.", 4, ["summary"]))
