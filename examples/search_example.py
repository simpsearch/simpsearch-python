from simpsearch import SimpSearch

client = SimpSearch()

results = client.parsed("hello world")

for r in results:
    print(r)