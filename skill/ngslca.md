---
name: ngslca
category: taxonomy
description: ngsLCA performs fast taxonomic classification of DNA reads using LCA algorithm.
tags: [ngslca, taxonomy, classification, lca]
author: oxo-call-community
source_url: "https://github.com/miwipe/ngsLCA"
---

## Concepts

- **Tool Overview**: ngsLCA classifies sequencing reads to taxonomic groups using LCA.
- **Core Function**: Determines taxonomic origin of sequencing reads.
- **Algorithm**: Uses Lowest Common Ancestor (LCA) approach for classification.
- **Input Format**: Accepts BAM files aligned to reference databases.
- **Output**: Produces taxonomic classification reports.
- **Use Case**: Metagenomics analysis, contamination detection, and species identification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Database**: Requires properly formatted reference database.
- **Memory Usage**: Large databases require memory.
- **Classification Accuracy**: Depends on database completeness.
- **Computational Cost**: Analysis can be computationally intensive.
- **Ambiguous Reads**: Some reads may remain unclassified.

## Examples

### Display help
**Args:** `ngslca --help`
**Explanation:** Shows available options and usage instructions.

### Run classification
**Args:** `ngslca -i alignment.bam -d database/ -o results.txt`
**Explanation:** Classifies reads using reference database.

### Output JSON
**Args:** `ngslca -i alignment.bam -d database/ --json -o results.json`
**Explanation:** Outputs results in JSON format.

### Minimum confidence
**Args:** `ngslca -i alignment.bam -d database/ -c 0.8 -o results.txt`
**Explanation:** Sets minimum confidence threshold.

### Taxonomic level
**Args:** `ngslca -i alignment.bam -d database/ -l species -o results.txt`
**Explanation:** Reports classification at species level.

### Threads
**Args:** `ngslca -i alignment.bam -d database/ -t 8 -o results.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Summary report
**Args:** `ngslca -i alignment.bam -d database/ --summary -o summary.txt`
**Explanation:** Generates summary statistics.