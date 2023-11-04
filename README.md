# BonsaiT: An Interface for BONSAI classifications

BonsaiT is a Python package for the standardization of Life-Cycle Assessment (LCA) data. It leverages NPL to aligns external classification systems with the BONSAI framework, ensuring data consistency across LCA datasets.

Key components include the Encoder, which converts text to vectors via language models like Sentence Transformers and Hugging Face's BERT, and the ClassTransformer, which identifies the BONSAI class most similar to a given source class through vector analysis and cosine similarity.

BonsaiT streamlines LCA data harmonization, enabling more accurate environmental impact assessments.

## Installation

To get started with BonsaiT, install it via pip:
```Bash
pip install bonsait
```

## Quick start

Here’s how to quickly implement BonsaiT in your project:

```Python
from bonsait import ClassTransformer

source_class = "electricity from coal"

# Set up the ClassTransformer with your source classification
class_transformer = ClassTransformer(source_class=source_class)

# Perform the transformation to find the BONSAI equivalent
transformed_class = class_transformer.transform()
print(f"The source classification <{source_class}> is transformed into BONSAI classification: <{transformed_class}>")
```


## License

BonsaiT is released under the MIT License