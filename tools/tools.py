from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str) -> str:
    """Searches for LinkedIn or TWitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    # we don't need to parse the response, because the LLM will return the URL for us.
    return res
