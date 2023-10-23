import torch


def cosine_similarity(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    a_norm = a / a.norm(dim=1)[:, None]
    b_norm = b / b.norm(dim=1)[:, None]
    return torch.mm(a_norm, b_norm.transpose(0, 1))
