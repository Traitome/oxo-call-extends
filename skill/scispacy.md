---
name: scispacy
category: nlp
description: scispaCy - A full SpaCy pipeline and models for scientific/biomedical documents
tags: ["scispacy", "nlp", "biomedical", "scientific-text"]
author: oxo-call-community
source_url: "https://allenai.github.io/scispacy"
---

## Concepts

- **Tool Overview**: scispaCy (v0.6.2) provides full SpaCy pipeline and models for scientific/biomedical documents.
- **Core Function**: Offers NLP tools specialized for scientific text processing.
- **Algorithm**: Implements spaCy-based NLP pipelines with biomedical-specific models.
- **Input/Output**: Accepts text documents and produces annotated entities.
- **Biomedical Focus**: Specifically trained on scientific and biomedical literature.
- **Applications**: Named entity recognition, relation extraction, and scientific text analysis.

## Pitfalls

- **Model Size**: Large model files require significant storage.
- **Computational Resources**: May require significant compute resources.
- **Domain Specificity**: Models are trained on specific domains.
- **Version Compatibility**: Different versions may have breaking changes.
- **Memory Usage**: High memory requirements during processing.
- **Training Data**: Model performance depends on training data quality.

## Examples

### Load model
**Args:** `import scispacy; nlp = scispacy.load('en_core_sci_sm')`
**Explanation:** Loads small English scientific model.

### Process text
**Args:** `doc = nlp("The TP53 gene is associated with cancer.")`
**Explanation:** Processes text and extracts entities.

### Entity recognition
**Args:** `for ent in doc.ents: print(ent.text, ent.label_)`
**Explanation:** Prints recognized entities and their labels.

### Large model
**Args:** `import scispacy; nlp = scispacy.load('en_core_sci_lg')`
**Explanation:** Loads large English scientific model.

### Custom pipeline
**Args:** `nlp.add_pipe('scispacy_linker', config={'resolve_abbreviations': True})`
**Explanation:** Adds entity linking component.

### Save model
**Args:** `nlp.to_disk('./sci-model/')`
**Explanation:** Saves trained model to disk.

### Text preprocessing
**Args:** `doc = nlp.pipe(texts, batch_size=100)`
**Explanation:** Processes multiple texts efficiently.