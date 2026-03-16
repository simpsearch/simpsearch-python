# SimpSearch

**SimpSearch — Lightweight Python library for extracting clean text and structured search results.**

SimpSearch simplifies web search and webpage text extraction by using the W3C HTML-to-Text service.

---

## Features

* Web search using Brave
* Website text extraction
* Raw search output
* Clean text extraction
* Link extraction
* Structured parsed search results
* Pagination support

---

## Installation

```bash
pip install simpsearch
```

---

## Quick Start

```python
from simpsearch import SimpSearch

client = SimpSearch()

print(client.parsed("hello world"))
```

---

## Usage Examples

### Raw search results

```python
client.raw("hello world")
```

---

### Only links

```python
client.links("hello world")
```

Example output:

```python
[
 "https://example.com",
 "https://another-site.com"
]
```

---

### Structured results

```python
client.parsed("hello world")
```

Example output:

```python
[
 {
  "title": "Example Title",
  "link": "https://example.com",
  "snippet": "Example snippet text"
 }
]
```

---

### Extract website text

```python
client.extract("https://example.com")
```

---

## Pagination Example

```python
client.parsed("hello world", offset=10)
```

---

## License

MIT License

---

## Contributing

Contributions are welcome.

If you would like to improve SimpSearch:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a pull request

Community contributions help make this project better for everyone.
