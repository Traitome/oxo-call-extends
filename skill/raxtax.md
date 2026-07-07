---
name: raxtax
category: metagenomics
description: RaxTax is a k-mer-based non-Bayesian taxonomic classifier for metagenomic samples.
tags: [raxtax, metagenomics, taxonomy, classification]
author: oxo-call-community
source_url: "https://github.com/noahares/raxtax"
---

## Concepts

- **Tool Overview**: raxtax classifies sequences.
- **Core Function**: Taxonomic classification.
- **Algorithm**: Uses k-mer methods.
- **Input Format**: Accepts sequence files.
- **Output**: Produces taxonomic assignments.
- **Use Case**: Metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Database Quality**: Affects classification.
- **Parameters**: Must be configured.
- **Runtime**: Classification may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `raxtax --help`
**Explanation:** Shows available options and usage instructions.

### Classify sequences
**Args:** `raxtax classify -i sequences.fasta -d database/ -o classifications.txt`
**Explanation:** Classifies sequences taxonomically.

### With parameters
**Args:** `raxtax classify -i sequences.fasta -p params.yaml -o classifications.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `raxtax -v classify -i sequences.fasta -o classifications.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `raxtax -t 4 classify -i sequences.fasta -o classifications.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With k-mer size
**Args:** `raxtax classify -i sequences.fasta -k 31 -o classifications.txt`
**Explanation:** Uses specific k-mer size.

### Generate report
**Args:** `raxtax classify -i sequences.fasta -o classifications.txt --report report.html`
**Explanation:** Generates HTML report.