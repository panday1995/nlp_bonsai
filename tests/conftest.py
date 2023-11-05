from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from bonsait import BaseClass, BonsaiTransformer, EmbeddingCache


@pytest.fixture
def temp_dir():
    with TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


@pytest.fixture
def class_transformer():
    class_transformer = BonsaiTransformer(source_class="test_class")
    return class_transformer


@pytest.fixture
def embedding_cache(temp_dir):
    embedding_cache = EmbeddingCache(temp_dir)
    return embedding_cache


# TODO: add test for BaseClass
