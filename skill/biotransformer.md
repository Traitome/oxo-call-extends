---
name: biotransformer
category: annotation
description: Predict small molecule metabolism in mammals and microbiota
tags: [metabolism, metabolite-prediction, small-molecule]
author: oxo-call-community
source_url: "https://bitbucket.org/wishartlab/biotransformer3.0jar"
---

## Concepts
- **Tool Overview**: BioTransformer predicts small molecule metabolism in mammals, gut microbiota, and environmental microbiota. It also assists in metabolite identification.
- **Metabolism Prediction**: Predicts metabolic transformations including Phase I/II metabolism, gut microbial metabolism, and environmental microbial degradation.
- **Applications**: Drug metabolism prediction, metabolomics, environmental chemistry, xenobiotic transformation.

## Pitfalls
- **Prediction Accuracy**: Predictions are computational; experimental validation required.
- **Coverage**: May not predict all possible metabolic transformations.

## Examples
### Predict human metabolism
**Args:** `java -jar biotransformer.jar -k cid -i 2244 -b human -s 1 -o metabolites.sdf`
**Explanation:** Predicts human metabolic products for a compound (aspirin, CID 2244).

### Predict gut microbial metabolism
**Args:** `java -jar biotransformer.jar -k cid -i 2244 -b gut -s 2 -o gut_metabolites.sdf`
**Explanation:** Predicts gut microbial metabolism products (2 steps).
