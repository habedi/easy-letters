from typing import Any, List

import numpy as np
import openai
from numpy import ndarray, dtype


class LanguageModels:
    """
    Supported language models.
    """
    OPENAI_GPT35TURBO = "gpt-3.5-turbo"
    OPENAI_GPT4TURBO = "gpt-4-turbo"
    OPENAI_GPT4O = "gpt-4o"
    OPENAI_GPT4OMINI = "gpt-4o-mini"


class EmbeddingModels:
    """
    Supported text embedding models.
    """
    OPENAPI_EMS = "text-embedding-3-small"
    OPENAPI_EML = "text-embedding-3-large"


class OpenAIConnector:
    """
    Connector to interact with the OpenAI API for embeddings and chat completions.

    Attributes:
        client (openai.Client): The client used for API calls.
    """

    def __init__(self, api_key: str, **kwargs):
        """
        Initialize the connector with an API key and extra options.

        Args:
            api_key (str): Your OpenAI API key.
            **kwargs: Additional parameters for the OpenAI client.
        """
        self.client = openai.Client(api_key=api_key, **kwargs)

    def embed(self, documents: List[str], model: str) -> List[ndarray[Any, dtype[Any]]]:
        """
        Generate embeddings for a list of documents using a given model.

        Args:
            documents (List[str]): Documents to embed.
            model (str): The model to use for generating embeddings.

        Returns:
            List[ndarray[Any, dtype[Any]]]: A list of numpy arrays with the embeddings.
        """
        embeddings = self.client.embeddings.create(input=documents, model=model)
        return [np.array(d.embedding) for d in embeddings.data]

    def chat(self, prompt: str, model: str, temperature: float = 0.0, max_tokens: int = 512) -> str:
        """
        Generate a chat response for a given prompt using a specified model.

        Args:
            prompt (str): The prompt text.
            model (str): The model to use.
            temperature (float, optional): Sampling temperature (defaults to 0.0).
            max_tokens (int, optional): Maximum tokens to generate (defaults to 512).

        Returns:
            str: The chat response text.
        """
        completion = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return completion.choices[0].message.content
