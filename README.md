# Regional NLP

A lightweight multilingual NLP preprocessing library for Indian regional languages.

## Supported Languages

- Telugu
- Malayalam

## Features

- Tokenization
- Stopword Removal
- Multilingual Text Processing

## Installation

```bash
pip install nltk
```

## Example Usage

```python
from preprocess import Charlie

result = Charlie(
    "ఇది నా తెలుగు పరిశోధన ప్రాజెక్ట్",
    "telugu"
)

print(result)
```

## Example Output

```python
['తెలుగు', 'పరిశోధన', 'ప్రాజెక్ట్']
```