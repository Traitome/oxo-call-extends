---
name: reditools3
category: expression
description: REDItools3 is an RNA editing detection tool implemented in Python3 for analyzing RNA-seq data.
tags: [reditools3, expression, rna-editing, rna-seq]
author: oxo-call-community
source_url: "https://github.com/BioinfoUNIBA/REDItools3"
---

## Concepts

- **Tool Overview**: reditools3 detects editing.
- **Core Function**: RNA editing detection.
- **Algorithm**: Uses comparison methods.
- **Input Format**: Accepts RNA-seq data.
- **Output**: Produces editing sites.
- **Use Case**: Transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Detection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reditools3 --help`
**Explanation:** Shows available options and usage instructions.

### Detect editing
**Args:** `reditools3 detect -i rna_reads.bam -r reference.fasta -o editing_sites.txt`
**Explanation:** Detects RNA editing sites.

### With parameters
**Args:** `reditools3 detect -i rna_reads.bam -p params.yaml -o editing_sites.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reditools3 -v detect -i rna_reads.bam -o editing_sites.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reditools3 -t 4 detect -i rna_reads.bam -o editing_sites.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With DNA reference
**Args:** `reditools3 detect -i rna_reads.bam -d dna_reads.bam -o editing_sites.txt`
**Explanation:** Uses DNA reference for comparison.

### Generate report
**Args:** `reditools3 detect -i rna_reads.bam -o editing_sites.txt --report report.html`
**Explanation:** Generates HTML report.