from simpsearch import SimpSearch

client = SimpSearch()

text = client.extract("https://example.com")

print(text)