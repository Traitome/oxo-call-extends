---
name: rdp_classifier
category: metagenomics
description: RDP Classifier is a naive Bayesian classifier that can rapidly and accurately provide taxonomic assignments from domain to genus.
tags: [rdp_classifier, metagenomics, taxonomy, classification]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/rdp-classifier/"
---

## Concepts

- **Tool Overview**: rdp_classifier classifies sequences.
- **Core Function**: Taxonomic classification.
- **Algorithm**: Uses Bayesian methods.
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
**Args:** `rdp_classifier --help`
**Explanation:** Shows available options and usage instructions.

### Classify sequences
**Args:** `rdp_classifier classify -i sequences.fasta -o classifications.txt`
**Explanation:** Classifies sequences taxonomically.

### With parameters
**Args:** `rdp_classifier classify -i sequences.fasta -p params.yaml -o classifications.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rdp_classifier -v classify -i sequences.fasta -o classifications.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rdp_classifier -t 4 classify -i sequences.fasta -o classifications.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With confidence threshold
**Args:** `rdp_classifier classify -i sequences.fasta -c 0.8 -o classifications.txt`
**Explanation:** Uses confidence threshold.

### Generate report
**Args:** `rdp_classifier classify -i sequences.fasta -o classifications.txt --report report.html`
**Explanation:** Generates HTML report.