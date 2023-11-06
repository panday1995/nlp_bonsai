import torch


def test_encode_source_class(class_transformer):
    embedding_src = class_transformer.encode_source_class(source_class="test_class")

    assert embedding_src is not None
    assert isinstance(embedding_src, torch.Tensor)


def test_encode_target_class(class_transformer):
    embedding_target = class_transformer.encode_target_class()

    assert embedding_target is not None
    assert isinstance(embedding_target, list)


def test_transform(class_transformer):
    transformed_class = class_transformer.transform(source_class="test_class")
    assert isinstance(transformed_class, str)
    assert transformed_class in class_transformer._target_class.values
