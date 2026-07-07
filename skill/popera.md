---
name: popera
category: epigenomics
description: popera identifies DNase I hypersensitive sites.
tags: [popera, epigenomics, dnase, regulatory]
author: oxo-call-community
source_url: "https://github.com/forrestzhang/Popera"
---

## Concepts

- **Tool Overview**: popera analyzes DNase-seq data.
- **Core Function**: DHS identification.
- **Algorithm**: Uses signal processing methods.
- **Input Format**: Accepts BAM/BED files.
- **Output**: Produces DHS annotations.
- **Use Case**: Epigenomics, regulatory element analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Detection Accuracy**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `popera --help`
**Explanation:** Shows available options and usage instructions.

### Identify DHS
**Args:** `popera -i dnase.bam -o dhs.bed`
**Explanation:** Identifies DNase I hypersensitive sites.

### With parameters
**Args:** `popera -i dnase.bam -p params.yaml -o dhs.bed`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `popera -v -i dnase.bam -o dhs.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `popera -t 4 -i dnase.bam -o dhs.bed`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `popera -i dnase.bam -o dhs.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `popera -i dnase.bam -o dhs.bed --report report.html`
**Explanation:** Generates HTML report.