import numpy as np

from easy_letters import Ranker
from tests.shared import (documents_with_embeddings, embedding_to_search,
                          search_response)


def test_find_similar():
    """
    Test the find_similar method of the Ranker class.
    This test checks if the method returns the correct similar documents based
    on the provided embedding.
    """
    # Arrange
    ranker = Ranker()
    collection_name = "test_collection"

    # Act
    ranker.make_collection(documents_with_embeddings, collection_name)
    response = ranker.find_similar(embedding_to_search, collection_name, 2)

    # Assert
    print(type(response))
    assert response[1].id == search_response[1]["id"]
    assert np.isclose(response[1].score, search_response[1]["score"], atol=1e-4)
    assert response[1].payload == search_response[1]["payload"]
