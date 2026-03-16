import re
import requests
from urllib.parse import quote_plus

from .exceptions import RequestFailedError


HTML2TXT_ENDPOINT = "https://www.w3.org/services/html2txt?url="
BRAVE_SEARCH_URL = "https://search.brave.com/search?q="


def encode_query(query: str) -> str:
    """Encode search query for URL."""
    return quote_plus(query)


def build_search_url(query: str, offset: int = 0) -> str:
    """Build Brave search URL."""
    encoded = encode_query(query)

    if offset:
        return f"{BRAVE_SEARCH_URL}{encoded}&offset={offset}&spellcheck=0"

    return f"{BRAVE_SEARCH_URL}{encoded}"


def call_html2txt_api(
    url: str,
    no_inline_refs: bool = False,
    remove_numbers: bool = False,
) -> str:
    """
    Call the W3C HTML-to-Text API.
    """

    params = []

    if no_inline_refs:
        params.append("noinlinerefs=on")

    if remove_numbers:
        params.append("nonums=on")

    param_string = "&".join(params)

    endpoint = f"{HTML2TXT_ENDPOINT}{url}"

    if param_string:
        endpoint += f"&{param_string}"

    try:
        response = requests.get(endpoint, timeout=30)

        if response.status_code != 200:
            raise RequestFailedError(
                f"Request failed with status {response.status_code}"
            )

        return response.text

    except requests.RequestException as exc:
        raise RequestFailedError(str(exc)) from exc


def parse_links(text: str) -> list:
    """Extract URLs from text."""
    pattern = r"https?://[^\s]+"
    return re.findall(pattern, text)


def remove_links_from_text(text: str) -> str:
    """Remove URLs from text."""
    return re.sub(r"https?://\S+", "", text)