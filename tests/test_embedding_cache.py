import numpy as np


def test_save_and_load_embedding(embedding_cache, temp_dir):
    class_value = ["test_class_1", "test_class_2"]
    encoding = np.random.rand(3, 5)  # Example encoding

    # Save the encoding
    embedding_cache.save_embedding(encoding, class_value)

    # Ensure the file is saved
    hash = embedding_cache._get_hash(class_value)
    file_path = temp_dir / f"{hash}.pt"
    assert file_path.exists()

    # Load the encoding
    loaded_encoding = embedding_cache.load_embedding(class_value)
    assert loaded_encoding is not None
    np.testing.assert_array_equal(loaded_encoding, encoding)


def test_load_nonexistent_embedding(embedding_cache):
    class_value = ["nonexistent_class"]
    # Attempt to load a non-existent encoding
    loaded_encoding = embedding_cache.load_embedding(class_value)
    assert loaded_encoding is None
