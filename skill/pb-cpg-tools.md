---
name: pb-cpg-tools
category: epigenomics
description: pb-CpG-tools provides tools for analyzing CpG methylation data from PacBio sequencing.
tags: [pb-cpg-tools, epigenomics, cpg, methylation]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pb-CpG-tools"
---

## Concepts

- **Tool Overview**: pb-CpG-tools analyzes methylation data.
- **Core Function**: Processes CpG methylation data.
- **Algorithm**: Uses statistical analysis for methylation calling.
- **Input Format**: Accepts PacBio sequencing data.
- **Output**: Produces methylation calls and statistics.
- **Use Case**: Epigenomics, DNA methylation analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Coverage**: Requires sufficient coverage for calling.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pb-cpg-tools --help`
**Explanation:** Shows available options and usage instructions.

### Call methylation
**Args:** `pb-cpg-tools call -i input.bam -o methylation.txt`
**Explanation:** Calls CpG methylation from BAM file.

### With reference
**Args:** `pb-cpg-tools call -i input.bam -r reference.fasta -o methylation.txt`
**Explanation:** Uses reference genome for calling.

### Verbose mode
**Args:** `pb-cpg-tools -v call -i input.bam -o methylation.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pb-cpg-tools -t 8 call -i input.bam -o methylation.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pb-cpg-tools call -i input.bam -o methylation.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `pb-cpg-tools report -i methylation.txt -o report.html`
**Explanation:** Generates HTML report.