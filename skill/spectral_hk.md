---
name: spectral_hk
category: chemistry
description: Spectral_HK - NCGC Spectral HashKey for chemical compounds
tags: [spectral_hk, chemistry, spectral-hash, chemical-compounds, fingerprint]
author: oxo-call-community
source_url: "https://bitbucket.org/ncgc/spectral_hk"
---

## Concepts

- **Tool Overview**: spectral_hk (v0.1) - A spectral hash key tool
- **Core Function**: Generates spectral hash keys for chemical compounds
- **Input/Output**: Accepts chemical structures; outputs hash keys
- **Algorithm**: Spectral hashing for chemical fingerprints
- **Installation**: `conda install -c bioconda spectral_hk`
- **Key Features**: Spectral hashing, chemical fingerprints, compound identification

## Pitfalls

- **Input Requirements**: Requires properly formatted chemical structures
- **Structure Quality**: Structure quality affects hash generation
- **Hash Parameters**: Hash parameters affect key uniqueness
- **Memory Usage**: Large compound sets require significant memory
- **Output Format**: Output format depends on configuration
- **Hash Collisions**: Hash collisions may occur with similar structures

## Examples

### Display help
**Args:** `spectral_hk --help`
**Explanation:** Shows available options and usage information.

### Basic hash generation
**Args:** `spectral_hk -i compounds.smi -o hash_keys.txt`
**Explanation:** Generate spectral hash keys from SMILES.

### With hash parameters
**Args:** `spectral_hk -i compounds.smi -o hash_keys.txt --bits 1024`
**Explanation:** Set hash bit size.

### Multiple compounds
**Args:** `spectral_hk -i compound1.smi compound2.smi -o hash_keys.txt`
**Explanation:** Generate hash keys for multiple compounds.

### Output detailed results
**Args:** `spectral_hk -i compounds.smi -o hash_keys.txt --detailed`
**Explanation:** Output detailed hash information.

### Output fingerprints
**Args:** `spectral_hk -i compounds.smi -o hash_keys.txt --fingerprints`
**Explanation:** Output chemical fingerprints.

### Output statistics
**Args:** `spectral_hk -i compounds.smi -o hash_keys.txt --stats`
**Explanation:** Output hash statistics.

### Generate report
**Args:** `spectral_hk -i compounds.smi -o hash_keys.txt --report`
**Explanation:** Generate hash generation report.

### With threads
**Args:** `spectral_hk -i compounds.smi -o hash_keys.txt -p 8`
**Explanation:** Use multiple threads for hash generation.