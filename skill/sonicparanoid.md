---
name: sonicparanoid
category: comparative-genomics
description: SonicParanoid - Fast orthology inference with machine learning
tags: [sonicparanoid, comparative-genomics, orthology, machine-learning, evolution]
author: oxo-call-community
source_url: "https://gitlab.com/salvo981/sonicparanoid2"
---

## Concepts

- **Tool Overview**: sonicparanoid (v2.0.9) - An orthology inference tool
- **Core Function**: Infers orthologous genes between species
- **Input/Output**: Accepts protein sequences; outputs orthology groups
- **Algorithm**: Machine learning and language models for orthology prediction
- **Installation**: `conda install -c bioconda sonicparanoid`
- **Key Features**: Fast orthology inference, ML-based, comprehensive results

## Pitfalls

- **Input Requirements**: Requires properly formatted protein sequences
- **Database**: Requires protein database for comparison
- **Species Coverage**: Multiple species require proper configuration
- **Memory Usage**: Large protein sets require significant memory
- **Output Format**: Output format depends on configuration
- **Training Data**: ML model requires proper training data

## Examples

### Display help
**Args:** `sonicparanoid --help`
**Explanation:** Shows available options and usage information.

### Basic orthology inference
**Args:** `sonicparanoid -i proteins.fasta -o orthology_groups.tsv`
**Explanation:** Infer orthology groups from proteins.

### With multiple species
**Args:** `sonicparanoid -i species1.fasta species2.fasta -o orthology_groups.tsv`
**Explanation:** Infer orthology between multiple species.

### With machine learning
**Args:** `sonicparanoid -i proteins.fasta -o orthology_groups.tsv --ml`
**Explanation:** Use machine learning for inference.

### With coverage threshold
**Args:** `sonicparanoid -i proteins.fasta -o orthology_groups.tsv --coverage 0.5`
**Explanation:** Set coverage threshold for orthology.

### Output detailed results
**Args:** `sonicparanoid -i proteins.fasta -o orthology_groups.tsv --detailed`
**Explanation:** Output detailed orthology results.

### With threads
**Args:** `sonicparanoid -i proteins.fasta -o orthology_groups.tsv -p 8`
**Explanation:** Use multiple threads for inference.

### Generate report
**Args:** `sonicparanoid -i proteins.fasta -o orthology_groups.tsv --report`
**Explanation:** Generate orthology inference report.