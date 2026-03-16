from simpsearch import SimpSearch


def test_links():
    client = SimpSearch()

    results = client.links("python programming")

    assert isinstance(results, list)