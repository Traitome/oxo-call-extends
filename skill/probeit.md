---
name: probeit
category: genome-editing
description: probeit designs probes for pathogen detection and genotyping.
tags: [probeit, genome-editing, probe-design, diagnostics]
author: oxo-call-community
source_url: "https://github.com/steineggerlab/probeit"
---

## Concepts

- **Tool Overview**: probeit designs diagnostic probes.
- **Core Function**: Probe design for pathogens.
- **Algorithm**: Uses sequence analysis methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces probe sequences.
- **Use Case**: Pathogen detection, diagnostics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Probe Specificity**: May have cross-reactivity.
- **Runtime**: Design may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `probeit --help`
**Explanation:** Shows available options and usage instructions.

### Design probes
**Args:** `probeit -i pathogen.fasta -o probes.txt`
**Explanation:** Designs probes for pathogen detection.

### With parameters
**Args:** `probeit -i pathogen.fasta -p params.yaml -o probes.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `probeit -v -i pathogen.fasta -o probes.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `probeit -t 4 -i pathogen.fasta -o probes.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `probeit -i pathogen.fasta -o probes.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `probeit -i pathogen.fasta -o probes.txt --report report.html`
**Explanation:** Generates HTML report.