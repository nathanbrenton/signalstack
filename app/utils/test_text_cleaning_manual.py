from app.utils.text_cleaning import clean_html_summary


sample = "&lt;p&gt;Hello &amp;amp; welcome&lt;/p&gt;"
print(clean_html_summary(sample))
