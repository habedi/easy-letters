from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
from qdrant_client.http.models import VectorParams, Distance


class Ranker:
    """
    Ranker class to find similar documents using QdrantClient.

    Attributes:
        client: The Qdrant client used for interacting with the database.
    """

    def __init__(self):
        """
        Initialize the Ranker with an in-memory Qdrant client.
        """
        self.client = QdrantClient(":memory:")

    def make_collection(self, documents_with_embeddings,
                        collection_name="letters"):
        """
        Create a collection with the given documents and embeddings in the db.

        Args:
            documents_with_embeddings (dict): A dictionary containing 'text'
            and 'embedding' keys with lists of documents and their
            corresponding embeddings.
            collection_name (str): The name of the collection to create.
            Defaults to "letters".

        Returns:
            None
        """
        documents = documents_with_embeddings['text']
        embeddings = documents_with_embeddings['embedding']

        points = [PointStruct(id=idx, vector=e, payload={'text': d})
                  for idx, (d, e) in enumerate(zip(documents, embeddings))]

        print(
            f"Creating collection {collection_name} with {len(points)} "
            f"points of size {embeddings[0].shape[0]}")
        self.client.create_collection(collection_name=collection_name,
                                      vectors_config=VectorParams(
                                          size=embeddings[0].shape[0],
                                          distance=Distance.COSINE))

        self.client.upsert(collection_name, points)

    def find_similar(self, embedding, collection_name="letters", top_k=5,
                     min_similarity=0.1):
        """
        Find similar documents in the given collection for the given embedding
         and return top k results.

        Args:
            embedding (list or numpy.ndarray): The embedding vector to search
            for similar documents.
            collection_name (str): The name of the collection to search in.
            Defaults to "letters".
            top_k (int): The number of top similar documents to return.
            Defaults to 5.
            min_similarity (float): The minimum similarity score threshold.
            Defaults to 0.1.

        Returns:
            list: A list of search results with similar documents.
        """
        return self.client.search(collection_name=collection_name,
                                  query_vector=embedding,
                                  limit=top_k, score_threshold=min_similarity)
