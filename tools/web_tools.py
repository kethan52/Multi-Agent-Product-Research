import requests
from crewai.tools import tool
from bs4 import BeautifulSoup

@tool
def web_search_tool(query: str):
    """Perform a web search using DuckDuckGo API."""
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.json().get("AbstractText", "") or response.json().get("Answer", "No relevant info found")
        return result
    except requests.exceptions.RequestException as e:
        return f"Error: Web search failed. Details: {e}"
