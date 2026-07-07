---
name: plastedma
category: annotation
description: plastedma analyzes plastic-degrading enzymes in metagenomic data.
tags: [plastedma, annotation, plastic-degrading, enzymes]
author: oxo-call-community
source_url: "https://github.com/ozefreitas/PlastEDMA"
---

## Concepts

- **Tool Overview**: plastedma identifies plastic-degrading enzymes.
- **Core Function**: Plastic enzyme detection in metagenomes.
- **Algorithm**: Uses HMMER-based search methods.
- **Input Format**: Accepts amino acid sequence files.
- **Output**: Produces enzyme detection results.
- **Use Case**: Environmental metagenomics, bioremediation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Detection Accuracy**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plastedma --help`
**Explanation:** Shows available options and usage instructions.

### Analyze sequences
**Args:** `plastedma -i sequences.fasta -o results/`
**Explanation:** Analyzes sequences for plastic-degrading enzymes.

### With parameters
**Args:** `plastedma -i sequences.fasta -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plastedma -v -i sequences.fasta -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plastedma -t 4 -i sequences.fasta -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plastedma -i sequences.fasta -o results.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `plastedma -i sequences.fasta -o results/ --report report.html`
**Explanation:** Generates HTML report.