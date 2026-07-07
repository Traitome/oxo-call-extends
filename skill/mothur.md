---
name: mothur
category: metagenomics
description: Comprehensive software for microbial ecology and metagenomics analysis.
tags: [mothur, metagenomics, microbial-ecology]
author: oxo-call-community
source_url: "https://www.mothur.org"
---

## Concepts

- **Tool Overview**: mothur v1.48.5 provides comprehensive bioinformatics tools for microbial ecology.
- **Core Function**: Analyzes microbial community structure from sequencing data.
- **16S rRNA Analysis**: Specialized for 16S rRNA amplicon sequencing data.
- **OTU Clustering**: Groups sequences into operational taxonomic units.
- **Phylogenetic Analysis**: Constructs phylogenetic trees from sequences.
- **Input/Output**: Accepts FASTA, FASTQ, and alignment files; outputs diversity metrics.

## Pitfalls

- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for OTU clustering.
- **Data Quality**: Results depend on sequencing quality and primer selection.
- **Computational Resources**: Large datasets may require significant resources.
- **Runtime**: Complex analyses may take significant time.
- **Version Compatibility**: Some options may vary between versions.

## Examples

### Process 16S data
**Args:** `mothur "#make.contigs(file=seqs.fastq); screen.seqs(); align.seqs();"`
**Explanation:** Processes raw 16S sequencing data through pipeline.

### OTU clustering
**Args:** `mothur "#cluster.split(fasta=aligned.fasta, count=count_table.txt)"`
**Explanation:** Performs OTU clustering using split method.

### Alpha diversity
**Args:** `mothur "#alpha.div(phylip=phylip.dist)"`
**Explanation:** Calculates alpha diversity metrics.

### Beta diversity
**Args:** `mothur "#beta.div(phylip=phylip.dist)"`
**Explanation:** Calculates beta diversity metrics.

### Generate report
**Args:** `mothur "#summary.seqs(fasta=aligned.fasta)"`
**Explanation:** Generates sequence summary report.