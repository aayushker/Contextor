import feedparser
import re

def clean_html(raw_html):
    clean_text = re.sub('<.*?>', '', raw_html)
    return clean_text.strip()

def get_google_news_summary(query):
    feed_url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}"
    feed = feedparser.parse(feed_url)
    if not feed.entries:
        print("[Google News RSS] No entries found.")
        return None
    
    snippets = []
    for entry in feed.entries[:5]:
        title = clean_html(entry.title)
        summary = clean_html(entry.summary)
        snippets.append(f"{title}. {summary}")
    
    return " ".join(snippets)
