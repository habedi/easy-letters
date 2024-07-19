from typing import Any, List

import numpy as np
import openai
from numpy import ndarray, dtype


class LanguageModels:
    """List of supported language models."""
    OPENAI_GPT35TURBO = 'gpt-3.5-turbo'
    OPENAI_GPT4TURBO = 'gpt-4-turbo'
    OPENAI_GPT4O = 'gpt-4o'
    OPENAI_GPT4OMINI = 'gpt-4o-mini'


class EmbeddingModels:
    """List of supported text embedding models."""
    OPENAPI_EMS = 'text-embedding-3-small'
    OPENAPI_EML = 'text-embedding-3-large'


class OpenAIConnector:
    """
    Connector class to interact with OpenAI API for embeddings and
    chat completions.

    Attributes:
        client (openai.Client): The OpenAI client used for API interactions.
    """

    def __init__(self, api_key: str, **kwargs):
        """
        Initialize the OpenAIConnector with an API key and optional parameters.

        Args:
            api_key (str): The API key for authenticating with the OpenAI API.
            **kwargs: Additional keyword arguments to pass to the OpenAI client.
        """
        self.client = openai.Client(api_key=api_key, **kwargs)

    def embed(self, documents: List[str], model: str) -> List[
        ndarray[Any, dtype[Any]]]:
        """
        Generate embeddings for a list of documents using a specified model.

        Args:
            documents (List[str]): A list of documents to embed.
            model (str): The model to use for generating embeddings.

        Returns:
            List[ndarray[Any, dtype[Any]]]: A list of numpy arrays containing
             the embeddings.
        """
        embeddings = self.client.embeddings.create(input=documents,
                                                   model=model)
        return [np.array(d.embedding) for d in embeddings.data]

    def chat(self, prompt: str, model: str, temperature: float = 0.0,
             max_tokens: int = 512) -> str:
        """
        Generate a chat completion for a given prompt using a specified model.

        Args:
            prompt (str): The input prompt for the chat model.
            model (str): The model to use for generating the chat completion.
            temperature (float, optional): The sampling temperature.
            Defaults to 0.0.
            max_tokens (int, optional): The maximum number of tokens for the
            model to generate. Defaults to 512.

        Returns:
            str: The generated chat response.
        """
        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt},
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return completion.choices[0].message.content
