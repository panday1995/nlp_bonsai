from typing import List, Optional, Union

import torch
from sentence_transformers import SentenceTransformer, util
from transformers import AutoModel


class CorrFinder:
    def __init__(
        self, model: Union[SentenceTransformer, AutoModel], device: str = "cpu"
    ) -> None:
        self._model = model
        self._device = device
        self._text: Optional[str] = None

    @classmethod
    def from_sentence_transformer(cls, model_name: str, device: str = "cpu"):
        encoder = SentenceTransformer(model_name, device)
        return cls(encoder)

    # TODO: Add hugging face bert models
    @classmethod
    def from_hugging_face(cls, model_name: str, device: str = "cpu"):
        ...

    @property
    def text(self) -> Optional[str]:
        return self._text

    @text.setter
    def set_text(self, text: str):
        return text

    def _encode_text(self):
        if isinstance(self._model, SentenceTransformer):
            array_text = self._model.encode(self._text, convert_to_tensor=True)
            return array_text

    def compute_similarity(
        self,
        target_vectors: List[torch.Tensor],
        similarity_func: callable,
    ):
        matrix_text = self._encode_text().unsqueeze(0)
        matrix_target = torch.stack(target_vectors).to(self._device)
        similarities = similarity_func(matrix_text, matrix_target)
        idx_most_similar = torch.argmax(similarities)
        return idx_most_similar
