---
name: ribocutter
category: genome-editing
description: RiboCutter designs sgRNA oligos from abundant sequences in FASTQ files.
tags: [ribocutter, genome-editing, sgRNA-design, crispr]
author: oxo-call-community
source_url: "https://github.com/Delayed-Gitification/ribocutter.git"
---

## Concepts

- **Tool Overview**: ribocutter designs sgRNAs.
- **Core Function**: sgRNA oligo design.
- **Algorithm**: Uses sequence analysis methods.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces sgRNA sequences.
- **Use Case**: CRISPR editing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Sequence Quality**: Affects design.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ribocutter --help`
**Explanation:** Shows available options and usage instructions.

### Design sgRNAs
**Args:** `ribocutter design -i reads.fastq -o sgRNAs.txt`
**Explanation:** Designs sgRNA oligos from abundant sequences.

### With parameters
**Args:** `ribocutter design -i reads.fastq -p params.yaml -o sgRNAs.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ribocutter -v design -i reads.fastq -o sgRNAs.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ribocutter -t 4 design -i reads.fastq -o sgRNAs.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `ribocutter design -i reads.fastq -r genome.fasta -o sgRNAs.txt`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `ribocutter design -i reads.fastq -o sgRNAs.txt --report report.html`
**Explanation:** Generates HTML report.