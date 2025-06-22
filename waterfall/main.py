import logging
from wikipedia import get_wikipedia_summary
from newsRSS import get_google_news_summary
from Search import get_duckduckgo_snippets

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_context_summary(query):
    context = get_wikipedia_summary(query)
    if context:
        logger.info("✅ Found on Wikipedia")
        return context
    
    context = get_google_news_summary(query)
    if context:
        logger.info("📰 Found on Google News RSS")
        return context
    
    context = get_duckduckgo_snippets(query)
    if context:
        logger.info("🔎 Found via DuckDuckGo Search")
        return context

    logger.warning("❌ No relevant context found.")
    return "❌ No relevant context found."
