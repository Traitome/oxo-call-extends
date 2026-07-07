---
name: uchime
category: analysis
description: UCHIME - Tool for detecting chimeric sequences in amplicon data.
tags: [uchime, chimera-detection, amplicon-sequencing, bioinformatics, microbiology]
author: oxo-call-community
source_url: "https://www.drive5.com/usearch/manual/uchime_algo.html"
---

## Concepts

- **Tool Overview**: UCHIME - A tool for detecting chimeric sequences in amplicon sequencing data.
- **Core Function**: Identifies chimeric sequences formed by PCR recombination.
- **Input**: Sequence alignments, amplicon sequences.
- **Output**: Chimeric sequence predictions, confidence scores.
- **Installation**: `conda install -c bioconda uchime`
- **Use Case**: Amplicon sequencing, microbiome analysis, sequence validation.

## Pitfalls

- **Sensitivity**: May miss complex chimeras.
- **Reference Database**: Requires good reference database.

## Examples

### Detect chimeras
**Args:** `uchime -i sequences.fasta -o chimeras.txt`
**Explanation:** Detect chimeric sequences in amplicon data.

### With reference
**Args:** `uchime_ref -i reads.fasta -d reference.fasta -o results/`
**Explanation:** Detect chimeras using reference database.
