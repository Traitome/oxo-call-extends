---
name: platypus-conquistador
category: metagenomics
description: platypus-conquistador confirms taxonomic groups in metagenomic samples.
tags: [platypus-conquistador, metagenomics, taxonomy, verification]
author: oxo-call-community
source_url: "https://github.com/biocore/Platypus-Conquistador"
---

## Concepts

- **Tool Overview**: platypus-conquistador verifies taxonomic groups.
- **Core Function**: Taxonomic group confirmation.
- **Algorithm**: Uses sequence alignment methods.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces taxonomic verification results.
- **Use Case**: Metagenomics, taxonomic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Classification Accuracy**: May have verification errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `platypus-conquistador --help`
**Explanation:** Shows available options and usage instructions.

### Confirm taxonomic groups
**Args:** `platypus-conquistador -i mapping.bam -o taxonomy.txt`
**Explanation:** Confirms specific taxonomic groups.

### With parameters
**Args:** `platypus-conquistador -i mapping.bam -p params.yaml -o taxonomy.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `platypus-conquistador -v -i mapping.bam -o taxonomy.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `platypus-conquistador -t 4 -i mapping.bam -o taxonomy.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `platypus-conquistador -i mapping.bam -o taxonomy.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `platypus-conquistador -i mapping.bam -o taxonomy.txt --report report.html`
**Explanation:** Generates HTML report.