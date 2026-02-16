from functools import lru_cache
from typing import Iterable, List

from sentence_transformers import SentenceTransformer

from config import MODEL_NAME


@lru_cache(maxsize=1)
def get_embedding_model() -> SentenceTransformer:
    return SentenceTransformer(MODEL_NAME)


def embed_text(text: str) -> List[float]:
    model = get_embedding_model()
    return model.encode(text).tolist()


def embed_texts(texts: Iterable[str]) -> List[List[float]]:
    model = get_embedding_model()
    text_list = list(texts)
    return [vector.tolist() for vector in model.encode(text_list)]