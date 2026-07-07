---
name: haplogrep
category: bioinformatics
description: HaploGrep is a tool for mtDNA haplogroup classification (legacy version).
tags: [haplogrep, mtDNA, haplogroup, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/seppinho/haplogrep-cmd"
---

## Concepts

- **mtDNA Haplogroup Classification**: HaploGrep classifies mtDNA haplogroups.

- **Human mtDNA Analysis**: Analyzes human mitochondrial DNA sequences.

- **Haplogroup Prediction**: Predicts haplogroup assignments from mtDNA.

- **Population Genetics**: Used in population genetics research.

- **Sequence Analysis**: Analyzes mtDNA sequence variations.

- **Legacy Tool**: Older version; consider using HaploGrep3.

## Pitfalls

- **Database Updates**: Database may be outdated compared to newer versions.

- **Sequence Quality**: Low-quality sequences may affect classification.

- **Ambiguous Results**: Some samples may have ambiguous assignments.

- **Data Format**: Ensure correct input format.

- **Deprecated**: Consider migrating to HaploGrep3 for newer features.

## Examples

### Classify haplogroup
**Args:** `haplogrep -i input.fasta -o haplogroup.txt`
**Explanation:** Classifies mtDNA haplogroup from sequence.

### With VCF input
**Args:** `haplogrep -v variants.vcf -o haplogroup.txt`
**Explanation:** Uses VCF file for haplogroup classification.

### Batch processing
**Args:** `for f in *.fasta; do haplogrep -i $f -o ${f%.fasta}_haplogroup.txt; done`
**Explanation:** Processes multiple FASTA files.

### Generate report
**Args:** `haplogrep -i input.fasta -r -o report.html`
**Explanation:** Generates classification report.

### Update database
**Args:** `haplogrep --update`
**Explanation:** Updates reference database.

### Help command
**Args:** `haplogrep --help`
**Explanation:** Shows available options and usage information.