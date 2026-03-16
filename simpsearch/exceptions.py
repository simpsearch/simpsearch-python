class EasySearchError(Exception):
    """Base exception for SimpSearch."""


class InvalidURLError(EasySearchError):
    """Raised when an invalid URL is provided."""


class RequestFailedError(EasySearchError):
    """Raised when an HTTP request fails."""


class ParsingError(EasySearchError):
    """Raised when parsing of content fails."""