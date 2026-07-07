---
name: orthologer
category: annotation
description: Orthologer detects orthologs for comparative genomics and functional annotation.
tags: [orthologer, annotation, orthology, comparative-genomics]
author: oxo-call-community
source_url: "https://orthologer.ezlab.org"
---

## Concepts

- **Tool Overview**: Orthologer identifies orthologous genes across species.
- **Core Function**: Detects orthologs for functional annotation.
- **Algorithm**: Uses graph-based orthology detection.
- **Input Format**: Accepts protein sequence files.
- **Output**: Produces ortholog assignments and annotations.
- **Use Case**: Comparative genomics, gene annotation, and evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Species Coverage**: Limited by database coverage.
- **Annotation Quality**: Depends on reference data.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `orthologer --help`
**Explanation:** Shows available options and usage instructions.

### Run ortholog detection
**Args:** `orthologer -i proteins.fasta -o orthologs.txt`
**Explanation:** Detects orthologs in protein sequences.

### With reference
**Args:** `orthologer -i proteins.fasta -r reference.fasta -o orthologs.txt`
**Explanation:** Uses reference sequences.

### Output format
**Args:** `orthologer -i proteins.fasta -o orthologs.json --json`
**Explanation:** Outputs in JSON format.

### Verbose mode
**Args:** `orthologer -i proteins.fasta -v -o orthologs.txt`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `orthologer batch -d fastas/ -o results/`
**Explanation:** Processes multiple sequence files.

### Quality filtering
**Args:** `orthologer -i proteins.fasta -q 0.9 -o orthologs.txt`
**Explanation:** Filters by quality threshold.