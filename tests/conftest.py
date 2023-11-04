import pytest

from bonsait import ClassTransformer


@pytest.fixture
def class_transformer():
    class_transformer = ClassTransformer(source_class="test_class")
    return class_transformer
