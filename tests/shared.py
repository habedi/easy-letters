import numpy as np

from easy_letters import Ranker

# Sample documents and their embeddings for testing
documents_with_embeddings = {
    "text": ["Document 1", "Document 2"],
    "embedding": [np.array([0.1, 0.2, 0.3]), np.array([0.4, 0.5, 0.6])],
}

# Sample embedding to search for similar documents
embedding_to_search = np.array([0.1, 0.2, 0.3])

# The expected response (score is Cosine similarity)
search_response = [
    {"id": 0, "score": 1.0, "payload": {"text": "Document 1"}},
    {"id": 1, "score": 0.9746, "payload": {"text": "Document 2"}},
]


def test_make_collection():
    """
    Test the make_collection method of the Ranker class.
    This test checks if the collection is created successfully with the correct
     parameters.
    """
    # Arrange
    ranker = Ranker()
    collection_name = "test_collection"

    # Act
    ranker.make_collection(documents_with_embeddings, collection_name)

    # Assert
    coll = ranker.client.get_collection(collection_name)
    assert coll is not None
    assert coll.points_count == 2
    assert coll.config.params.vectors.size == 3
    assert coll.config.params.vectors.distance == "Cosine"
