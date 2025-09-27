import wikipedia
import logging

logger = logging.getLogger(__name__)

def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=3)
        first_para = summary.split('\n\n')[0]
        logger.info(f"[Wikipedia] Found summary for: {query}")
        return first_para.strip()
    except Exception as e:
        logger.warning(f"[Wikipedia] Not found or error: {e}")
        return None
