---
name: mdmcleaner
category: qc
description: Pipeline for assessment, classification and refinement of microbial dark matter SAGs and MAGs.
tags: [mdmcleaner, metagenomics, genome-quality]
author: oxo-call-community
source_url: "https://github.com/KIT-IBG-5/mdmcleaner"
---

## Concepts

- **Tool Overview**: mdmcleaner processes and refines microbial dark matter genomes.
- **Core Function**: Assesses and improves quality of SAGs/MAGs.
- **Quality Assessment**: Evaluates genome completeness and contamination.
- **Taxonomic Classification**: Classifies microbial dark matter.
- **Refinement**: Improves genome quality through filtering.
- **Installation**: `conda install -c bioconda mdmcleaner`

## Pitfalls

- **Data Requirements**: Requires high-quality draft genomes.
- **Computation Time**: Slow for large datasets.
- **Memory Requirements**: High memory for complex analyses.
- **Parameter Tuning**: Requires careful threshold adjustment.
- **Reference Databases**: Depends on up-to-date databases.
- **Output Interpretation**: Results require biological knowledge.

## Examples

### Assess genome quality
**Args:** `mdmcleaner assess -i genome.fasta -o report.txt`
**Explanation:** Assesses genome completeness and contamination.

### Classify genomes
**Args:** `mdmcleaner classify -i genome.fasta -o taxonomy.txt`
**Explanation:** Classifies microbial dark matter.

### Refine genomes
**Args:** `mdmcleaner refine -i genome.fasta -o refined.fasta`
**Explanation:** Improves genome quality.

### Batch processing
**Args:** `mdmcleaner batch -d genomes/ -o results/`
**Explanation:** Processes multiple genomes.

### Help documentation
**Args:** `mdmcleaner --help`
**Explanation:** Displays available commands and options.
