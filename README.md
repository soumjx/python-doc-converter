# DocGo (Core Python Implementation)

A lightweight, dependency-free command-line tool to convert `.docx` files into Markdown, HTML, and CSV.

**Note:** It is implemented using **Core Python (Standard Library) only** to demonstrate foundational Computer Science concepts and Software Engineering patterns without relying on external libraries like `python-docx` or `pandas`.

---

## 🚀 Features

- **Zero Dependencies:** Runs on any machine with Python 3.10+ installed.
- **Low-Level Parsing:** Implements a custom ZIP and XML parser to extract content from MS Word OpenXML format.
- **Architecture:** Uses **Strategy Pattern** for formatters and **Generator Patterns** for memory-efficient parsing.
- **Supported Formats:**
  - Markdown (`.md`)
  - HTML (`.html`)
  - CSV (`.csv`)

---

## 🛠 Project Structure

```text
docgo/
├── src/docgo/
│   ├── core.py        # Custom XML Extractor (The "Driver")
│   ├── formatters.py  # Output Strategies (MD, HTML, CSV)
│   └── main.py        # CLI Entry Point
├── pyproject.toml     # Project metadata
├── test.docx          # Sample input file
└── README.md
````

---

## ⚙️ Environment Setup
```
git clone https://github.com/soumjx/python-doc-converter.git
cd 
```
### place the test.docx in the root directory

---

## ▶️ Usage

### Standard Python

```bash
python -m src.docgo.main test.docx html -o output/result.html
```
### All Output Formats

```bash
python -m src.docgo.main test.docx md -o output/doc.md
python -m src.docgo.main test.docx html -o output/doc.html
python -m src.docgo.main test.docx csv -o output/data.csv
```
---


### Using uv

```bash
uv venv
.venv\Scripts\activate
```


### All Output Formats

```bash
uv run python -m src.docgo.main test.docx md -o output/doc.md
uv run python -m src.docgo.main test.docx html -o output/doc.html
uv run python -m src.docgo.main test.docx csv -o output/data.csv
```
---


