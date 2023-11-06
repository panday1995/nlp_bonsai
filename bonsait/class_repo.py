from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Iterable, Optional

import requests
import torch

from bonsait.configs import BONSAI_ACTIVITY_API, BONSAI_API_KEY, CACHE_DIR


class EmbeddingCache:
    def __init__(self, cache_dir: Path | None = None) -> None:
        if not cache_dir:
            print(f"Use default cache directory {CACHE_DIR}")
            cache_dir = CACHE_DIR
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)

    def _get_hash(self, class_value: Iterable) -> str:
        class_value_byte = json.dumps(class_value, sort_keys=True).encode(
            "utf-8"
        )  # NOTE: `sort_keys` make sure unsorted iterable get the same hash value
        return hashlib.sha256(class_value_byte).hexdigest()

    def _get_file_path(self, hash: str) -> Path:
        return self.cache_dir / f"{hash}.pt"

    def save_embedding(self, encoding, class_value: Iterable):
        hash = self._get_hash(class_value)
        file_path = self._get_file_path(hash)
        torch.save(encoding, file_path)

    def load_embedding(self, class_value: Optional[Iterable]):
        if not class_value:
            return None
        hash = self._get_hash(class_value)
        file_path = self._get_file_path(hash)
        if os.path.exists(file_path):
            return torch.load(file_path)


class BaseClass:
    def __init__(self, name: str, src: Iterable) -> None:
        self.values = src
        self.name = name

    @classmethod
    def from_bonsai(
        cls,
        class_name: str,  # , cache: Optional[ClassCache] = None
    ) -> "BaseClass":
        if class_name == "activity":
            key = BONSAI_API_KEY if BONSAI_API_KEY else None
            class_activity = get_bonsai_activity_classification(key=key)
            return cls(name="activity", src=class_activity)


def get_bonsai_activity_classification(
    url: str = BONSAI_ACTIVITY_API, key: str = None
) -> Iterable[str]:
    """Get BONSAI's activity classification using its API

    Parameters
    ----------
    url : str, optional
        url for bonsai activity classification, by default BONSAI_ACTIVITY_API

    Returns
    -------
    Iterable[str]
        a list of activity classifications
    """

    try:
        headers = None
        if key:
            headers = {"Authorization": f"Token {key}"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        activities_data = response.json()

        activity_names = [activity["description"] for activity in activities_data]
        print(f"successfully fetched activity classifications from {url}")
        return activity_names
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error Connecting: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout Error: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error: {req_err}")  # Ambiguous error
    except Exception as err:
        print(f"An error occurred: {err}")  # Other errors

    return []
