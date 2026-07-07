---
name: psytrans
category: expression
description: psytrans separates parasite and symbiont transcriptomes from mixed sequencing data.
tags: [psytrans, expression, transcriptomics, parasite]
author: oxo-call-community
source_url: "https://github.com/rivera10/psytrans"
---

## Concepts

- **Tool Overview**: psytrans separates transcriptomes.
- **Core Function**: Transcriptome separation.
- **Algorithm**: Uses sequence alignment.
- **Input Format**: Accepts mixed RNA-seq reads.
- **Output**: Produces separated transcriptomes.
- **Use Case**: Parasite-host transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Sequence Similarity**: May affect separation.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psytrans --help`
**Explanation:** Shows available options and usage instructions.

### Separate transcriptomes
**Args:** `psytrans -i mixed_reads.fastq -r host_reference.fasta -p parasite_reference.fasta -o output_dir`
**Explanation:** Separates parasite/symbiont from host transcriptomes.

### With parameters
**Args:** `psytrans -i mixed_reads.fastq -r host_reference.fasta -p parasite_reference.fasta -params params.yaml -o output_dir`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psytrans -v -i mixed_reads.fastq -r host_reference.fasta -p parasite_reference.fasta -o output_dir`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psytrans -t 4 -i mixed_reads.fastq -r host_reference.fasta -p parasite_reference.fasta -o output_dir`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `psytrans -i mixed_reads.fastq -r host_reference.fasta -p parasite_reference.fasta -o output_dir --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `psytrans -i mixed_reads.fastq -r host_reference.fasta -p parasite_reference.fasta -o output_dir --report report.html`
**Explanation:** Generates HTML report.