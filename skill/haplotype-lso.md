---
name: haplotype-lso
category: bioinformatics
description: Haplotype analysis for Candidatus Liberibacter solanacearum (Lso) from targeted amplicon capillary sequencing data.
tags: [haplotype-lso, plant-pathogen, haplotype-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/holtgrewe/haplotype-lso"
---

## Concepts

- **Lso Haplotype Analysis**: haplotype-lso analyzes Lso haplotypes.

- **Capillary Sequencing**: Works with capillary sequencing data.

- **Targeted Amplicons**: Designed for targeted amplicon data.

- **Plant Pathogen**: Focused on Candidatus Liberibacter solanacearum.

- **Haplotype Identification**: Identifies Lso haplotypes from sequencing data.

- **Population Analysis**: Supports population-level analysis.

## Pitfalls

- **Data Type**: Requires capillary sequencing data.

- **Target Specific**: Designed specifically for Lso targets.

- **Reference Database**: Ensure using correct reference sequences.

- **Amplicon Design**: Results depend on amplicon design.

- **Sequence Quality**: Low-quality sequences may affect analysis.

## Examples

### Analyze Lso haplotypes
**Args:** `haplotype-lso --input sequences.fasta --output haplotypes.txt`
**Explanation:** Analyzes Lso haplotypes from sequences.

### With quality filtering
**Args:** `haplotype-lso --input sequences.fasta --min-quality 30 --output haplotypes.txt`
**Explanation:** Filters sequences by quality.

### Batch processing
**Args:** `for f in *.fasta; do haplotype-lso --input $f --output ${f%.fasta}_haplotypes.txt; done`
**Explanation:** Processes multiple sequence files.

### Generate report
**Args:** `haplotype-lso --input sequences.fasta --report --output report.html`
**Explanation:** Generates comprehensive analysis report.

### Phylogenetic tree
**Args:** `haplotype-lso --input sequences.fasta --tree --output tree.nwk`
**Explanation:** Generates phylogenetic tree from haplotypes.

### Update database
**Args:** `haplotype-lso --update-db`
**Explanation:** Updates reference database.

### Help command
**Args:** `haplotype-lso --help`
**Explanation:** Shows available options and usage information.