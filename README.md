# SimpSearch

**SimpSearch — Lightweight Python library for extracting clean text and structured search results.**

SimpSearch is a developer‑friendly Python library that allows you to perform web searches and extract readable text from webpages using the **W3C HTML‑to‑Text service**.

The library converts webpages into clean plain text and also supports **structured search result parsing**.

---

# ✨ Features

* 🔎 Web search using Brave
* 🌐 Website text extraction
* 📄 Raw search output
* 🧹 Clean text extraction
* 🔗 Link extraction
* 📊 Structured parsed search results
* 📑 Pagination support
* ⚡ Lightweight and fast
* 🧩 Simple Python API
* 🪶 Minimal dependencies

---

# 📦 Installation

Install from PyPI:

```bash
pip install simpsearch
```

Or install from source:

```bash
git clone https://github.com/simpsearch/simpsearch-python.git
cd simpsearch
pip install -e .
```

---

# 🚀 Quick Start

```python
from simpsearch import SimpSearch

client = SimpSearch()

results = client.parsed("hello world")

print(results)
```

---

# 🧠 How It Works

SimpSearch works in two stages:

1. **Brave Search** generates search results
2. The **W3C HTML2TXT service** converts HTML pages into readable text

This makes it possible to extract clean text without needing a full HTML parser.

---

# 📚 Usage Examples

Below are multiple small examples showing different ways to use SimpSearch.

---

## Example 1 — Basic Search

```python
from simpsearch import SimpSearch

client = SimpSearch()

print(client.raw("python programming"))
```

---

## Example 2 — Clean Text Search Results

Remove URLs from the search results.

```python
client.text("python programming")
```

---

## Example 3 — Extract Only Links

```python
links = client.links("machine learning")

print(links)
```

Example output:

```python
[
 "https://example.com",
 "https://another-site.com"
]
```

---

## Example 4 — Structured Search Results

```python
results = client.parsed("open source projects")

for r in results:
    print(r["title"])
    print(r["link"])
    print(r["snippet"])
```

---

## Example 5 — Extract Website Text

```python
text = client.extract("https://example.com")

print(text)
```

---

## Example 6 — Extract Text Without Inline References

```python
client.extract(
    "https://example.com",
    no_inline_refs=True
)
```

---

## Example 7 — Extract Text Without Numbers

```python
client.extract(
    "https://example.com",
    remove_numbers=True
)
```

---

## Example 8 — Pagination Search

Retrieve the next page of search results.

```python
client.parsed("python tutorials", offset=10)
```

---

## Example 9 — Iterate Over Links

```python
for link in client.links("ai tools"):
    print(link)
```

---

## Example 10 — Build a Simple Search Tool

```python
query = "best python libraries"

results = client.parsed(query)

for r in results:
    print(f"{r['title']} -> {r['link']}")
```

---

# 📄 API Reference

## Main Class

```python
SimpSearch
```

Create a client instance.

```python
client = SimpSearch()
```

---

## Methods

### extract()

Extract readable text from any webpage.

```python
client.extract(url)
```

Optional parameters:

* `no_inline_refs=True`
* `remove_numbers=True`

---

### raw()

Return the full raw text search result.

```python
client.raw("query")
```

---

### text()

Return search results with links removed.

```python
client.text("query")
```

---

### links()

Return only links extracted from results.

```python
client.links("query")
```

---

### parsed()

Return structured search results.

```python
client.parsed("query")
```

Example output:

```python
[
 {
  "title": "Example",
  "link": "https://example.com",
  "snippet": "Example snippet"
 }
]
```

---

# 📂 Project Structure

```
simpsearch/

simpsearch/
    __init__.py
    client.py
    search.py
    extract.py
    parser.py
    utils.py
    exceptions.py

examples/
    search_example.py
    extract_example.py

tests/
    test_search.py
    test_extract.py
```

---

# ⚙️ Dependencies

SimpSearch intentionally uses minimal dependencies.

Required:

```
requests
re
urllib.parse
```

---

# 🧪 Running Tests

```bash
pytest
```

---

# 🛠 Development Setup

```bash
git clone https://github.com/yourusername/simpsearch
cd simpsearch
pip install -e .
```

---

# 🤝 Contributing

Contributions are welcome!

Steps:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📈 Future Roadmap

Possible improvements for the project:

* Async support
* CLI tool
* Multiple search engines
* Built‑in caching
* Rate limiting
* AI‑ready structured outputs

---

# 📜 License

MIT License

You are free to use, modify, and distribute this software.

---

# ⭐ Support the Project

If you like this project:

* Give it a ⭐ on GitHub
* Share it with developers
* Contribute improvements

Open‑source projects grow through community support.
