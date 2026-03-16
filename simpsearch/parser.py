import re
from typing import List, Dict

from .exceptions import ParsingError


def parse_search_results(text: str) -> List[Dict[str, str]]:
    """
    Parse Brave search results into structured format.

    Returns:
        List of dictionaries with title, link, snippet.
    """

    try:
        results = []

        blocks = re.split(r"\n{2,}", text)

        for block in blocks:
            link_match = re.search(r"https?://\S+", block)

            if not link_match:
                continue

            link = link_match.group()

            lines = block.split("\n")

            title = lines[0].strip() if lines else ""

            snippet = " ".join(lines[1:]).strip()

            results.append(
                {
                    "title": title,
                    "link": link,
                    "snippet": snippet,
                }
            )

        return results

    except Exception as exc:
        raise ParsingError(str(exc)) from exc