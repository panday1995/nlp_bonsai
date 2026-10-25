# BonsaiT: an interface for BONSAI classifications

BonsaiT is a Python package for the standardization of classifications in Life-Cycle Assessment (LCA). It leverages NLP to aligns external classification systems with the BONSAI framework, ensuring data consistency across LCA datasets.

Key components include the `Encoder`, which converts text to vectors via language models like Sentence Transformers and Hugging Face's BERT, and the `BonsaiTransformer`, which identifies the BONSAI class most similar to a given source class through vector analysis and cosine similarity.

BonsaiT can be used to:

- Identify the BONSAI class most similar to a given source class.
- Translate classifications between different systems.
- Harmonize LCA data from different sources.

## Installation

Requires Python 3.11 or 3.12. Python 3.10 is no longer supported because
Pillow 13 (required for the October 2026 security fixes) requires Python 3.11+.
NumPy remains on the 1.x series to avoid an unrelated NumPy 2 migration.

For development, use Poetry 2.5.1 and install the committed lockfile with
`poetry sync`. The security refresh upgrades Sentence Transformers from 2.x
to 6.x; only load models from trusted sources and validate your model-specific
embedding results before deploying. Existing installations must be upgraded;
changing this repository does not patch environments already deployed.

To get started with BonsaiT, install it via pip:
```Bash
pip install bonsait
```

## Quick start

Here is how to quickly implement BonsaiT in your project:

```Python
from bonsait import BonsaiTransformer

source_class = "electricity from coal"

# Set up the BonsaiTransformer
class_transformer = BonsaiTransformer()

# Perform the transformation to find the BONSAI equivalent
transformed_class = class_transformer.match(source_class=source_class)
print(f"The source classification <{source_class}> is transformed into BONSAI classification: <{transformed_class}>")
```


## License

BonsaiT is released under the MIT License
