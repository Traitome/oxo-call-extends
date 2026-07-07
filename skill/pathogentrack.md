---
name: pathogentrack
category: expression
description: PathogenTrack identifies pathogenic microorganisms from scRNA-seq data.
tags: [pathogentrack, expression, scrna-seq, pathogen-detection]
author: oxo-call-community
source_url: "https://github.com/ncrna/PathogenTrack"
---

## Concepts

- **Tool Overview**: PathogenTrack detects pathogens in scRNA-seq data.
- **Core Function**: Identifies microbial sequences from single-cell data.
- **Algorithm**: Uses alignment and classification methods.
- **Input Format**: Accepts scRNA-seq reads or count matrices.
- **Output**: Produces pathogen identification results.
- **Use Case**: Single-cell analysis, infectious disease research.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Host Contamination**: May detect host sequences.
- **Sensitivity**: Depends on sequencing depth.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pathogentrack --help`
**Explanation:** Shows available options and usage instructions.

### Detect pathogens
**Args:** `pathogentrack -i counts.h5ad -o results/`
**Explanation:** Identifies pathogens from scRNA-seq data.

### With reads
**Args:** `pathogentrack -r reads.fastq -o results/`
**Explanation:** Processes raw sequencing reads.

### Verbose mode
**Args:** `pathogentrack -v -i counts.h5ad -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pathogentrack -t 8 -i counts.h5ad -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pathogentrack -i counts.h5ad -o results.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pathogentrack -i counts.h5ad -o results/ -r report.html`
**Explanation:** Generates HTML report.