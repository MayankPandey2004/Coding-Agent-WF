import os
import chromadb

CHROMA_PATH = os.path.abspath("./chroma_db")
COLLECTION_NAME = "agent_memory"

_client = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_or_create_collection(name=COLLECTION_NAME)


def save_memory(text: str, metadata: dict | None = None) -> None:
    """Store a piece of long-term memory (e.g. a lesson learned from a session)."""
    existing = _collection.count()
    _collection.add(
        documents=[text],
        metadatas=[metadata or {"source": "session"}],
        ids=[f"mem_{existing}_{abs(hash(text)) % 100000}"],
    )


def retrieve_memories(query: str, k: int = 3) -> list[str]:
    """Retrieve the k most relevant past memories for a given query."""
    if _collection.count() == 0:
        return []
    k = min(k, _collection.count())
    results = _collection.query(query_texts=[query], n_results=k)
    docs = results.get("documents", [[]])
    return docs[0] if docs else []


def memory_count() -> int:
    return _collection.count()
