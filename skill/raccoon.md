---
name: raccoon
category: alignment
description: "Raccoon (Rigorous Alignment Curation: Cleanup Of Outliers and Noise) cleans up sequence alignments by removing outliers and noise."
tags: [raccoon, alignment, curation, quality-control]
author: oxo-call-community
source_url: "https://github.com/artic-network/raccoon/blob/main/README.md"
---
## Concepts

- **Tool Overview**: raccoon curates alignments.
- **Core Function**: Alignment cleanup.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts alignment files.
- **Output**: Produces cleaned alignments.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Alignment Quality**: Affects curation.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `raccoon --help`
**Explanation:** Shows available options and usage instructions.

### Clean alignment
**Args:** `raccoon clean -i alignment.fasta -o cleaned.fasta`
**Explanation:** Cleans up alignment.

### With parameters
**Args:** `raccoon clean -i alignment.fasta -p params.yaml -o cleaned.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `raccoon -v clean -i alignment.fasta -o cleaned.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `raccoon -t 4 clean -i alignment.fasta -o cleaned.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Remove outliers
**Args:** `raccoon clean -i alignment.fasta -o cleaned.fasta --remove-outliers`
**Explanation:** Removes outlier sequences.

### Generate report
**Args:** `raccoon clean -i alignment.fasta -o cleaned.fasta --report report.html`
**Explanation:** Generates HTML report.