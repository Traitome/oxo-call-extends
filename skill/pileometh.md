---
name: pileometh
category: epigenomics
description: pileometh extracts methylation data from BS-seq experiments.
tags: [pileometh, epigenomics, methylation, bs-seq]
author: oxo-call-community
source_url: "https://github.com/dpryan79/PileOMeth"
---

## Concepts

- **Tool Overview**: pileometh extracts methylation data.
- **Core Function**: BS-seq methylation extraction.
- **Algorithm**: Uses methylation calling methods.
- **Input Format**: Accepts BS-seq data files.
- **Output**: Produces methylation extraction results.
- **Use Case**: Epigenomics, methylation analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Methylation Calling**: May have calling errors.
- **Runtime**: Extraction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pileometh --help`
**Explanation:** Shows available options and usage instructions.

### Extract methylation
**Args:** `pileometh -i bs_seq_data.bam -o methylation_results.txt`
**Explanation:** Extracts methylation from BS-seq data.

### With parameters
**Args:** `pileometh -i bs_seq_data.bam -p params.yaml -o methylation_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pileometh -v -i bs_seq_data.bam -o methylation_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pileometh -t 4 -i bs_seq_data.bam -o methylation_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pileometh -i bs_seq_data.bam -o methylation_results.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `pileometh -i bs_seq_data.bam -o methylation_results.txt --report report.html`
**Explanation:** Generates HTML report.