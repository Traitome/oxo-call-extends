---
name: mhcnuggets
category: variant-calling
description: MHCnuggets: Neoantigen peptide MHC binding prediction for class I and II
tags: [mhcnuggets, variant-calling]
author: oxo-call-community
source_url: "http://karchinlab.org/apps/mhcnuggets.html"
---

## Concepts

- **Tool Overview**: mhcnuggets v2.4.1 - # MHCnuggets  Welcome to MHCnuggets! Presumably you're here to do some peptide-MHC prediction and not because you were [hungry](https://www.mcdonalds.com/us/en-us/product/chicken-mcnuggets-4-piece.html).  ### Usage ### For an overview of how to use MHCnuggets please refer to the Jupyter notebook called `user_guide.ipynb` in the repository  ### Installation ###  MHCnuggets is `pip` installable as: ```bash pip install mhcnuggets ```  **Required pacakges:**  * numpy * scipy * scikit-learn * tensorflow * keras  You might want to check if the Keras backend is configured to use the Tensforflow backend..
- **Core Function**: MHCnuggets: Neoantigen peptide MHC binding prediction for class I and II
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mhcnuggets`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
