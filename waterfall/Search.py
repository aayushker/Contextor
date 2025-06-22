import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_duckduckgo_snippets(query):
    """
    Fetches top 5 DuckDuckGo search results and returns their snippets as a summary paragraph.
    Uses the DuckDuckGo Instant Answer API (free, no API key required).
    """
    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json",
        "no_html": 1,
        "skip_disambig": 1
    }
    try:
        res = requests.get(url, params=params, timeout=5)
        res.raise_for_status()
        data = res.json()
        # Collect Abstract, RelatedTopics, and Results
        snippets = []
        if data.get("Abstract"):
            snippets.append(data["Abstract"])
        # RelatedTopics may contain more snippets
        for topic in data.get("RelatedTopics", [])[:5]:
            if isinstance(topic, dict) and topic.get("Text"):
                snippets.append(topic["Text"])
        # Results may contain more snippets
        for result in data.get("Results", [])[:5]:
            if result.get("Text"):
                snippets.append(result["Text"])
        summary = " ".join(snippets).strip()
        if summary:
            logger.info("[DuckDuckGo] Found results for query: %s", query)
            return summary
        else:
            logger.warning("[DuckDuckGo] No relevant results found for query: %s", query)
            return None
    except Exception as e:
        logger.error("[DuckDuckGo] Error fetching results: %s", e)
        return None
