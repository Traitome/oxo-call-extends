---
name: omark
category: qc
description: OMArk assesses proteome quality based on OMAmer orthology placements.
tags: [omark, qc, proteome-quality, orthology]
author: oxo-call-community
source_url: "https://github.com/DessimozLab/omark"
---

## Concepts

- **Tool Overview**: OMArk evaluates proteome completeness and quality.
- **Core Function**: Assesses proteome quality using orthology information.
- **Algorithm**: Uses OMAmer placements for quality assessment.
- **Input Format**: Accepts FASTA protein sequences.
- **Output**: Produces quality scores and completeness metrics.
- **Use Case**: Genome annotation, proteome evaluation, and quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Database Requirements**: Requires OMA database.
- **Sequence Quality**: Results depend on input sequence quality.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Validation**: Results should be validated with other methods.

## Examples

### Display help
**Args:** `omark --help`
**Explanation:** Shows available options and usage instructions.

### Assess proteome
**Args:** `omark assess -i proteome.fasta -o quality.txt`
**Explanation:** Assesses proteome quality.

### With database
**Args:** `omark assess -i proteome.fasta -d oma_db -o quality.txt`
**Explanation:** Uses custom OMA database.

### Output format
**Args:** `omark assess -i proteome.fasta -o results.csv --csv`
**Explanation:** Outputs results in CSV format.

### Verbose mode
**Args:** `omark assess -i proteome.fasta -v -o quality.txt`
**Explanation:** Runs with verbose output.

### Generate report
**Args:** `omark report -i proteome.fasta -o report.html`
**Explanation:** Generates HTML quality report.

### Batch processing
**Args:** `omark batch -d proteomes/ -o results/`
**Explanation:** Processes multiple proteome files.