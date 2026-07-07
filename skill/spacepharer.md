---
name: spacepharer
category: microbiology
description: SpacePHARER - Sensitive identification of phages from CRISPR spacers
tags: [spacepharer, microbiology, phage, crispr, spacer, identification]
author: oxo-call-community
source_url: "https://github.com/soedinglab/spacepharer"
---

## Concepts

- **Tool Overview**: spacepharer (v5.c2e680a) - A phage identification tool
- **Core Function**: Identifies phages from CRISPR spacers in prokaryotic hosts
- **Input/Output**: Accepts CRISPR spacers; outputs phage identifications
- **Algorithm**: Sensitive matching of spacers to phage sequences
- **Installation**: `conda install -c bioconda spacepharer`
- **Key Features**: Phage identification, CRISPR analysis, sensitive detection

## Pitfalls

- **Input Requirements**: Requires properly formatted CRISPR spacer sequences
- **Phage Database**: Requires phage database for identification
- **Spacer Quality**: Quality of spacers affects identification accuracy
- **Memory Usage**: Large databases require significant memory
- **Output Format**: Output format depends on configuration
- **Interpretation**: Results require biological interpretation

## Examples

### Display help
**Args:** `spacepharer --help`
**Explanation:** Shows available options and usage information.

### Basic phage identification
**Args:** `spacepharer -i spacers.fasta -d phage_db/ -o phages.tsv`
**Explanation:** Identify phages from CRISPR spacers.

### With host genome
**Args:** `spacepharer -i spacers.fasta -d phage_db/ -h host.fasta -o phages.tsv`
**Explanation:** Use host genome for context.

### With sensitivity
**Args:** `spacepharer -i spacers.fasta -d phage_db/ -o phages.tsv --sensitive`
**Explanation:** Use sensitive mode for identification.

### With e-value threshold
**Args:** `spacepharer -i spacers.fasta -d phage_db/ -o phages.tsv --evalue 0.001`
**Explanation:** Set e-value threshold for matches.

### Output detailed results
**Args:** `spacepharer -i spacers.fasta -d phage_db/ -o phages.tsv --detailed`
**Explanation:** Output detailed identification results.

### Output statistics
**Args:** `spacepharer -i spacers.fasta -d phage_db/ -o phages.tsv --stats`
**Explanation:** Output identification statistics.

### Generate report
**Args:** `spacepharer -i spacers.fasta -d phage_db/ -o phages.tsv --report`
**Explanation:** Generate identification report.