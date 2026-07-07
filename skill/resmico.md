---
name: resmico
category: qc
description: ResMiCo improves metagenome-assembled genomes quality using deep learning.
tags: [resmico, qc, metagenomics, deep-learning]
author: oxo-call-community
source_url: "https://github.com/leylabmpi/ResMiCo"
---

## Concepts

- **Tool Overview**: resmico improves MAG quality.
- **Core Function**: MAG quality improvement.
- **Algorithm**: Uses deep learning methods.
- **Input Format**: Accepts contigs/scaffolds.
- **Output**: Produces improved MAGs.
- **Use Case**: Metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Model Quality**: Affects improvement.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `resmico --help`
**Explanation:** Shows available options and usage instructions.

### Improve MAG quality
**Args:** `resmico improve -i contigs.fasta -o improved.fasta`
**Explanation:** Improves MAG quality using deep learning.

### With parameters
**Args:** `resmico improve -i contigs.fasta -p params.yaml -o improved.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `resmico -v improve -i contigs.fasta -o improved.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `resmico -t 4 improve -i contigs.fasta -o improved.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With model
**Args:** `resmico improve -i contigs.fasta -m model.pt -o improved.fasta`
**Explanation:** Uses custom trained model.

### Generate report
**Args:** `resmico improve -i contigs.fasta -o improved.fasta --report report.html`
**Explanation:** Generates HTML report.