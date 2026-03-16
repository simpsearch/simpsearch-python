from .utils import build_search_url, call_html2txt_api
from .parser import parse_search_results
from .utils import parse_links, remove_links_from_text


def search_raw(query: str, offset: int = 0) -> str:
    """Return raw search results text."""

    url = build_search_url(query, offset)

    return call_html2txt_api(url)


def search_text(query: str, offset: int = 0) -> str:
    """Return search results with links removed."""

    raw = search_raw(query, offset)

    return remove_links_from_text(raw)


def search_links(query: str, offset: int = 0) -> list:
    """Return only links from search results."""

    raw = search_raw(query, offset)

    return parse_links(raw)


def search_parsed(query: str, offset: int = 0):
    """Return structured parsed results."""

    raw = search_raw(query, offset)

    return parse_search_results(raw)