from .extract import extract_text
from .search import (
    search_raw,
    search_text,
    search_links,
    search_parsed,
)


class SimpSearch:
    """
    Main client class for SimpSearch.
    """

    def extract(
        self,
        url: str,
        no_inline_refs: bool = True,
        remove_numbers: bool = True,
    ) -> str:
        """
        Extract readable text from webpage.
        """

        return extract_text(
            url,
            no_inline_refs=no_inline_refs,
            remove_numbers=remove_numbers,
        )

    def raw(self, query: str, offset: int = 0) -> str:
        """Return raw search output."""

        return search_raw(query, offset)

    def text(self, query: str, offset: int = 0) -> str:
        """Return cleaned text without links."""

        return search_text(query, offset)

    def links(self, query: str, offset: int = 0) -> list:
        """Return only links."""

        return search_links(query, offset)

    def parsed(self, query: str, offset: int = 0):
        """Return structured search results."""

        return search_parsed(query, offset)