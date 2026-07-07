---
name: seer
category: sequence-analysis
description: seer - Sequence element (k-mer) enrichment analysis
tags: ["seer", "sequence-analysis", "k-mer", "enrichment"]
author: oxo-call-community
source_url: "https://github.com/johnlees/seer"
---

## Concepts

- **Tool Overview**: seer (v1.1.4) performs sequence element (k-mer) enrichment analysis.
- **Core Function**: Identifies enriched k-mer sequences associated with phenotypes or traits.
- **Algorithm**: Uses association testing to find statistically significant k-mer enrichments.
- **Input/Output**: Accepts FASTA files and produces k-mer association results.
- **k-mer Analysis**: Focuses on short sequence elements for association studies.
- **Applications**: GWAS, microbial genomics, and sequence analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Multiple Testing**: Requires proper correction for multiple comparisons.
- **False Positives**: May incorrectly identify enriched k-mers.
- **k-mer Size**: Choosing the right k-mer size affects performance.

## Examples

### Basic analysis
**Args:** `seer -i sequences.fasta -o results.txt`
**Explanation:** `-i` input FASTA; `-o` output results.

### With phenotype file
**Args:** `seer -i sequences.fasta -p phenotypes.txt -o results.txt`
**Explanation:** `-p` specifies phenotype file.

### k-mer size
**Args:** `seer -i sequences.fasta -k 31 -o results.txt`
**Explanation:** `-k 31` sets k-mer size to 31.

### Verbose logging
**Args:** `seer -i sequences.fasta -v -o results.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `seer -i sequences.fasta -t 8 -o results.txt`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Quality filtering
**Args:** `seer -i sequences.fasta -q 20 -o results.txt`
**Explanation:** `-q 20` filters low-quality sequences.

### Help command
**Args:** `seer --help`
**Explanation:** Shows available commands and options.