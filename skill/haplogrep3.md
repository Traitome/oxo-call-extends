---
name: haplogrep3
category: bioinformatics
description: HaploGrep3 is a tool for mtDNA haplogroup classification and phylogenetic analysis.
tags: [haplogrep3, mtDNA, haplogroup, bioinformatics]
author: oxo-call-community
source_url: "https://haplogrep.readthedocs.io/en/latest"
---

## Concepts

- **mtDNA Haplogroup Classification**: HaploGrep3 classifies mtDNA haplogroups.

- **Phylogenetic Analysis**: Performs phylogenetic analysis of mtDNA sequences.

- **Human Population Genetics**: Used in human population genetics studies.

- **Sequence Variants**: Analyzes mtDNA sequence variants.

- **Haplogroup Prediction**: Predicts haplogroup assignments.

- **Quality Control**: Provides QC metrics for mtDNA data.

## Pitfalls

- **Sequence Quality**: Low-quality sequences may affect classification.

- **Reference Database**: Ensure using up-to-date reference database.

- **Ambiguous Results**: Some samples may have ambiguous assignments.

- **Data Format**: Ensure correct input format.

- **Population Specificity**: Results may vary by population.

## Examples

### Classify haplogroup
**Args:** `haplogrep3 classify -i input.fasta -o haplogroup.txt`
**Explanation:** Classifies mtDNA haplogroup from sequence.

### With VCF input
**Args:** `haplogrep3 classify -v variants.vcf -o haplogroup.txt`
**Explanation:** Uses VCF file for haplogroup classification.

### Batch processing
**Args:** `for f in *.fasta; do haplogrep3 classify -i $f -o ${f%.fasta}_haplogroup.txt; done`
**Explanation:** Processes multiple FASTA files.

### Generate report
**Args:** `haplogrep3 classify -i input.fasta -report -o report.html`
**Explanation:** Generates comprehensive classification report.

### Update database
**Args:** `haplogrep3 update`
**Explanation:** Updates reference database to latest version.

### Phylogenetic tree
**Args:** `haplogrep3 tree -i input.fasta -o tree.nwk`
**Explanation:** Generates phylogenetic tree from sequences.

### Help command
**Args:** `haplogrep3 --help`
**Explanation:** Shows available options and usage information.