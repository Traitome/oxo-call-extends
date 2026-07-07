---
name: rearr
category: alignment
description: REARR performs chimeric alignment of CRISPR-seq data for genome editing analysis.
tags: [rearr, alignment, crispr, genome-editing]
author: oxo-call-community
source_url: "https://ljw20180420.github.io/rearr"
---

## Concepts

- **Tool Overview**: rearr aligns CRISPR.
- **Core Function**: Chimeric alignment.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts CRISPR-seq reads.
- **Output**: Produces alignments.
- **Use Case**: Genome editing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects alignment.
- **Parameters**: Must be configured.
- **Runtime**: Alignment may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rearr --help`
**Explanation:** Shows available options and usage instructions.

### Align CRISPR reads
**Args:** `rearr align -i crispr_reads.fastq -r reference.fasta -o alignments.sam`
**Explanation:** Aligns CRISPR-seq reads.

### With parameters
**Args:** `rearr align -i crispr_reads.fastq -p params.yaml -o alignments.sam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rearr -v align -i crispr_reads.fastq -o alignments.sam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rearr -t 4 align -i crispr_reads.fastq -o alignments.sam`
**Explanation:** Uses 4 threads for parallel processing.

### With guide RNA
**Args:** `rearr align -i crispr_reads.fastq -g guide_rna.txt -o alignments.sam`
**Explanation:** Uses guide RNA sequences.

### Generate report
**Args:** `rearr align -i crispr_reads.fastq -o alignments.sam --report report.html`
**Explanation:** Generates HTML report.