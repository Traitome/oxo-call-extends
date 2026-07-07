---
name: peaks2utr
category: annotation
description: peaks2utr annotates three_prime UTR from peak data.
tags: [peaks2utr, annotation, utr, peak]
author: oxo-call-community
source_url: "https://github.com/haessar/peaks2utr"
---

## Concepts

- **Tool Overview**: peaks2utr annotates 3' UTR regions.
- **Core Function**: Identifies UTR from peak annotations.
- **Algorithm**: Uses parallelized Python processing.
- **Input Format**: Accepts peak and alignment files.
- **Output**: Produces UTR annotations.
- **Use Case**: Gene annotation, transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large peak sets require memory.
- **Peak Quality**: Results depend on peak quality.
- **Annotation Accuracy**: Requires proper gene models.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peaks2utr --help`
**Explanation:** Shows available options and usage instructions.

### Annotate UTR
**Args:** `peaks2utr -i peaks.bed -g genome.fasta -o utr.gff`
**Explanation:** Annotates 3' UTR from peaks.

### With annotation
**Args:** `peaks2utr -i peaks.bed -a annotation.gtf -o utr.gff`
**Explanation:** Uses gene annotation for UTR.

### Verbose mode
**Args:** `peaks2utr -v -i peaks.bed -o utr.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peaks2utr -t 4 -i peaks.bed -o utr.gff`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peaks2utr -i peaks.bed -o utr.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `peaks2utr -i peaks.bed -o utr.gff --report report.html`
**Explanation:** Generates HTML report.