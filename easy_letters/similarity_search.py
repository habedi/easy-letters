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

    def make_collection(self, documents_with_embeddings, collection_name="letters"):
        """
        Create a collection with the given documents and embeddings in the database.

        Args:
            documents_with_embeddings (dict): A dictionary containing 'text'
                and 'embedding' keys with lists of documents and their
                corresponding embeddings.
            collection_name (str): The name of the collection to create.
                Defaults to "letters".

        Returns:
            None
        """
        documents = documents_with_embeddings["text"]
        embeddings = documents_with_embeddings["embedding"]

        points = [
            PointStruct(id=idx, vector=e, payload={"text": d})
            for idx, (d, e) in enumerate(zip(documents, embeddings))
        ]

        print(
            f"Creating collection {collection_name} with {len(points)} "
            f"points of size {embeddings[0].shape[0]}"
        )
        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=embeddings[0].shape[0], distance=Distance.COSINE
            ),
        )

        self.client.upsert(collection_name, points)

    def find_similar(
        self, embedding, collection_name="letters", top_k=5, min_similarity=0.1
    ):
        """
        Find similar documents in the given collection for the provided embedding.

        This method queries the Qdrant collection for documents that are most similar
        to the provided embedding vector, returning the top k results with a similarity
        score above the specified threshold. The response is converted into a list of
        dictionaries for easier indexing.

        Args:
            embedding (list or numpy.ndarray): The embedding vector to search for similar documents.
            collection_name (str): The name of the collection to search in. Defaults to "letters".
            top_k (int): The maximum number of similar documents to return. Defaults to 5.
            min_similarity (float): The minimum similarity score threshold. Defaults to 0.1.

        Returns:
            list: A list of dictionaries, each containing:
                  - "id": The document's identifier.
                  - "payload": A dictionary with the document content (e.g., {"text": "..."})
                  - "score": The similarity score.
        """
        response = self.client.query_points(
            collection_name=collection_name,
            query=embedding,
            limit=top_k,
            score_threshold=min_similarity,
        )
        return [
            {"id": point.id, "payload": point.payload, "score": point.score}
            for point in response.points
        ]
