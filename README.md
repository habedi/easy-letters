# Easy Letters

[![Tests](https://github.com/habedi/easy-letters/actions/workflows/tests.yml/badge.svg)](https://github.com/habedi/easy-letters/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/easy-letters.svg)](https://badge.fury.io/py/easy-letters)
[![Downloads](https://pepy.tech/badge/easy-letters)](https://pepy.tech/project/easy-letters)

Easy Letters is a Python package that helps job seekers write application letters. A simple retrieval
augmented generation (RAG) pipeline is used to generate the letters. The user can then edit the draft letter to suit
their needs.

See the `notebooks/README.md` file for how easy letters works.

## Installation

You can install Easy Letters using pip:

```bash
pip install easy-letters
```

## Getting Started

### API Key Setup

At the moment, Easy Letters gets the API key for supported services from the environment variables.
So you need to set the following environment variables to be able to use Easy Letters:

- `OPENAI_API_KEY`: The OpenAI API key (required)

### Sample Notebooks

You can find Jupyter notebooks with example code in the `notebooks` directory.
The notebooks demonstrate how to use Easy Letters to generate application letter drafts.

### Supported Models

Easy Letters currently supports the following models:

| Model                            | Type            |
|----------------------------------|-----------------|
| GPT-3.5 Turbo                    | Text Generation |
| GPT-4 Turbo                      | Text Generation |
| GPT-4o                           | Text Generation |
| GPT-4o Mini                      | Text Generation |
| Text Embedding 3 (Small Variant) | Text Embedding  |
| Text Embedding 3 (Large Variant) | Text Embedding  |

### Installing from Source

You can also install Easy Letters from the source code in this repository. The main benefit of this approach is that
you might find it easier to run the sample notebooks and modify the code as you wish this way.

After cloning this repository, you can navigate to the `easy-letters` directory and install the
dependencies using [Poetry](https://python-poetry.org/):

```bash
git clone https://github.com/habedi/easy-letters.git && cd easy-letters

# Assuming you have Poetry installed on your system
poetry install --with dev
```

## TODO

- [ ] Add support for Anthropic models and API
- [ ] Add support for locally served models via Ollama
