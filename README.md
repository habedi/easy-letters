## Easy Letters

[![Tests](https://github.com/habedi/easy-letters/actions/workflows/tests.yml/badge.svg)](https://github.com/habedi/easy-letters/actions/workflows/tests.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/habedi/easy-letters/badge)](https://www.codefactor.io/repository/github/habedi/easy-letters)
[![python version](https://img.shields.io/badge/Python-%3E=3.10-blue)](https://github.com/habedi/easy-letters)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/easy-letters.svg)](https://badge.fury.io/py/easy-letters)
[![pip downloads](https://img.shields.io/pypi/dm/easy-letters.svg)](https://pypi.org/project/easy-letters/)

Easy Letters is a Python library that can help job seekers write application letters.
Currently, it proves the basic blocks for creating a simple retrieval augmented generation (RAG) pipeline
to generate application letter drafts.
The user can then edit the draft letter to suit their needs.

See the [notebooks/README.md](notebooks/README.md) file for how it works.

### 🔧 Installation

You can install Easy Letters using pip:

```bash
pip install easy-letters
```

### 🚀 Getting Started

#### API Key Setup

Easy Letters gets the API key for supported services (like OpenAI) from the environment variables.
So you need to set the following environment variables to be able to use Easy Letters:

- `OPENAI_API_KEY`: The OpenAI API key (required)

#### Sample Notebooks

You can find Jupyter notebooks with example code in the [notebooks](notebooks/) directory.
The notebooks demonstrate how to use Easy Letters to generate application letter drafts.

#### Supported Models

Easy Letters currently supports the following models:

| Model                            | Type            |
|----------------------------------|-----------------|
| GPT-3.5 Turbo                    | Text Generation |
| GPT-4 Turbo                      | Text Generation |
| GPT-4o                           | Text Generation |
| GPT-4o Mini                      | Text Generation |
| Text Embedding 3 (Small Variant) | Text Embedding  |
| Text Embedding 3 (Large Variant) | Text Embedding  |

#### Installing from Source

You can also install Easy Letters from the source code in this repository. The main benefit of this approach is that
you might find it easier to run the sample notebooks and modify the code as you wish this way.

After cloning this repository, you can navigate to the directory where you cloned the repository and install the
dependencies using [Poetry](https://python-poetry.org/):

```bash
git clone https://github.com/habedi/easy-letters.git && cd easy-letters

# Assuming you have Poetry installed on your system
poetry install --with dev
```

#### Running Tests with Coverage

You can run the unit tests with coverage using the following command:

```bash
poetry run pytest tests/ --cov=easy_letters
```

### 📝 TODO

- [ ] Add support for Anthropic models and API
- [ ] Add support for locally served models via Ollama
