from simpsearch import SimpSearch


def test_extract():
    client = SimpSearch()

    text = client.extract("https://example.com")

    assert isinstance(text, str)