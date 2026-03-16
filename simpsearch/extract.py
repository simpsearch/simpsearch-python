from .utils import call_html2txt_api


def extract_text(
    url: str,
    no_inline_refs: bool = False,
    remove_numbers: bool = False,
) -> str:
    """
    Extract readable text from webpage.
    """

    return call_html2txt_api(
        url,
        no_inline_refs=no_inline_refs,
        remove_numbers=remove_numbers,
    )