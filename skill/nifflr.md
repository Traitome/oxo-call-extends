---
name: nifflr
category: expression
description: NIFFLR identifies novel isoforms from long-read RNA sequencing data.
tags: [nifflr, expression, isoforms, long-reads]
author: oxo-call-community
source_url: "https://github.com/alguoo314/NIFFLR"
---

## Concepts

- **Tool Overview**: NIFFLR discovers novel isoforms from long-read RNA sequencing data.
- **Core Function**: Identifies alternative splicing events and novel transcripts.
- **Algorithm**: Uses alignment and clustering to detect isoform diversity.
- **Input Format**: Accepts BAM files with long-read alignments.
- **Output**: Produces isoform annotations and expression estimates.
- **Use Case**: Transcriptomics analysis, isoform discovery, and gene expression.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Read Quality**: Results depend on input read quality.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Annotation Dependencies**: May require reference annotations.

## Examples

### Display help
**Args:** `nifflr --help`
**Explanation:** Shows available options and usage instructions.

### Run isoform discovery
**Args:** `nifflr -i alignment.bam -r reference.fasta -o isoforms.gtf`
**Explanation:** Identifies novel isoforms from aligned reads.

### With annotations
**Args:** `nifflr -i alignment.bam -r reference.fasta -a annotations.gtf -o isoforms.gtf`
**Explanation:** Uses existing annotations for comparison.

### Minimum reads
**Args:** `nifflr -i alignment.bam -r reference.fasta -m 3 -o isoforms.gtf`
**Explanation:** Sets minimum read support per isoform.

### Threads
**Args:** `nifflr -i alignment.bam -r reference.fasta -t 8 -o isoforms.gtf`
**Explanation:** Uses 8 threads for parallel processing.

### Output FASTA
**Args:** `nifflr -i alignment.bam -r reference.fasta --fasta -o isoforms.fasta`
**Explanation:** Outputs isoform sequences.

### Verbose mode
**Args:** `nifflr -i alignment.bam -r reference.fasta -v -o isoforms.gtf`
**Explanation:** Runs with verbose output.